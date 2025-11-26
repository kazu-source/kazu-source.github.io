"""
Scientific Notation Intro Generator - Grade 8 Unit 1
Generates problems introducing scientific notation
Example: Write 3400 in scientific notation: 3.4 × 10³
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ScientificNotationIntroGenerator:
    """Generates scientific notation introduction problems."""

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
        """Generate easy problems: convert simple numbers to scientific notation."""
        # Numbers like 2000, 3000, etc.
        coefficient = random.randint(2, 9)
        exponent = random.randint(2, 4)

        number = coefficient * (10 ** exponent)

        latex = f"\\text{{Write in scientific notation: }} {number}"
        solution = f"{coefficient} \\times 10^{{{exponent}}}"
        steps = [
            f"{number} = {coefficient} \\times {10**exponent}",
            f"{coefficient} \\times 10^{{{exponent}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: convert numbers with decimals or from scientific notation."""
        problem_type = random.choice(['to_scientific', 'from_scientific'])

        if problem_type == 'to_scientific':
            # Numbers like 3450, 6780, etc.
            first_digit = random.randint(1, 9)
            second_digit = random.randint(0, 9)
            third_digit = random.choice([0, 5])
            exponent = random.randint(2, 5)

            coefficient = first_digit + second_digit / 10 + third_digit / 100
            if third_digit == 0:
                coefficient = first_digit + second_digit / 10

            number = int(coefficient * (10 ** exponent))

            if third_digit == 0 and second_digit == 0:
                solution = f"{first_digit} \\times 10^{{{exponent}}}"
            elif third_digit == 0:
                solution = f"{first_digit}.{second_digit} \\times 10^{{{exponent}}}"
            else:
                solution = f"{coefficient} \\times 10^{{{exponent}}}"

            latex = f"\\text{{Write in scientific notation: }} {number}"
            steps = [f"{number} = {solution}"]

        else:  # from_scientific
            coefficient = random.randint(1, 9) + random.choice([0, 0.5])
            exponent = random.randint(2, 4)

            number = int(coefficient * (10 ** exponent))

            latex = f"\\text{{Write in standard form: }} {coefficient} \\times 10^{{{exponent}}}"
            solution = str(number)
            steps = [
                f"{coefficient} \\times 10^{{{exponent}}} = {coefficient} \\times {10**exponent}",
                f"{number}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: small numbers (decimals) in scientific notation."""
        problem_type = random.choice(['small_to_sci', 'small_from_sci'])

        if problem_type == 'small_to_sci':
            coefficient = random.randint(1, 9) + random.randint(0, 9) / 10
            exponent = random.randint(2, 4)

            number = coefficient / (10 ** exponent)

            latex = f"\\text{{Write in scientific notation: }} {number}"
            solution = f"{coefficient} \\times 10^{{-{exponent}}}"
            steps = [f"{number} = {coefficient} \\times 10^{{-{exponent}}}"]

        else:  # small_from_sci
            coefficient = random.randint(1, 9) + random.choice([0, 0.5])
            exponent = random.randint(2, 3)

            number = coefficient / (10 ** exponent)

            latex = f"\\text{{Write in standard form: }} {coefficient} \\times 10^{{-{exponent}}}"
            solution = str(number)
            steps = [
                f"{coefficient} \\times 10^{{-{exponent}}} = {coefficient} \\times \\frac{{1}}{{10^{{{exponent}}}}}",
                f"{number}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing and ordering numbers in scientific notation."""
        problem_type = random.choice(['compare', 'order', 'convert_complex'])

        if problem_type == 'compare':
            coef1 = random.randint(2, 7)
            coef2 = random.randint(2, 7)
            exp1 = random.randint(3, 6)
            exp2 = random.randint(3, 6)

            num1_value = coef1 * (10 ** exp1)
            num2_value = coef2 * (10 ** exp2)

            latex = f"\\text{{Which is greater: }} {coef1} \\times 10^{{{exp1}}} \\text{{ or }} {coef2} \\times 10^{{{exp2}}}?"

            if num1_value > num2_value:
                solution = f"{coef1} \\times 10^{{{exp1}}}"
                comparison = ">"
            elif num1_value < num2_value:
                solution = f"{coef2} \\times 10^{{{exp2}}}"
                comparison = "<"
            else:
                solution = "\\text{Equal}"
                comparison = "="

            steps = [
                f"{coef1} \\times 10^{{{exp1}}} = {num1_value}",
                f"{coef2} \\times 10^{{{exp2}}} = {num2_value}",
                f"{num1_value} {comparison} {num2_value}"
            ]

        elif problem_type == 'order':
            numbers = []
            for _ in range(3):
                coef = random.randint(1, 9)
                exp = random.randint(2, 5)
                numbers.append((coef, exp, coef * (10 ** exp)))

            # Sort by value
            numbers.sort(key=lambda x: x[2])

            latex = f"\\text{{Order from least to greatest: }} {numbers[0][0]} \\times 10^{{{numbers[0][1]}}}, {numbers[1][0]} \\times 10^{{{numbers[1][1]}}}, {numbers[2][0]} \\times 10^{{{numbers[2][1]}}}"
            solution = f"{numbers[0][0]} \\times 10^{{{numbers[0][1]}}} < {numbers[1][0]} \\times 10^{{{numbers[1][1]}}} < {numbers[2][0]} \\times 10^{{{numbers[2][1]}}}"
            steps = [
                f"{numbers[0][0]} \\times 10^{{{numbers[0][1]}}} = {numbers[0][2]}",
                f"{numbers[1][0]} \\times 10^{{{numbers[1][1]}}} = {numbers[1][2]}",
                f"{numbers[2][0]} \\times 10^{{{numbers[2][1]}}} = {numbers[2][2]}"
            ]

        else:  # convert_complex
            first_digit = random.randint(1, 9)
            second_digit = random.randint(1, 9)
            third_digit = random.randint(1, 9)
            exponent = random.randint(4, 6)

            coefficient = first_digit + second_digit / 10 + third_digit / 100
            number = int(coefficient * (10 ** exponent))

            latex = f"\\text{{Write in scientific notation: }} {number}"
            solution = f"{coefficient} \\times 10^{{{exponent}}}"
            steps = [f"{number} = {coefficient} \\times 10^{{{exponent}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ScientificNotationIntroGenerator()

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
