"""
Systems of linear equations generator for math worksheets.
Generates systems with varying difficulty levels and tracks solutions.
"""

import random
from typing import Tuple, List
from dataclasses import dataclass


@dataclass
class SystemProblem:
    """Represents a system of equations problem with its solution."""
    equation1_latex: str  # First equation in LaTeX
    equation2_latex: str  # Second equation in LaTeX
    latex: str  # Combined display format
    solution_x: float  # Solution for x
    solution_y: float  # Solution for y
    solution: str  # Formatted solution string
    steps: List[str]  # Solution steps (for future expansion)
    difficulty: str  # Difficulty level
    method: str  # Suggested solution method (substitution, elimination, etc.)


class SystemsOfEquationsGenerator:
    """Generates random systems of linear equations with different difficulty levels."""

    def __init__(self, seed=None):
        """
        Initialize the systems generator.

        Args:
            seed: Random seed for reproducibility (optional)
        """
        if seed:
            random.seed(seed)

    def generate_system(self, difficulty: str) -> SystemProblem:
        """
        Generate a system of equations based on difficulty level.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            SystemProblem object with equations and solution
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        elif difficulty == 'challenge':
            return self._generate_challenge()
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[SystemProblem]:
        """
        Generate multiple systems for a worksheet.

        Args:
            difficulty: Difficulty level
            num_problems: Number of problems to generate

        Returns:
            List of SystemProblem objects
        """
        return [self.generate_system(difficulty) for _ in range(num_problems)]

    def _generate_easy(self) -> SystemProblem:
        """
        Generate easy systems: One equation already solved for a variable.
        Example: y = 2x + 3
                 x + y = 9
        Method: Substitution (obvious)
        """
        # Choose solution
        x = random.randint(-5, 10)
        y = random.randint(-5, 10)

        # First equation: y = mx + b (already solved for y)
        m = random.randint(-3, 5)
        while m == 0:
            m = random.randint(-3, 5)
        b = y - m * x

        # Second equation: ax + by = c
        a = random.randint(1, 5)
        b_coef = random.randint(1, 5)
        c = a * x + b_coef * y

        # Format equations
        eq1_latex = f"y = {m}x + {b}" if b >= 0 else f"y = {m}x - {abs(b)}"

        if b_coef == 1:
            eq2_latex = f"{a}x + y = {c}"
        else:
            eq2_latex = f"{a}x + {b_coef}y = {c}"

        # Combined display
        latex = f"\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}"

        solution = f"({x}, {y})"
        steps = [
            f"Substitute y = {m}x + {b} into equation 2",
            f"Solve for x: x = {x}",
            f"Substitute back: y = {y}"
        ]

        return SystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            latex=latex,
            solution_x=x,
            solution_y=y,
            solution=solution,
            steps=steps,
            difficulty='easy',
            method='substitution'
        )

    def _generate_medium(self) -> SystemProblem:
        """
        Generate medium systems: Standard form, good for elimination.
        Example: 2x + 3y = 13
                 x - y = -1
        Method: Elimination or substitution
        """
        # Choose solution
        x = random.randint(-8, 12)
        y = random.randint(-8, 12)

        # First equation: a1*x + b1*y = c1
        a1 = random.randint(1, 6)
        b1 = random.randint(1, 6)
        c1 = a1 * x + b1 * y

        # Second equation: a2*x + b2*y = c2
        # Make coefficients different to avoid dependent equations
        a2 = random.randint(1, 6)
        b2 = random.randint(-6, 6)
        while b2 == 0:
            b2 = random.randint(-6, 6)
        c2 = a2 * x + b2 * y

        # Format equations with proper signs
        eq1_latex = self._format_standard_form(a1, b1, c1)
        eq2_latex = self._format_standard_form(a2, b2, c2)

        latex = f"\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}"

        solution = f"({x}, {y})"
        steps = [
            "Use elimination or substitution",
            f"x = {x}",
            f"y = {y}"
        ]

        return SystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            latex=latex,
            solution_x=x,
            solution_y=y,
            solution=solution,
            steps=steps,
            difficulty='medium',
            method='elimination'
        )

    def _generate_hard(self) -> SystemProblem:
        """
        Generate hard systems: Larger coefficients, may need multiplication before elimination.
        Example: 3x + 5y = 19
                 7x - 2y = 8
        """
        # Choose solution
        x = random.randint(-6, 10)
        y = random.randint(-6, 10)

        # First equation with larger coefficients
        a1 = random.randint(2, 8)
        b1 = random.randint(2, 8)
        c1 = a1 * x + b1 * y

        # Second equation - make sure it's not a simple multiple of first
        a2 = random.randint(2, 9)
        while a2 == a1:
            a2 = random.randint(2, 9)

        b2 = random.randint(-9, -2) if random.choice([True, False]) else random.randint(2, 9)
        c2 = a2 * x + b2 * y

        eq1_latex = self._format_standard_form(a1, b1, c1)
        eq2_latex = self._format_standard_form(a2, b2, c2)

        latex = f"\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}"

        solution = f"({x}, {y})"
        steps = [
            "Multiply equations to align coefficients",
            "Use elimination",
            f"x = {x}, y = {y}"
        ]

        return SystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            latex=latex,
            solution_x=x,
            solution_y=y,
            solution=solution,
            steps=steps,
            difficulty='hard',
            method='elimination'
        )

    def _generate_challenge(self) -> SystemProblem:
        """
        Generate challenge systems: Fractions or decimals in coefficients, or three-variable systems.
        For now: Systems with fraction solutions that need careful work.
        Example: 5x + 3y = 11
                 3x + 2y = 7
        """
        # Choose solution (may include fractions)
        # Start with a solution and work backwards
        x_num = random.randint(-10, 10)
        x_den = random.choice([1, 1, 1, 2, 3, 4])  # Mostly integers, some fractions

        y_num = random.randint(-10, 10)
        y_den = random.choice([1, 1, 1, 2, 3, 4])

        x = x_num / x_den
        y = y_num / y_den

        # Create equations that will produce this solution
        a1 = random.randint(3, 12)
        b1 = random.randint(3, 12)
        c1 = a1 * x + b1 * y

        a2 = random.randint(3, 12)
        while a2 == a1:
            a2 = random.randint(3, 12)

        b2 = random.randint(-12, -3) if random.choice([True, False]) else random.randint(3, 12)
        c2 = a2 * x + b2 * y

        # Round c values to avoid floating point mess
        c1 = round(c1)
        c2 = round(c2)

        # Recalculate actual solution based on rounded c values
        # Solve the system: a1*x + b1*y = c1, a2*x + b2*y = c2
        det = a1 * b2 - a2 * b1
        if det != 0:
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det

        eq1_latex = self._format_standard_form(a1, b1, c1)
        eq2_latex = self._format_standard_form(a2, b2, c2)

        latex = f"\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}"

        # Format solution
        if x == int(x) and y == int(y):
            solution = f"({int(x)}, {int(y)})"
        else:
            solution = f"({x:.2f}, {y:.2f})" if x != int(x) or y != int(y) else f"({int(x)}, {int(y)})"

        steps = [
            "Use elimination with larger coefficients",
            "Simplify carefully",
            f"Solution: {solution}"
        ]

        return SystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            latex=latex,
            solution_x=x,
            solution_y=y,
            solution=solution,
            steps=steps,
            difficulty='challenge',
            method='elimination'
        )

    def _format_standard_form(self, a: float, b: float, c: float) -> str:
        """
        Format equation in standard form: ax + by = c with proper signs.

        Args:
            a: coefficient of x
            b: coefficient of y
            c: constant

        Returns:
            LaTeX formatted equation
        """
        # Handle x term
        if a == 1:
            x_term = "x"
        elif a == -1:
            x_term = "-x"
        else:
            x_term = f"{int(a) if a == int(a) else a}x"

        # Handle y term with sign
        if b == 1:
            y_term = "+ y"
        elif b == -1:
            y_term = "- y"
        elif b > 0:
            y_term = f"+ {int(b) if b == int(b) else b}y"
        else:
            y_term = f"- {int(abs(b)) if abs(b) == int(abs(b)) else abs(b)}y"

        # Format constant
        c_str = str(int(c) if c == int(c) else c)

        return f"{x_term} {y_term} = {c_str}"


# Example usage and testing
if __name__ == "__main__":
    generator = SystemsOfEquationsGenerator()

    print("Systems of Equations Generator Test\n")

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Examples:")
        for i in range(2):
            system = generator.generate_system(difficulty)
            print(f"\n  System {i + 1}:")
            print(f"    {system.equation1_latex}")
            print(f"    {system.equation2_latex}")
            print(f"    Solution: {system.solution}")
            print(f"    Method: {system.method}")
