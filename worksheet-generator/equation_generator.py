"""
Linear equation generator for math worksheets.
Generates equations with varying difficulty levels and tracks solutions.
"""

import random
from typing import Tuple, Dict, List
from dataclasses import dataclass


@dataclass
class Equation:
    """Represents a linear equation problem with its solution."""
    latex: str  # LaTeX formatted equation
    solution: float  # The answer
    steps: List[str]  # Solution steps (for future expansion)
    difficulty: str  # Difficulty level


class LinearEquationGenerator:
    """Generates random linear equations with different difficulty levels."""

    def __init__(self, seed=None):
        """
        Initialize the equation generator.

        Args:
            seed: Random seed for reproducibility (optional)
        """
        if seed:
            random.seed(seed)

    def generate_equation(self, difficulty: str) -> Equation:
        """
        Generate a linear equation based on difficulty level.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            Equation object with problem and solution
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

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate multiple equations for a worksheet.

        Args:
            difficulty: Difficulty level
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        return [self.generate_equation(difficulty) for _ in range(num_problems)]

    def _generate_easy(self) -> Equation:
        """Generate one-step equations: x + a = b or ax = b"""
        problem_type = random.choice(['addition', 'multiplication'])

        if problem_type == 'addition':
            # x + a = b or x - a = b
            a = random.randint(1, 20)
            x = random.randint(1, 30)
            b = x + a

            if random.choice([True, False]):
                # x + a = b
                latex = f"x + {a} = {b}"
                steps = [f"x = {b} - {a}", f"x = {x}"]
            else:
                # x - a = b
                b = x - a
                latex = f"x - {a} = {b}"
                steps = [f"x = {b} + {a}", f"x = {x}"]

        else:  # multiplication
            # ax = b
            a = random.randint(2, 12)
            x = random.randint(1, 20)
            b = a * x
            latex = f"{a}x = {b}"
            steps = [f"x = {b} \\div {a}", f"x = {x}"]

        return Equation(latex=latex, solution=x, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate two-step equations: ax + b = c"""
        a = random.randint(2, 10)
        b = random.randint(-15, 15)
        x = random.randint(-10, 20)
        c = a * x + b

        # Format with proper signs
        if b >= 0:
            latex = f"{a}x + {b} = {c}"
        else:
            latex = f"{a}x - {abs(b)} = {c}"

        steps = [
            f"{a}x = {c - b}",
            f"x = {(c - b) / a}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=x, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate multi-step equations with parentheses: a(x + b) + c = d"""
        a = random.randint(2, 8)
        b = random.randint(-10, 10)
        c = random.randint(-15, 15)
        x = random.randint(-10, 15)
        d = a * (x + b) + c

        # Format with proper signs
        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

        latex = f"{a}(x {b_str}) {c_str} = {d}"

        steps = [
            f"{a}(x {b_str}) = {d - c}",
            f"x {b_str} = {(d - c) / a}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=x, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate equations with variables on both sides: ax + b = cx + d"""
        # Ensure a != c to have a valid equation
        a = random.randint(2, 10)
        c = random.randint(1, 10)
        while c == a:
            c = random.randint(1, 10)

        b = random.randint(-15, 15)
        d = random.randint(-15, 15)

        # Calculate x
        x = (d - b) / (a - c)

        # Only generate equations with integer solutions
        if x != int(x):
            # Adjust d to ensure integer solution
            x = random.randint(-10, 20)
            d = a * x + b - c * x
        else:
            x = int(x)

        # Format with proper signs
        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

        latex = f"{a}x {b_str} = {c}x {d_str}"

        steps = [
            f"{a - c}x = {d - b}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=x, steps=steps, difficulty='challenge')


# Example usage and testing
if __name__ == "__main__":
    generator = LinearEquationGenerator()

    print("Linear Equation Generator Test\n")

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Examples:")
        for i in range(3):
            eq = generator.generate_equation(difficulty)
            print(f"  {eq.latex}")
            print(f"  Solution: x = {eq.solution}\n")
