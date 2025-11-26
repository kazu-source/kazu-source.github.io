"""
Working with Powers of 10 Generator - Grade 8 Unit 1
Generates problems with powers of 10
Example: 10³ = 1000, 10⁻² = 0.01
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class WorkingWithPowersOf10Generator:
    """Generates working with powers of 10 problems."""

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
        """Generate easy problems: evaluate positive powers of 10."""
        exponent = random.randint(1, 5)

        result = 10 ** exponent

        latex = f"10^{{{exponent}}}"
        solution = str(result)
        steps = [f"10^{{{exponent}}} = {result}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: negative powers of 10 and multiplication."""
        problem_type = random.choice(['negative', 'multiply'])

        if problem_type == 'negative':
            exponent = random.randint(1, 4)

            result = 10 ** (-exponent)

            latex = f"10^{{-{exponent}}}"
            solution = str(result)
            steps = [
                f"10^{{-{exponent}}} = \\frac{{1}}{{10^{{{exponent}}}}}",
                f"\\frac{{1}}{{{10**exponent}}} = {result}"
            ]

        else:  # multiply
            number = random.choice([2, 3, 4, 5, 7, 8, 9])
            exponent = random.randint(2, 4)

            result = number * (10 ** exponent)

            latex = f"{number} \\times 10^{{{exponent}}}"
            solution = str(result)
            steps = [
                f"10^{{{exponent}}} = {10**exponent}",
                f"{number} \\times {10**exponent} = {result}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: operations with powers of 10."""
        problem_type = random.choice(['product', 'quotient', 'decimal_multiply'])

        if problem_type == 'product':
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 4)

            result_exp = exp1 + exp2

            latex = f"10^{{{exp1}}} \\times 10^{{{exp2}}}"
            solution = f"10^{{{result_exp}}}"
            steps = [
                f"10^{{{exp1}}} \\times 10^{{{exp2}}} = 10^{{{exp1} + {exp2}}}",
                f"10^{{{result_exp}}}"
            ]

        elif problem_type == 'quotient':
            exp1 = random.randint(5, 8)
            exp2 = random.randint(2, 4)

            result_exp = exp1 - exp2

            latex = f"\\frac{{10^{{{exp1}}}}}{{10^{{{exp2}}}}}"
            solution = f"10^{{{result_exp}}}"
            steps = [
                f"\\frac{{10^{{{exp1}}}}}{{10^{{{exp2}}}}} = 10^{{{exp1} - {exp2}}}",
                f"10^{{{result_exp}}}"
            ]

        else:  # decimal_multiply
            number = random.choice([1.5, 2.5, 3.5, 4.5, 5.5])
            exponent = random.randint(2, 3)

            result = number * (10 ** exponent)

            latex = f"{number} \\times 10^{{{exponent}}}"
            solution = str(result).rstrip('0').rstrip('.')
            steps = [
                f"10^{{{exponent}}} = {10**exponent}",
                f"{number} \\times {10**exponent} = {result}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex expressions with powers of 10."""
        problem_type = random.choice(['mixed_ops', 'negative_multiply', 'divide'])

        if problem_type == 'mixed_ops':
            exp1 = random.randint(2, 4)
            exp2 = random.randint(1, 3)
            exp3 = random.randint(2, 3)

            # 10^a × 10^(-b) / 10^c
            numerator_exp = exp1 - exp2
            result_exp = numerator_exp - exp3

            latex = f"\\frac{{10^{{{exp1}}} \\times 10^{{-{exp2}}}}}{{10^{{{exp3}}}}}"
            solution = f"10^{{{result_exp}}}"
            steps = [
                f"\\text{{Numerator: }} 10^{{{exp1}}} \\times 10^{{-{exp2}}} = 10^{{{numerator_exp}}}",
                f"\\frac{{10^{{{numerator_exp}}}}}{{10^{{{exp3}}}}} = 10^{{{result_exp}}}"
            ]

        elif problem_type == 'negative_multiply':
            number = random.choice([2, 3, 4, 5])
            exponent = random.randint(2, 4)

            result = number * (10 ** (-exponent))

            latex = f"{number} \\times 10^{{-{exponent}}}"
            solution = str(result)
            steps = [
                f"10^{{-{exponent}}} = {10**(-exponent)}",
                f"{number} \\times {10**(-exponent)} = {result}"
            ]

        else:  # divide
            number = random.choice([200, 300, 400, 500, 600, 700, 800, 900])
            exponent = random.randint(1, 2)

            result = number / (10 ** exponent)

            latex = f"\\frac{{{number}}}{{10^{{{exponent}}}}}"
            solution = str(int(result)) if result == int(result) else str(result)
            steps = [
                f"10^{{{exponent}}} = {10**exponent}",
                f"\\frac{{{number}}}{{{10**exponent}}} = {solution}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = WorkingWithPowersOf10Generator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}\n")

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
