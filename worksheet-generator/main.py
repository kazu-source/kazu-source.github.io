"""
Main entry point for the Math Worksheet Generator application.
"""

import sys
from gui import main as gui_main


def main():
    """
    Launch the Math Worksheet Generator GUI application.
    """
    print("=" * 50)
    print("Math Worksheet Generator")
    print("=" * 50)
    print("\nStarting GUI application...\n")

    try:
        gui_main()
    except KeyboardInterrupt:
        print("\n\nApplication closed by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        print("\nPlease ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
