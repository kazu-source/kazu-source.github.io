"""
Powers of Whole Numbers Generator - Grade 6 Unit 4
Generates problems evaluating powers of whole numbers
Example: Evaluate 3^4
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PowersOfWholeNumbersGenerator:
    """Generates powers of whole numbers problems."""

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
        """Generate easy problems: small bases and exponents."""
        base = random.randint(2, 5)
        exponent = random.randint(2, 3)
        result = base ** exponent

        latex = f"\\text{{Evaluate: }} {base}^{{{exponent}}}"
        solution = str(result)

        expansion = " \\times ".join([str(base)] * exponent)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{base}^{{{exponent}}} = {expansion} = {result}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: larger bases or exponents."""
        if random.choice([True, False]):
            base = random.randint(6, 10)
            exponent = random.randint(2, 3)
        else:
            base = random.randint(2, 5)
            exponent = random.randint(4, 5)

        result = base ** exponent

        latex = f"\\text{{Evaluate: }} {base}^{{{exponent}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{base}^{{{exponent}}} = {result}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: powers with exponent 1 or special cases."""
        choice = random.randint(1, 3)

        if choice == 1:
            # Exponent of 1
            base = random.randint(5, 50)
            latex = f"\\text{{Evaluate: }} {base}^{{1}}"
            solution = str(base)
            steps = [f"{base}^{{1}} = {base}"]
        elif choice == 2:
            # Base of 10
            exponent = random.randint(2, 4)
            result = 10 ** exponent
            latex = f"\\text{{Evaluate: }} 10^{{{exponent}}}"
            solution = str(result)
            steps = [f"10^{{{exponent}}} = {result}"]
        else:
            # Larger computation
            base = random.randint(11, 15)
            exponent = 2
            result = base ** exponent
            latex = f"\\text{{Evaluate: }} {base}^{{{exponent}}}"
            solution = str(result)
            steps = [f"{base}^{{{exponent}}} = {base} \\times {base} = {result}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing or adding powers."""
        if random.choice([True, False]):
            # Add two powers
            base1 = random.randint(2, 4)
            exp1 = 2
            val1 = base1 ** exp1

            base2 = random.randint(2, 4)
            exp2 = 2
            val2 = base2 ** exp2

            result = val1 + val2

            latex = f"\\text{{Evaluate: }} {base1}^{{{exp1}}} + {base2}^{{{exp2}}}"
            solution = str(result)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"{base1}^{{{exp1}}} = {val1}",
                    f"{base2}^{{{exp2}}} = {val2}",
                    f"{val1} + {val2} = {result}"
                ],
                difficulty='challenge'
            )
        else:
            # Multiply by a power
            multiplier = random.randint(2, 5)
            base = random.randint(2, 5)
            exponent = 2
            power_val = base ** exponent
            result = multiplier * power_val

            latex = f"\\text{{Evaluate: }} {multiplier} \\times {base}^{{{exponent}}}"
            solution = str(result)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"{base}^{{{exponent}}} = {power_val}",
                    f"{multiplier} \\times {power_val} = {result}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = PowersOfWholeNumbersGenerator()

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
