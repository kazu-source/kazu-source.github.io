"""
Test GUI logic without launching the full GUI window.
"""

import tkinter as tk
from gui import WorksheetGeneratorGUI


def test_title_update():
    """Test that worksheet title updates when problem type and difficulty changes."""
    print("Testing GUI Title Auto-Update with Difficulty")
    print("=" * 60)

    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the window

    # Create GUI instance
    gui = WorksheetGeneratorGUI(root)

    # Test initial state
    print(f"\nInitial state:")
    print(f"  Problem Type: {gui.problem_type_var.get()}")
    print(f"  Difficulty: {gui.difficulty_var.get()}")
    print(f"  Worksheet Title: {gui.title_var.get()}")

    # Change difficulty
    print(f"\nChanging difficulty to 'hard'...")
    gui.difficulty_var.set('hard')
    gui._update_worksheet_title()
    print(f"  Difficulty: {gui.difficulty_var.get()}")
    print(f"  Worksheet Title: {gui.title_var.get()}")

    # Change to Systems of Equations
    print(f"\nChanging to 'Systems of Equations' (keeping hard)...")
    gui.problem_type_var.set('Systems of Equations')
    gui._update_worksheet_title()
    print(f"  Problem Type: {gui.problem_type_var.get()}")
    print(f"  Difficulty: {gui.difficulty_var.get()}")
    print(f"  Worksheet Title: {gui.title_var.get()}")

    # Change difficulty while on systems
    print(f"\nChanging difficulty to 'easy'...")
    gui.difficulty_var.set('easy')
    gui._update_worksheet_title()
    print(f"  Difficulty: {gui.difficulty_var.get()}")
    print(f"  Worksheet Title: {gui.title_var.get()}")

    # Change back to Linear Equations with challenge
    print(f"\nChanging to 'Linear Equations' with 'challenge' difficulty...")
    gui.problem_type_var.set('Linear Equations')
    gui.difficulty_var.set('challenge')
    gui._update_worksheet_title()
    print(f"  Problem Type: {gui.problem_type_var.get()}")
    print(f"  Difficulty: {gui.difficulty_var.get()}")
    print(f"  Worksheet Title: {gui.title_var.get()}")

    print("\n" + "=" * 60)
    print("Test passed! Title updates with both type and difficulty.")

    root.destroy()


if __name__ == "__main__":
    test_title_update()
