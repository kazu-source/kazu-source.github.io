"""
Simplifying Square Roots Generator
Generates problems focused on simplifying square root expressions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class SimplifyingSquareRootsGenerator:
    """Generates simplifying square roots problems."""

    # Perfect squares for reference
    PERFECT_SQUARES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
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
        """Generate easy: Perfect square roots."""
        n = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        root = int(n ** 0.5)

        latex = f"\\sqrt{{{n}}}"
        solution = str(root)

        steps = [
            f"\\text{{Find a number that multiplied by itself equals }} {n}",
            f"{root} \\times {root} = {n}",
            f"\\sqrt{{{n}}} = {root}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium: Simplify non-perfect squares with one perfect square factor."""
        # Create number with one perfect square factor
        perfect = random.choice([4, 9, 16, 25])
        other = random.choice([2, 3, 5, 6, 7])
        n = perfect * other
        root_perfect = int(perfect ** 0.5)

        latex = f"\\sqrt{{{n}}}"
        solution = f"{root_perfect}\\sqrt{{{other}}}"

        steps = [
            f"\\text{{Factor }} {n} = {perfect} \\times {other}",
            f"\\sqrt{{{n}}} = \\sqrt{{{perfect} \\times {other}}}",
            f"= \\sqrt{{{perfect}}} \\times \\sqrt{{{other}}}",
            f"= {root_perfect}\\sqrt{{{other}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard: Larger numbers or multiple simplification steps."""
        problem_type = random.choice(['large_perfect', 'two_factors', 'coefficient'])

        if problem_type == 'large_perfect':
            # Larger perfect squares
            n = random.choice([121, 144, 169, 196, 225])
            root = int(n ** 0.5)

            latex = f"\\sqrt{{{n}}}"
            solution = str(root)

            steps = [
                f"{root} \\times {root} = {n}",
                f"\\sqrt{{{n}}} = {root}"
            ]

        elif problem_type == 'two_factors':
            # Number with larger perfect square factor
            perfect = random.choice([16, 25, 36, 49])
            other = random.choice([2, 3, 5, 7])
            n = perfect * other
            root_perfect = int(perfect ** 0.5)

            latex = f"\\sqrt{{{n}}}"
            solution = f"{root_perfect}\\sqrt{{{other}}}"

            steps = [
                f"\\text{{Factor }} {n} = {perfect} \\times {other}",
                f"\\sqrt{{{n}}} = {root_perfect}\\sqrt{{{other}}}"
            ]

        else:  # coefficient
            # Coefficient outside radical
            coef = random.randint(2, 5)
            inside = random.choice([4, 9, 16, 25])
            root_inside = int(inside ** 0.5)

            latex = f"{coef}\\sqrt{{{inside}}}"
            solution = str(coef * root_inside)

            steps = [
                f"\\sqrt{{{inside}}} = {root_inside}",
                f"{coef} \\times {root_inside} = {coef * root_inside}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex simplifications or operations with radicals."""
        problem_type = random.choice(['multiply_radicals', 'add_radicals', 'nested'])

        if problem_type == 'multiply_radicals':
            # Multiply two square roots
            a = random.choice([2, 3, 5, 6])
            b = random.choice([2, 3, 5, 8])
            product = a * b

            # Check if product is a perfect square
            root = int(product ** 0.5)
            if root * root == product:
                solution = str(root)
            else:
                # Simplify if possible
                for ps in [4, 9, 16, 25]:
                    if product % ps == 0:
                        solution = f"{int(ps**0.5)}\\sqrt{{{product // ps}}}"
                        break
                else:
                    solution = f"\\sqrt{{{product}}}"

            latex = f"\\sqrt{{{a}}} \\times \\sqrt{{{b}}}"

            steps = [
                f"\\sqrt{{{a}}} \\times \\sqrt{{{b}}} = \\sqrt{{{a} \\times {b}}}",
                f"= \\sqrt{{{product}}}",
                f"= {solution}"
            ]

        elif problem_type == 'add_radicals':
            # Add like radicals
            coef1 = random.randint(2, 5)
            coef2 = random.randint(2, 5)
            inside = random.choice([2, 3, 5, 7])
            result_coef = coef1 + coef2

            latex = f"{coef1}\\sqrt{{{inside}}} + {coef2}\\sqrt{{{inside}}}"
            solution = f"{result_coef}\\sqrt{{{inside}}}"

            steps = [
                f"\\text{{Like radicals - add coefficients}}",
                f"({coef1} + {coef2})\\sqrt{{{inside}}}",
                f"= {result_coef}\\sqrt{{{inside}}}"
            ]

        else:  # nested
            # Square root of a perfect square times a number
            a = random.choice([2, 3])
            b = random.choice([4, 9, 16])
            root_b = int(b ** 0.5)
            n = a * b

            latex = f"\\sqrt{{{n}}}"
            solution = f"{root_b}\\sqrt{{{a}}}"

            steps = [
                f"{n} = {b} \\times {a}",
                f"\\sqrt{{{n}}} = \\sqrt{{{b}}} \\times \\sqrt{{{a}}}",
                f"= {root_b}\\sqrt{{{a}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SimplifyingSquareRootsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
