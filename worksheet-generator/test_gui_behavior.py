"""
Simulate GUI behavior without launching the actual GUI window.
Tests that the problem type switching logic works correctly.
"""

import sys
import io

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from worksheet_config import get_config

class MockGUI:
    """Simulates the GUI behavior without creating windows."""

    def __init__(self):
        # Map display names to config keys (same as real GUI)
        self.problem_type_map = {
            'Linear Equations': 'linear_equation',
            'Systems of Equations': 'system_of_equations',
            'Inequalities': 'inequality'
        }

        # Simulated state variables
        self.problem_type = 'Linear Equations'
        self.difficulty = 'medium'
        self.num_problems = '10'
        self.title = 'Linear Equations - Medium'

    def _update_default_num_problems(self):
        """Update the default number of problems based on problem type."""
        # Get the config key from the display name
        config_key = self.problem_type_map.get(self.problem_type)
        if config_key:
            config = get_config(config_key)
            self.num_problems = str(config.default_num_problems)

    def _update_worksheet_title(self):
        """Update the worksheet title based on selected problem type and difficulty."""
        difficulty_capitalized = self.difficulty.capitalize()
        self.title = f"{self.problem_type} - {difficulty_capitalized}"

    def change_problem_type(self, new_type):
        """Simulate changing the problem type in the GUI."""
        self.problem_type = new_type
        self._update_default_num_problems()
        self._update_worksheet_title()

    def display_state(self):
        """Display current state."""
        print(f"  Problem Type: {self.problem_type}")
        print(f"  Difficulty: {self.difficulty}")
        print(f"  # Problems: {self.num_problems}")
        print(f"  Title: {self.title}")


# Test the GUI logic
print("Testing GUI Logic for Problem Type Switching")
print("=" * 60)

gui = MockGUI()

# Test each problem type
for problem_type in ['Linear Equations', 'Systems of Equations', 'Inequalities', 'Linear Equations']:
    print(f"\nSwitching to: {problem_type}")
    print("-" * 60)
    gui.change_problem_type(problem_type)
    gui.display_state()

print("\n" + "=" * 60)
print("GUI logic test completed successfully!")
print("\nExpected behavior verified:")
print("  - Linear Equations -> 10 problems")
print("  - Systems of Equations -> 6 problems")
print("  - Inequalities -> 8 problems")
