import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Prints a styled header."""
    print("\n" + "=" * 40)
    print(f"   {title.upper()}")
    print("=" * 40)