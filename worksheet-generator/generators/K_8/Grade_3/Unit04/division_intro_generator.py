"""
Division Introduction Generator - Grade 3 Unit 4
Generates problems focused on understanding division as sharing or grouping
Example: 12 ÷ 3 = 4 (12 items shared into 3 groups)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DivisionIntroGenerator:
    """Generates division introduction problems focusing on sharing and grouping."""

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
        """Generate easy problems: small numbers (dividends up to 20)."""
        divisor = random.randint(2, 5)
        quotient = random.randint(2, 4)
        dividend = divisor * quotient

        # Simple division problem
        latex = f"{dividend} \\div {divisor}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: larger dividends (up to 50) with sharing context."""
        divisor = random.randint(2, 5)
        quotient = random.randint(3, 10)
        dividend = divisor * quotient

        contexts = [
            (f"Share {dividend} items equally among {divisor} groups", "sharing"),
            (f"Divide {dividend} objects into {divisor} equal groups", "grouping"),
            (f"Split {dividend} items into {divisor} equal parts", "sharing")
        ]

        context, context_type = random.choice(contexts)
        latex = f"\\text{{{context}. How many in each group?}}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with real-world context."""
        divisor = random.randint(2, 6)
        quotient = random.randint(4, 10)
        dividend = divisor * quotient

        contexts = [
            f"Sarah has {dividend} cookies. She wants to share them equally among {divisor} friends",
            f"A teacher has {dividend} pencils to divide equally among {divisor} students",
            f"There are {dividend} apples to be packed into {divisor} boxes with the same number in each",
            f"A farmer picked {dividend} flowers and wants to make {divisor} bouquets with the same number of flowers"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}. How many does each get?}}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step or with remainders."""
        problem_type = random.choice(['multi_step', 'remainder'])

        if problem_type == 'multi_step':
            # Two-step problem
            divisor1 = random.randint(2, 4)
            quotient1 = random.randint(3, 6)
            dividend1 = divisor1 * quotient1

            divisor2 = random.randint(2, 3)
            quotient2 = quotient1 // divisor2

            contexts = [
                f"{dividend1} candies are shared among {divisor1} children. Each child then shares their candies with {divisor2} friends",
                f"A baker made {dividend1} cookies and packed them into {divisor1} boxes. Each box is then divided into {divisor2} smaller packages"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. How many in each final group?}}"
            solution = str(quotient2)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"{dividend1} \\div {divisor1} = {quotient1}", f"{quotient1} \\div {divisor2} = {quotient2}"],
                difficulty='challenge'
            )
        else:
            # Simple remainder problem
            divisor = random.randint(2, 5)
            quotient = random.randint(3, 8)
            remainder = random.randint(1, divisor - 1)
            dividend = divisor * quotient + remainder

            contexts = [
                f"{dividend} items divided into groups of {divisor}",
                f"Share {dividend} objects among {divisor} groups"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. How many in each group and how many left over?}}"
            solution = f"{quotient} R{remainder}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"{dividend} \\div {divisor} = {quotient} \\text{{ R}} {remainder}"],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = DivisionIntroGenerator()

    print("DIVISION INTRODUCTION GENERATOR TEST\n")
    print("=" * 50)

    print("\nEasy (Simple division):")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium (Sharing/grouping context):")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard (Word problems):")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge (Multi-step or remainders):")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
