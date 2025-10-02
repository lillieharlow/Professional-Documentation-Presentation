"""
tasks.py: helps a user keep track of their tasks. 

Imports:
- json: Save and load tasks as text files (like storing tasks in a notebook).
- os: Helps with file and folder handling (making sure files are saved in the right place).
- emoji_library: Custom file that holds emoji icons for task completion, priority, etc.
- styling: Custom file for styling the terminal (colours, tables, clearing the screen).
- utils: Custom file with helper functions (like showing “no tasks” messages).
"""

import json
import os
from emoji_library import complete, incomplete, interesting, high, medium, low
from styling import *
from utils import print_no_tasks

# ========= Task class =========
class Task:
    """Represents a single task with a title and completion status.
    Purpose: Create, complete, and manage tasks.
    Inheritance: Base class for PriorityTask.
    Methods: __init__, mark_complete, mark_incomplete, __str__, title_upper, is_high_priority.
    Variables: title (str), completed (bool)."""
    
    # ===== Create new task =====
    def __init__(self, title: str) -> None:
        """Initialize a new task with a title and set it as incomplete.
        Parameters: title (str): The title of the task.
        Returns: None"""
        self.title = title
        self.completed = False
    
    # ===== Task complete =====
    def mark_complete(self) -> None:
        """Mark the task as complete.
        Returns: None"""
        self.completed = True
    
    # ===== Task incomplete =====
    def mark_incomplete(self) -> None:
        """Mark the task as incomplete.
        Returns: None"""
        self.completed = False

    def __str__(self) -> str:
        """Return the task title as a string.
        Returns: str: The task title."""
        return self.title

    # ===== task UPPERCASE (TDD 1 feature) =====
    def title_upper(self) -> str:
        """Return the task title in uppercase.
        Returns: str: The task title in uppercase."""
        return self.title.upper()
    
    # ===== Check if task is high priority (TDD 2 feature) =====
    def is_high_priority(self) -> bool:
        """Check if task is high priority (always False for base Task).
        Returns: bool: Always False for base Task."""
        return False

# ========= Task priority =========
class PriorityTask(Task):
    """Represents a task with a priority level (High, Medium, Low).
    Purpose: Create and manage tasks with priority.
    Inheritance: Inherits from Task class.
    Methods: __init__, __str__, is_high_priority.
    Variables: priority (str)."""
    
    def __init__(self, title: str, priority: str) -> None:
        """Initialize a new priority task with a title and priority level.
        Parameters: title (str): Title of the task.
                    priority (str): Task priority level ("High", "Medium", "Low").
        Returns: None"""
        super().__init__(title) # Call parent class constructor
        self.priority: str = priority

    def __str__(self) -> str:  # Priority level mapped as emoji
        """Return the task title with a priority emoji, emoji is based on priority level.
        Returns: str: Task title with priority emoji."""
        if self.priority == "High":
            prio_emoji = high
        elif self.priority == "Medium":
            prio_emoji = medium
        elif self.priority == "Low":
            prio_emoji = low
        else:
            prio_emoji = ""
        return f"{prio_emoji} {self.title}" # Adds priority emoji to task title
        
    def is_high_priority(self) -> bool:
        """Check if task is high priority.
        Returns: bool: True if priority is "High", else False."""
        return self.priority == "High"

