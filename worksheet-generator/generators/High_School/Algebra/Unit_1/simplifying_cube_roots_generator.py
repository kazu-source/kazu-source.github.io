"""
Simplifying Cube Roots Generator
Generates problems focused on simplifying cube root expressions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class SimplifyingCubeRootsGenerator:
    """Generates simplifying cube roots problems."""

    # Perfect cubes for reference
    PERFECT_CUBES = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

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
        """Generate easy: Perfect cube roots."""
        root = random.choice([2, 3, 4, 5])
        n = root ** 3

        latex = f"\\sqrt[3]{{{n}}}"
        solution = str(root)

        steps = [
            f"\\text{{Find a number that multiplied by itself 3 times equals }} {n}",
            f"{root} \\times {root} \\times {root} = {n}",
            f"\\sqrt[3]{{{n}}} = {root}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium: Simplify with one perfect cube factor."""
        # Create number with one perfect cube factor
        perfect_root = random.choice([2, 3])
        perfect = perfect_root ** 3
        other = random.choice([2, 3, 4, 5])
        n = perfect * other

        latex = f"\\sqrt[3]{{{n}}}"
        solution = f"{perfect_root}\\sqrt[3]{{{other}}}"

        steps = [
            f"\\text{{Factor }} {n} = {perfect} \\times {other}",
            f"\\sqrt[3]{{{n}}} = \\sqrt[3]{{{perfect} \\times {other}}}",
            f"= \\sqrt[3]{{{perfect}}} \\times \\sqrt[3]{{{other}}}",
            f"= {perfect_root}\\sqrt[3]{{{other}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard: Larger perfect cubes or negative cube roots."""
        problem_type = random.choice(['large_perfect', 'negative', 'coefficient'])

        if problem_type == 'large_perfect':
            # Larger perfect cubes
            root = random.choice([5, 6, 7])
            n = root ** 3

            latex = f"\\sqrt[3]{{{n}}}"
            solution = str(root)

            steps = [
                f"{root}^3 = {n}",
                f"\\sqrt[3]{{{n}}} = {root}"
            ]

        elif problem_type == 'negative':
            # Negative cube roots (cube roots of negative numbers)
            root = random.choice([2, 3, 4, 5])
            n = -(root ** 3)

            latex = f"\\sqrt[3]{{{n}}}"
            solution = str(-root)

            steps = [
                f"\\text{{Cube root of negative is negative}}",
                f"({-root})^3 = {n}",
                f"\\sqrt[3]{{{n}}} = {-root}"
            ]

        else:  # coefficient
            # Coefficient with cube root
            coef = random.randint(2, 4)
            root = random.choice([2, 3])
            inside = root ** 3

            latex = f"{coef}\\sqrt[3]{{{inside}}}"
            solution = str(coef * root)

            steps = [
                f"\\sqrt[3]{{{inside}}} = {root}",
                f"{coef} \\times {root} = {coef * root}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex simplifications with cube roots."""
        problem_type = random.choice(['multiply_cubes', 'simplify_large', 'mixed'])

        if problem_type == 'multiply_cubes':
            # Multiply cube roots
            a = random.choice([2, 3, 4])
            b = random.choice([2, 4, 5])
            product = a * b

            # Check if product is a perfect cube
            for i in range(1, 10):
                if i ** 3 == product:
                    solution = str(i)
                    break
            else:
                # Simplify if possible
                for cube_root in [2, 3]:
                    cube = cube_root ** 3
                    if product % cube == 0:
                        solution = f"{cube_root}\\sqrt[3]{{{product // cube}}}"
                        break
                else:
                    solution = f"\\sqrt[3]{{{product}}}"

            latex = f"\\sqrt[3]{{{a}}} \\times \\sqrt[3]{{{b}}}"

            steps = [
                f"\\sqrt[3]{{{a}}} \\times \\sqrt[3]{{{b}}} = \\sqrt[3]{{{a} \\times {b}}}",
                f"= \\sqrt[3]{{{product}}}",
                f"= {solution}"
            ]

        elif problem_type == 'simplify_large':
            # Larger number with perfect cube factor
            perfect_root = random.choice([2, 3, 4])
            perfect = perfect_root ** 3
            other = random.choice([2, 3, 5])
            n = perfect * other

            latex = f"\\sqrt[3]{{{n}}}"
            solution = f"{perfect_root}\\sqrt[3]{{{other}}}"

            steps = [
                f"{n} = {perfect} \\times {other}",
                f"= {perfect_root}^3 \\times {other}",
                f"\\sqrt[3]{{{n}}} = {perfect_root}\\sqrt[3]{{{other}}}"
            ]

        else:  # mixed
            # Expression with cube root
            root = random.choice([2, 3])
            n = root ** 3
            multiplier = random.randint(2, 5)

            latex = f"{multiplier} \\times \\sqrt[3]{{{n}}}"
            result = multiplier * root
            solution = str(result)

            steps = [
                f"\\sqrt[3]{{{n}}} = {root}",
                f"{multiplier} \\times {root} = {result}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SimplifyingCubeRootsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
