from __future__ import annotations


class Colors:
    """
    A class used to hold text colors.

    """
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ORANGE = '\033[38;5;208m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'
    BLACK = '\033[30m'
    DARK_BLUE = '\033[34m'
    DARK_MAGENTA = '\033[35m'

    # If you use reset at the end of a print statement, the next print statement
    # will be default color
    RESET = '\033[0m'

    # Name: color_text
    # Function: Applies color to console text
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    @staticmethod
    def color_text(text, color):
        return f"{color}{text}{Colors.RESET}"
