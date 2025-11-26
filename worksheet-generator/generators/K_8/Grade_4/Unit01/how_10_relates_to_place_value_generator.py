"""
How 10 Relates to Place Value Generator - Grade 4 Unit 1
Generates problems showing the relationship between place values and powers of 10
Example: 500 is 10 times as much as what number?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class How10RelatesToPlaceValueGenerator:
    """Generates problems about how 10 relates to place value."""

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
        """Generate easy problems: 10 times a 1-digit number."""
        base = random.randint(1, 9)
        result = base * 10

        latex = f"{base} \\times 10 = ?"
        solution = str(result)

        steps = [
            f"{base} \\times 10 = {result}",
            f"\\text{{When multiplying by 10, shift one place left}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: finding what number times 10 gives result."""
        base = random.randint(2, 99)
        result = base * 10

        problem_type = random.choice(['forward', 'backward'])

        if problem_type == 'forward':
            latex = f"{base} \\times 10 = ?"
            solution = str(result)
            steps = [
                f"{base} \\times 10 = {result}"
            ]
        else:
            latex = f"{result:,} \\text{{ is 10 times as much as what number?}}"
            solution = str(base)
            steps = [
                f"{result:,} \\div 10 = {base}",
                f"\\text{{When dividing by 10, shift one place right}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: comparing place values."""
        base = random.randint(100, 999)

        problem_type = random.choice(['ten_times', 'one_tenth'])

        if problem_type == 'ten_times':
            result = base * 10
            latex = f"\\text{{What is 10 times }} {base:,}?"
            solution = f"{result:,}"
            steps = [
                f"{base:,} \\times 10 = {result:,}",
                f"\\text{{Shift all digits one place to the left}}"
            ]
        else:
            result = base // 10
            latex = f"\\text{{What is }} \\frac{{1}}{{10}} \\text{{ of }} {base:,}?"
            solution = str(result)
            steps = [
                f"{base:,} \\div 10 = {result}",
                f"\\text{{Shift all digits one place to the right}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step or comparison problems."""
        base = random.randint(10, 99)

        problem_type = random.choice(['100_times', 'comparison'])

        if problem_type == '100_times':
            result = base * 100
            latex = f"\\text{{What is 100 times }} {base}?"
            solution = f"{result:,}"
            steps = [
                f"{base} \\times 100 = {base} \\times 10 \\times 10",
                f"= {base * 10} \\times 10",
                f"= {result:,}"
            ]
        else:
            # Comparison problem
            number = base * 10
            latex = f"\\text{{The digit 4 in }} {base * 10} \\text{{ is how many times the value of 4 in }} {base}?"
            # This is a bit abstract, so let's make it simpler
            latex = f"\\text{{How many times greater is }} {base * 10} \\text{{ than }} {base}?"
            solution = "10"
            steps = [
                f"{base * 10} \\div {base} = 10",
                f"\\text{{A digit in one place is 10 times the same digit one place to the right}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = How10RelatesToPlaceValueGenerator()

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
