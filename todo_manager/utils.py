""" utils.py handles helper functions for the todo_manager app.
Imports:
- styling: Custom file for styling the terminal (colours, clearing the screen).
- emoji_library: Custom file that holds emoji icons for user actions (like login success, errors
"""

from styling import print_info, clear_screen, print_error
from emoji_library import interesting, cross

# ========== print_no_tasks() =========
def print_no_tasks() -> None:
    """Print a message to user when there are no tasks.
    Returns: None"""
    print_info(f"{interesting} You don't have any tasks listed, let's add some!")
    
# ========== Task Number Input =========
def get_task_number(task_list, action):
    """Get a valid task number from user for actions like delete/complete.
    Parameters: task_list: The list of tasks to choose from.
                action (str): The action being performed (e.g., "delete", "complete").
    Returns: int or None: The index of the selected task, or None if invalid."""
    if not task_list.get_tasks():
        return None
    max_num = len(task_list.get_tasks())
    
    user_input = input(f"\nWhich task do you want to {action}? (1-{max_num}): ").strip()
    try:
        index = int(user_input) - 1
        if 0 <= index < max_num:
            return index
        else:
            print_error(f"\n{cross} Cheeky! That task number isn't there!")
    except ValueError:
        print_error(f"\n{interesting} That's not a number!")
    return None
    
# ========== Retry task actions (delete/complete) ==========
def retry_task(task_list, action, action_func, after_success_msg=None, after_success_func=None):
    """Retry a task action (like delete or complete) until successful or user opts out.
    Parameters: task_list: The list of tasks to operate on.
                action (str): The action being performed (e.g., "delete", "complete").
                action_func: The function to call to perform the action.
                after_success_msg (str, optional): Message to print after successful action.
                after_success_func (function, optional): Function to call after successful action.
    Returns: None."""
    while True:
        task_list.display_tasks()
        index = get_task_number(task_list, action)
        if index is not None:
            action_func(index)
            clear_screen()
            if after_success_msg:
                print_info(after_success_msg)
            if after_success_func:
                after_success_func()
            break
        else:
            again = input("\nTry again?\n\nPress 'y' to retry or enter anything else to return to the main menu: ").strip().lower()
            if again == "y":
                clear_screen()
            else:
                clear_screen()
                break