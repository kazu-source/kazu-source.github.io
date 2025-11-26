"""
Approximating Irrational Numbers Generator - Grade 8 Unit 1
Generates problems approximating irrational numbers
Example: Approximate √10 to the nearest tenth
"""

import random
import math
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ApproximatingIrrationalNumbersGenerator:
    """Generates approximating irrational numbers problems."""

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
        """Generate easy problems: approximate √n between two integers."""
        # Non-perfect squares between 1 and 50
        non_perfect_squares = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
        number = random.choice(non_perfect_squares)

        lower = int(math.sqrt(number))
        upper = lower + 1

        latex = f"\\text{{Between which two integers is }} \\sqrt{{{number}}}?"
        solution = f"{lower} \\text{{ and }} {upper}"
        steps = [
            f"\\sqrt{{{lower**2}}} = {lower}",
            f"\\sqrt{{{upper**2}}} = {upper}",
            f"\\text{{Since }} {lower**2} < {number} < {upper**2}, \\text{{ then }} {lower} < \\sqrt{{{number}}} < {upper}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: approximate to nearest tenth."""
        non_perfect_squares = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15]
        number = random.choice(non_perfect_squares)

        actual_value = math.sqrt(number)
        rounded_value = round(actual_value, 1)

        latex = f"\\text{{Approximate }} \\sqrt{{{number}}} \\text{{ to the nearest tenth}}"
        solution = f"{rounded_value}"
        steps = [
            f"\\sqrt{{{number}}} \\approx {actual_value:.3f}",
            f"\\text{{Rounded to nearest tenth: }} {rounded_value}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: ordering irrational numbers or approximating π."""
        problem_type = random.choice(['order', 'pi', 'compare'])

        if problem_type == 'order':
            # Order square roots
            numbers = random.sample([2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15], 3)
            numbers.sort()

            latex = f"\\text{{Order from least to greatest: }} \\sqrt{{{numbers[0]}}}, \\sqrt{{{numbers[1]}}}, \\sqrt{{{numbers[2]}}}"
            solution = f"\\sqrt{{{numbers[0]}}} < \\sqrt{{{numbers[1]}}} < \\sqrt{{{numbers[2]}}}"
            steps = [
                f"\\sqrt{{{numbers[0]}}} \\approx {math.sqrt(numbers[0]):.2f}",
                f"\\sqrt{{{numbers[1]}}} \\approx {math.sqrt(numbers[1]):.2f}",
                f"\\sqrt{{{numbers[2]}}} \\approx {math.sqrt(numbers[2]):.2f}"
            ]

        elif problem_type == 'pi':
            latex = f"\\text{{Approximate }} \\pi \\text{{ to the nearest hundredth}}"
            solution = "3.14"
            steps = [
                "\\pi \\approx 3.14159...",
                "\\text{Rounded to nearest hundredth: } 3.14"
            ]

        else:  # compare
            num1 = random.choice([2, 3, 5, 6, 7])
            num2 = random.choice([8, 10, 11, 12, 13, 15])

            val1 = math.sqrt(num1)
            val2 = math.sqrt(num2)

            latex = f"\\text{{Which is greater: }} \\sqrt{{{num1}}} \\text{{ or }} \\sqrt{{{num2}}}?"
            solution = f"\\sqrt{{{num2}}}"
            steps = [
                f"\\sqrt{{{num1}}} \\approx {val1:.2f}",
                f"\\sqrt{{{num2}}} \\approx {val2:.2f}",
                f"\\sqrt{{{num2}}} > \\sqrt{{{num1}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex approximations and expressions."""
        problem_type = random.choice(['expression', 'locate', 'cube_root'])

        if problem_type == 'expression':
            # Approximate √a + √b
            num1 = random.choice([2, 3, 5])
            num2 = random.choice([6, 7, 8, 10])

            val1 = math.sqrt(num1)
            val2 = math.sqrt(num2)
            total = val1 + val2

            latex = f"\\text{{Approximate }} \\sqrt{{{num1}}} + \\sqrt{{{num2}}} \\text{{ to the nearest tenth}}"
            solution = f"{round(total, 1)}"
            steps = [
                f"\\sqrt{{{num1}}} \\approx {val1:.3f}",
                f"\\sqrt{{{num2}}} \\approx {val2:.3f}",
                f"{val1:.3f} + {val2:.3f} \\approx {total:.3f}",
                f"\\text{{Rounded: }} {round(total, 1)}"
            ]

        elif problem_type == 'locate':
            # Locate √n on number line
            number = random.choice([5, 6, 7, 8, 10, 11, 12])
            value = math.sqrt(number)
            lower = int(value)
            upper = lower + 1

            # Determine if closer to lower or upper
            if value - lower < 0.5:
                closer = f"\\text{{closer to }} {lower}"
            else:
                closer = f"\\text{{closer to }} {upper}"

            latex = f"\\text{{Is }} \\sqrt{{{number}}} \\text{{ closer to }} {lower} \\text{{ or }} {upper}?"
            solution = closer
            steps = [
                f"\\sqrt{{{number}}} \\approx {value:.2f}",
                f"\\text{{Distance to {lower}: }} {abs(value - lower):.2f}",
                f"\\text{{Distance to {upper}: }} {abs(value - upper):.2f}",
                closer
            ]

        else:  # cube_root
            # Approximate cube root
            numbers = [10, 15, 20, 25, 30]
            number = random.choice(numbers)

            value = number ** (1/3)
            lower = int(value)
            upper = lower + 1

            latex = f"\\text{{Between which two integers is }} \\sqrt[3]{{{number}}}?"
            solution = f"{lower} \\text{{ and }} {upper}"
            steps = [
                f"\\sqrt[3]{{{lower**3}}} = {lower}",
                f"\\sqrt[3]{{{upper**3}}} = {upper}",
                f"{lower} < \\sqrt[3]{{{number}}} < {upper}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ApproximatingIrrationalNumbersGenerator()

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