# ========= TaskList class =========
class TaskList:
    """Manages a list of tasks for a user, including adding, deleting,
    completing, displaying, saving, and loading tasks.
    Purpose: Manage a user's task list.
    Composition: Contains multiple Task and PriorityTask objects.
    Methods: __init__, add_task, delete_task, mark_complete, get_tasks, display_tasks, save_tasks, load_tasks
        is_valid_task_number, show_invalid_number_error.
    Variables: username (str), tasks (Task), index (int), filename (str)."""

    # ===== Setup task list =====
    def __init__(self, username: str) -> None:
        """Initialize a TaskList for a user, load any existing tasks.
        Parameters: username (str): The name of the user.
        Returns: None"""
        self.username: str = username
        self.tasks: list[Task] = []
        self.filename: str = f"data/{username}_tasks.json"
        self.load_tasks()
    
    # ===== Add new task =====
    def add_task(self, task: Task) -> None:
        """Add a new task to the task list and save to file.
        Parameters: task (Task): The task to add.
        Returns: None"""
        self.tasks.append(task)
        self.save_tasks()
        clear_screen()
        print_success(f"Nice cache! {task.title} was added to your tasks!")

    # ===== Delete task by index =====
    def delete_task(self, index: int) -> None:
        """Delete a task from the task list by its index and save to file.
        Parameters: index (int): The index of the task to delete.
        Returns: None"""
        if self.is_valid_task_number(index):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
        else:
            self.show_invalid_number_error()
            return None
    
    # ===== Complete task by index =====
    def mark_complete(self, index: int) -> None:
        """Mark a task as complete by its index and save to file.
        Parameters: index (int): The index of the task to mark as complete.
        Returns: None"""
        if self.is_valid_task_number(index):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print_success(f"Great job! {self.tasks[index].title} is now complete!")
        else:
            self.show_invalid_number_error()

    # ===== Get/return task list to user =====
    def get_tasks(self) -> list[Task]:
        """Return the list of tasks for this user.
        Returns: list[Task]: The list of tasks."""
        return self.tasks
    
    # ===== Display tasks =====
    def display_tasks(self) -> None:
        """Display the user's tasks in a formatted table with completion status,
        uppercase for high priority tasks, and colour.
        Returns: None"""
        if not self.tasks:
            print_no_tasks()
            return

        table = create_task_table(self.username)

        # TDD testing implementation code - makes high priority tasks bold, red and uppercase
        for i, task in enumerate(self.tasks, 1):
            status = complete if task.completed else incomplete
            # High priority PriorityTask: uppercase and red, keep original emoji
            if isinstance(task, PriorityTask) and task.is_high_priority():
                base = task.__str__()
                prio_emoji = base.replace(task.title, '').strip()
                display_title = f"{prio_emoji} {task.title_upper()}"
                display_title = red_text(display_title)
            elif isinstance(task, PriorityTask):
                display_title = task.__str__()
            else:
                display_title = str(task)
            table.add_row(str(i), display_title, status)

        print_table(table)
    
    # ===== Save tasks to users file =====
    def save_tasks(self) -> None:
        """Save the current list of tasks to a JSON file for persistent storage.
        Returns: None"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        task_data = []
        for task in self.tasks:
            task_info = {
                "title": task.title,
                "completed": task.completed,
                "type": task.__class__.__name__
            }
            if isinstance(task, PriorityTask):
                task_info["priority"] = task.priority
            task_data.append(task_info)
        try:
            with open(self.filename, 'w') as file:
                json.dump(task_data, file, indent=2)
        except Exception as e:
            print_error(f"\nThis is awkward {interesting}. JaSON couldn't save tasks because {e}")

    # ===== Load tasks from users file =====
    def load_tasks(self) -> None:
        """Load tasks from a JSON file (if it exists). Otheriwse, start with empty list.
        Returns: None
        """
        try:
            with open(self.filename, 'r') as file:
                task_data = json.load(file)
            self.tasks = []
            for data in task_data:
                if data.get("type") == "PriorityTask":
                    task = PriorityTask(data["title"], data.get("priority", "Medium"))
                else:
                    task = Task(data["title"])
                task.completed = data["completed"]
                self.tasks.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []  # No tasks file yet or file is empty/corrupted - start new list
        except Exception:
            print_error("\nOh no! JaSON says... I don't like that one, start again!")
            self.tasks = []

    # ========== Helper methods =========
    
    # ===== Check if task number is valid =====
    def is_valid_task_number(self, index: int) -> bool:
        """Check if the provided index is a valid task number.
        Parameters: index (int): The index to check.
        Returns: bool: True if valid, else False."""
        return 0 <= index < len(self.tasks)
    
    # ===== Show message when user does not input valid number =====
    def show_invalid_number_error(self) -> None:
        """Display an error message when the user inputs an invalid task number.
        Returns: None"""
        print_error(f"\nCheeky! That's not a valid number. Please pick a number from the list!")