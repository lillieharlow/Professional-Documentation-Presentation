"""
styling.py: Styling for the CLI app using Rich, pyfiglet, and custom print functions. 

Imports:
- os: Helps with file and folder handling (making sure files are saved in the right place).
- pyfiglet: Facilitates creating & displaying stylised ASCII art text
- rich: Enables coloured & formatted console output including tables
"""

import os
import pyfiglet
from rich.console import Console
from rich.table import Table

console = Console(style="bold")

# ========= Basic Print Functions =========
def print_error(message:str) -> None:
    """Prints provided message in red (error)

    Parameters:
        message (str): The message to format
    
    Returns:
        None: Prints message to console"""
    console.print(f"[bold #ff0000]{message}[bold /#ff0000]", markup=True) # force rich to style all text bold in red

def print_success(message:str) -> None:
    """Prints provided message in green (success)

    Parameters:
        message (str): The message to format
    
    Returns:
        None: Prints message to console"""
    console.print(message, style="#00ff84", markup=True)

def print_info(message:str) -> None:
    """Prints provided message in yellow (info)

    Parameters:
        message (str): The message to format
    
    Returns:
        None: Prints message to console"""
    console.print(message, style="#ffe600", markup=True)

def red_text(message:str) -> str:
    """Formats provided message as bold & red colour, for use in testing
    
    Parameters:
        message (str): The message to format
    
    Returns:
        str: Formatted message"""
    return f"[bold #ff0000]{message}[bold /#ff0000]" # red text for TDD testing implementation

# ========= ASCII Art Title =========
def print_rainbow_text(text:str, font:str='ansi_shadow') -> None:
    """Prints provided message in rainbow colours & stylised using ASCII art with pyfiglet

    Parameters:
        message (str): The message to format
        font (str): The pyfiglet font to use (default = ansi_shadow)

    Returns:
        None: Prints message to console"""
    figlet_text = pyfiglet.figlet_format(text, font=font) # Convert input text to ASCII art with pyfiglet

    rich_colors = [   # List rainbow colours
        "#ff7a7a",  # Red
        "#fff27e",  # Yellow
        "#94ffcb",  # Green
        "#9eeaff",  # Blue
        "#d382ff",  # Purple
        "#fe85c2"   # Pink
    ]
    
    lines = figlet_text.splitlines()  # Split the ASCII art into lines for processing
    max_line_length = max(len(line) for line in lines) if lines else 0 # Find length of longest line to set total width for padding
    total_width = max_line_length + 8  # 4 spaces of padding on each side

    for _ in range(2):
        console.print(" " * total_width) # Print 2 empty lines for padding at top

    for i, line in enumerate(lines): # Loop through each line of the ASCII art
        colored_line = ""  # Store the coloured version of the line
        for j, char in enumerate(line): # Loop through each char in the line
            color_index = (j + i) % len(rich_colors) # Pick colour and cycle through rainbow colours
            color = rich_colors[color_index]
            colored_line += f"[bold {color}]{char}[/bold {color}]" # Add Rich markup to bold and colour char

        left_padding = "    " # padding on left
        right_padding = " " * (total_width - len(line) - 4) # padding on right
        padded_line = left_padding + colored_line + right_padding # combine left and right
        console.print(padded_line) # Print padded line

    console.print(" " * total_width) # Bottom padding

# ========= App Title =========
def show_app_title():
    """Helper function that prints the configured app title to console

    Returns:
        None: Prints title to console"""
    console.print("="*50)
    print_rainbow_text("TO DO.", font='ansi_shadow')
    console.print("="*50 + "\n")

# ========= Task Table =========
def create_task_table(username):
    """Display provided users tasks in a table format. Each column has different colour.
        
    Parameters:
        username (str): Username of the logged in user
    
    Returns:
        Table (rich): Table object containing users tasks
    """
    table = Table(title=f"{username}'s Tasks", style="#00fbff", show_header=True)

    table.add_column("TASK #", width=8, justify="center", header_style="#d382ff") # Purple
    table.add_column("TASK", min_width=30, justify="center", header_style="#fe85c2") # Pink
    table.add_column("DONE", width=8, justify="center", header_style="#ff7a7a") # Red

    return table

# ========= Print Table =========
def print_table(table:Table) -> None:
    """Prints a provided table to console
    
    Parameters: 
        table (Table): rich Table object
    
    Returns: None"""
    console.print(table)
    
# ========= Clear screen styling =========
    
def clear_screen():
    """Clear screen for better visibility, using os
    
    Returns: None"""
    os.system('clear')
    show_app_title()