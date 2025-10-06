"""user.py handles user management (signup, login) securely.
Imports:
- json: Save and load user data (like usernames and passwords) as text files.
- os: Helps with file and folder handling (making sure user files are saved in the right place).
- getpass: Securely get user passwords without showing them on screen.
- emoji_library: Custom file that holds emoji icons for user actions (like login success, errors).
- styling: Custom file for styling the terminal (colours, clearing the screen).
- bcrypt: Securely hash and check passwords (so we don't store plain text passwords)."""

import json
import os
from getpass import getpass
from emoji_library import emoji_person, emoji_add, emoji_cross, emoji_lock, emoji_interesting, emoji_smile
from styling import print_error, print_success, clear_screen
import bcrypt

# ========= User class =========
class User:
    """Handles user signup and login. Tracks currently logged-in user. 
    Purpose: Manage user accounts securely.
    Methods: __init__, load_users, save_users, register_user, login_user,
        get_current_user, hash_password, check_password.
    Variables: users_file (str), logged_in_user (str)."""

    # ========== Create user and set up file location ==========
    def __init__(self, users_file: str = "data/users.json"):
        """Initialize user object and set up file location for user data.
        Parameters: users_file (str): Path to the JSON file storing user data.
        Returns: None."""
        self.users_file = users_file
        self.logged_in_user = None

    # ========== Load user from json file ==========
    def load_users(self) -> dict:
        """Load users from JSON file. If file doesn't exist, return empty dict.
        Returns: dict: Dictionary of users with usernames as keys and hashed passwords (bytes) as values."""
        if not os.path.exists(self.users_file):
            return {}
        try:
            with open(self.users_file, "r") as f:
                data = json.load(f) # Convert bytes back to proper format for bcrypt
                for username, user_data in data.items():
                    if isinstance(user_data["password"], str): # Convert string back to bytes for bcrypt
                        user_data["password"] = user_data["password"].encode('latin-1')
                return data
        except Exception as e:
            print_error(f"\nError loading users: {e}")
            return {}
    
    # ========== Save user to json file ==========
    def save_users(self, users: dict) -> None:
        """Save users to JSON file.
        Parameters: users (dict): Dictionary of users with usernames as keys and hashed passwords (bytes) as values.
        Returns: None."""
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        
        try:
            users_for_json = {} # Convert bytes to string for JSON storage
            for username, user_data in users.items():
                users_for_json[username] = {
                    "password": user_data["password"].decode('latin-1')
                }
            with open(self.users_file, "w") as f:
                json.dump(users_for_json, f, indent=2)
            clear_screen()
            print_success(f"\nNice cache! Your account has been saved.")
        except Exception as e:
            print_error(f"\nUgh, JaSON didn't like that one {emoji_interesting}. Error: {e}\nPlease try again.")

    # ========== Sign up/create new user account ==========
    def register_user(self) -> str:
        """Create a new user with username and password.
        Returns: str: The username of the newly registered user."""
        users = self.load_users()
        print_success(f"\nYay! {emoji_smile} Let's create your TO DO. account!")

        while True:
            username = input(f"\n{emoji_person} Choose your username: ").strip()
            if not username:
                print_error(f"\nPlease enter a valid username!")
                continue
            if username in users:
                print_error(f"\nThat username's already taken. Please try again!")
                continue
            break

        while True:
            password = getpass(f"\n{emoji_add} Please enter your password (5+ characters): ").strip()
            if len(password) < 5:
                print_error(f"\nThat password's too short. Give me a longer one!")
                continue
            password_confirm = getpass(f"\n{emoji_add} Second time's a charm! Please re-enter your password: ").strip()
            if password != password_confirm:
                print_error(f"\nHmm {emoji_interesting} your passwords don't match. Want to try again?")
                continue
            break

        hashed_password = self.hash_password(password)  # Secure password hashing
        users[username] = {"password": hashed_password}
        self.save_users(users)
        self.logged_in_user = username
        print()
        return username

    # ========== Log in existing user - 3 attempts ==========
    def login_user(self) -> str:
        """Log in an existing user by verifying username and password.
        Returns: str: Username of the logged-in user, or None if login failed."""
        users = self.load_users()
        print_success(f"\n {emoji_smile} Please enter your login details:")

        attempts = 0
        while attempts < 3:
            username = input(f"\n{emoji_person} Username: ").strip()
            if not username:
                print_error(f"\n{emoji_cross} Please enter a valid username.")
                continue
            password = getpass(f"\n{emoji_lock} Password: ").strip()
            if username in users and self.check_password(password, users[username]["password"]): # Secure password verification
                self.logged_in_user = username
                return username
            else:
                attempts += 1
                if attempts < 3:
                    print_error(f"\nOops! That username or password didn't match {emoji_interesting}. Please try again!")
        clear_screen()
        print_error(f"\nUmm, this is awkward {emoji_interesting} Did you forget your details?\nLet's go back to the main menu.")
        return None
                
    # ========== Get current user ==========
    def get_current_user(self) -> str:
        """Return the currently logged-in user.
        Returns: str: Username of logged-in user, or None if no user is logged in."""
        return self.logged_in_user # Who's using the app right now

    # ========== Secure password hashing with bcrypt ==========
    def hash_password(self, password: str) -> bytes:
        """Hash password using bcrypt for secure storage.
        Parameters: password (str): The plain text password to hash.
        Returns: bytes: The hashed password."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password: str, hashed: bytes) -> bool:
        """Check a plain text password against a hashed password.
        Parameters: password (str): The plain text password to check.
                    hashed (bytes): The hashed password to compare against.
        Returns: bool: True if the password matches the hash, else False."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

# ========== Guest User - doesn't save tasks or login details ==========
class GuestUser(User): # Inherits from User class
    """Represents a guest user who doesn't save tasks or login details.
    Purpose: Allow temporary access without saving data.
    Inheritance: Inherits from User class.
    Methods: __init__."""
    def __init__(self) -> None:
        super().__init__()
        self.is_guest = True