"""
Comparing Fractions Generator - Grade 3 Unit 6
Generates problems comparing fractions with the same denominator
Example: Which is greater: 2/5 or 3/5?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingFractionsGenerator:
    """Generates comparing fractions problems (same denominator)."""

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
        """Generate easy problems: thirds, fourths (not halves to ensure 2 different numerators)."""
        denominator = random.choice([3, 4])  # Avoid 2 since it only has one numerator

        # Generate two different numerators
        available = list(range(1, denominator))
        num1, num2 = random.sample(available, 2)

        latex = f"\\text{{Compare: }} \\frac{{{num1}}}{{{denominator}}} \\quad \\text{{and}} \\quad \\frac{{{num2}}}{{{denominator}}}"

        if num1 > num2:
            solution = f"\\frac{{{num1}}}{{{denominator}}} > \\frac{{{num2}}}{{{denominator}}}"
            comparison = ">"
        else:
            solution = f"\\frac{{{num1}}}{{{denominator}}} < \\frac{{{num2}}}{{{denominator}}}"
            comparison = "<"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Same denominator: compare numerators: {num1} {comparison} {num2}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: fifths, sixths, eighths."""
        denominator = random.choice([5, 6, 8])

        # Generate two different numerators
        available = list(range(1, denominator))
        num1, num2 = random.sample(available, 2)

        latex = f"\\text{{Compare: }} \\frac{{{num1}}}{{{denominator}}} \\quad \\text{{and}} \\quad \\frac{{{num2}}}{{{denominator}}}"

        if num1 > num2:
            solution = f"\\frac{{{num1}}}{{{denominator}}} > \\frac{{{num2}}}{{{denominator}}}"
            comparison = ">"
        else:
            solution = f"\\frac{{{num1}}}{{{denominator}}} < \\frac{{{num2}}}{{{denominator}}}"
            comparison = "<"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Same denominator: compare numerators: {num1} {comparison} {num2}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with fraction comparisons."""
        denominator = random.choice([3, 4, 5, 6, 8])

        # Generate two different numerators
        available = list(range(1, denominator))
        num1, num2 = random.sample(available, 2)

        contexts = [
            f"Sarah ate \\frac{{{num1}}}{{{denominator}}} of a pizza and Tom ate \\frac{{{num2}}}{{{denominator}}} of the same pizza. Who ate more?",
            f"John walked \\frac{{{num1}}}{{{denominator}}} of a mile and Maria walked \\frac{{{num2}}}{{{denominator}}} of a mile. Who walked farther?",
            f"A recipe needs \\frac{{{num1}}}{{{denominator}}} cup of sugar. Another recipe needs \\frac{{{num2}}}{{{denominator}}} cup. Which needs more sugar?",
            f"One book is \\frac{{{num1}}}{{{denominator}}} complete and another is \\frac{{{num2}}}{{{denominator}}} complete. Which book is more complete?"
        ]

        context = random.choice(contexts)

        if num1 > num2:
            if "Sarah" in context:
                answer = "Sarah"
            elif "John" in context:
                answer = "John"
            elif "recipe" in context:
                answer = "First recipe"
            else:
                answer = "First book"
            comparison = ">"
            solution = f"{answer} \\text{{ (}} \\frac{{{num1}}}{{{denominator}}} > \\frac{{{num2}}}{{{denominator}}} \\text{{)}}"
        else:
            if "Sarah" in context:
                answer = "Tom"
            elif "John" in context:
                answer = "Maria"
            elif "recipe" in context:
                answer = "Second recipe"
            else:
                answer = "Second book"
            comparison = "<"
            solution = f"{answer} \\text{{ (}} \\frac{{{num2}}}{{{denominator}}} > \\frac{{{num1}}}{{{denominator}}} \\text{{)}}"

        latex = f"\\text{{{context}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Compare: {num1} {comparison} {num2}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: ordering multiple fractions."""
        denominator = random.choice([6, 8, 10])

        # Generate 3 different numerators
        nums = random.sample(range(1, denominator), 3)

        latex = f"\\text{{Order from least to greatest: }} \\frac{{{nums[0]}}}{{{denominator}}}, \\frac{{{nums[1]}}}{{{denominator}}}, \\frac{{{nums[2]}}}{{{denominator}}}"

        sorted_nums = sorted(nums)
        solution = f"\\frac{{{sorted_nums[0]}}}{{{denominator}}} < \\frac{{{sorted_nums[1]}}}{{{denominator}}} < \\frac{{{sorted_nums[2]}}}{{{denominator}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Same denominator: compare numerators: {sorted_nums[0]} < {sorted_nums[1]} < {sorted_nums[2]}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ComparingFractionsGenerator()

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
