"""
Equations with Variables on Both Sides Generator - Grade 8 Unit 2
Generates equations where variables appear on both sides
Example: 3x + 5 = 2x + 8, solve for x
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EquationsWithVariablesOnBothSidesGenerator:
    """Generates equations with variables on both sides."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy problems: simple variables on both sides."""
        # Generate x value
        x = random.randint(1, 10)

        # Left side: ax + b
        a1 = random.randint(2, 5)
        b1 = random.randint(1, 10)

        # Right side: cx + d where a1 != c
        c = random.randint(1, a1 - 1) if a1 > 1 else a1 + 1
        d = a1 * x + b1 - c * x

        latex = f"{a1}x + {b1} = {c}x + {d}"
        solution = f"x = {x}"
        steps = [
            f"{a1}x + {b1} = {c}x + {d}",
            f"{a1}x - {c}x = {d} - {b1}",
            f"{a1 - c}x = {d - b1}",
            f"x = {x}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: variables on both sides with negative coefficients."""
        x = random.randint(-5, 10)

        # Left side: ax + b
        a1 = random.randint(3, 7)
        b1 = random.randint(-8, 8)

        # Right side: cx + d
        c = random.randint(1, a1 - 1)
        d = a1 * x + b1 - c * x

        # Format with proper signs
        b1_str = f"+ {b1}" if b1 >= 0 else f"- {abs(b1)}"
        d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

        latex = f"{a1}x {b1_str} = {c}x {d_str}"
        solution = f"x = {x}"

        diff = a1 - c
        const_diff = d - b1

        steps = [
            f"{a1}x {b1_str} = {c}x {d_str}",
            f"{a1}x - {c}x = {d} - ({b1})",
            f"{diff}x = {const_diff}",
            f"x = {x}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: more complex coefficients and constants."""
        x = random.randint(-10, 10)

        # Left side: ax + b
        a1 = random.randint(4, 10)
        b1 = random.randint(-15, 15)

        # Right side: cx + d
        c = random.randint(-3, 3)
        if c == a1:
            c = c + 1
        d = a1 * x + b1 - c * x

        # Format with proper signs
        b1_str = f"+ {b1}" if b1 >= 0 else f"- {abs(b1)}"
        c_str = f"{c}x" if c >= 0 else f"- {abs(c)}x"
        d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

        latex = f"{a1}x {b1_str} = {c_str} {d_str}"
        solution = f"x = {x}"

        diff = a1 - c
        const_diff = d - b1

        steps = [
            f"{a1}x {b1_str} = {c_str} {d_str}",
            f"{a1}x - ({c})x = {d} - ({b1})",
            f"{diff}x = {const_diff}",
            f"x = \\frac{{{const_diff}}}{{{diff}}} = {x}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: fractional coefficients or complex equations."""
        problem_type = random.choice(['fractional', 'complex'])

        if problem_type == 'fractional':
            x = random.randint(2, 12)

            # Use fractions
            a1_num = random.randint(1, 3)
            a1_den = random.randint(2, 4)

            c_num = random.randint(1, 2)
            c_den = a1_den  # Same denominator for easier calculation

            b1 = random.randint(1, 10)

            # Calculate d so that x is the solution
            # a1_num/a1_den * x + b1 = c_num/c_den * x + d
            # d = a1_num/a1_den * x + b1 - c_num/c_den * x
            d = (a1_num * x) // a1_den + b1 - (c_num * x) // c_den

            latex = f"\\frac{{{a1_num}}}{{{a1_den}}}x + {b1} = \\frac{{{c_num}}}{{{c_den}}}x + {d}"
            solution = f"x = {x}"
            steps = [
                f"\\frac{{{a1_num}}}{{{a1_den}}}x + {b1} = \\frac{{{c_num}}}{{{c_den}}}x + {d}",
                f"\\frac{{{a1_num}}}{{{a1_den}}}x - \\frac{{{c_num}}}{{{c_den}}}x = {d} - {b1}",
                f"\\frac{{{a1_num - c_num}}}{{{a1_den}}}x = {d - b1}",
                f"x = {x}"
            ]
        else:  # complex
            x = random.randint(1, 8)

            # Left side: ax + bx + c = (a+b)x + c
            a = random.randint(2, 5)
            b = random.randint(1, 3)
            c = random.randint(-5, 5)

            # Right side: dx + e
            d = random.randint(1, 4)
            e = (a + b) * x + c - d * x

            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            e_str = f"+ {e}" if e >= 0 else f"- {abs(e)}"

            latex = f"{a}x + {b}x {c_str} = {d}x {e_str}"
            solution = f"x = {x}"
            steps = [
                f"{a}x + {b}x {c_str} = {d}x {e_str}",
                f"{a + b}x {c_str} = {d}x {e_str}",
                f"{a + b - d}x = {e - c}",
                f"x = {x}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EquationsWithVariablesOnBothSidesGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
