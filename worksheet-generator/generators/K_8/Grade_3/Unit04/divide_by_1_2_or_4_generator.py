"""
Divide by 1, 2, or 4 Generator - Grade 3 Unit 4
Generates division problems focusing on dividing by 1, 2, or 4
Builds fluency with basic division facts
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DivideBy1_2_Or4Generator:
    """Generates division problems with divisors 1, 2, or 4."""

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
        """Generate easy problems: small dividends (up to 25)."""
        divisor = random.choice([1, 2, 4])

        if divisor == 1:
            quotient = random.randint(1, 25)
        elif divisor == 2:
            quotient = random.randint(1, 12)
        else:  # divisor == 4
            quotient = random.randint(1, 6)

        dividend = divisor * quotient

        latex = f"{dividend} \\div {divisor}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: larger dividends (up to 50)."""
        divisor = random.choice([1, 2, 4])

        if divisor == 1:
            quotient = random.randint(10, 50)
        elif divisor == 2:
            quotient = random.randint(5, 25)
        else:  # divisor == 4
            quotient = random.randint(3, 12)

        dividend = divisor * quotient

        latex = f"{dividend} \\div {divisor}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with context."""
        divisor = random.choice([2, 4])  # Skip 1 for more interesting word problems

        if divisor == 2:
            quotient = random.randint(5, 20)
        else:  # divisor == 4
            quotient = random.randint(4, 12)

        dividend = divisor * quotient

        if divisor == 2:
            contexts = [
                f"A pair of shoes costs ${dividend}. How much does one shoe cost?",
                f"{dividend} students need to form {divisor} equal teams. How many on each team?",
                f"Mom bought {dividend} cookies and wants to share them equally between {divisor} children. How many does each child get?",
                f"There are {dividend} apples in {divisor} baskets with the same number in each. How many apples per basket?"
            ]
        else:  # divisor == 4
            contexts = [
                f"A package of {dividend} pencils is divided equally among {divisor} students. How many does each get?",
                f"There are {dividend} wheels on some cars. If each car has {divisor} wheels, how many cars are there?",
                f"{dividend} cupcakes are packed into boxes of {divisor}. How many boxes are needed?",
                f"A rectangle has a perimeter of {dividend} cm and {divisor} equal sides. What is the length of each side?"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(quotient)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{dividend} \\div {divisor} = {quotient}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step or missing number problems."""
        problem_type = random.choice(['multi_step', 'missing_number'])

        if problem_type == 'multi_step':
            # Two operations: first multiply, then divide
            factor1 = random.choice([2, 4])
            factor2 = random.randint(2, 6)
            product = factor1 * factor2

            divisor = random.choice([2, 4])
            quotient = product // divisor

            contexts = [
                f"John has {factor1} packs of {factor2} stickers. He shares them equally among {divisor} friends",
                f"A store has {factor1} boxes with {factor2} toys in each. They divide all toys into {divisor} equal groups",
                f"There are {factor1} rows of {factor2} chairs. The chairs are rearranged into {divisor} equal sections"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. How many in each group?}}"
            solution = str(quotient)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"{factor1} \\times {factor2} = {product}", f"{product} \\div {divisor} = {quotient}"],
                difficulty='challenge'
            )
        else:
            # Missing dividend: ? ÷ divisor = quotient
            divisor = random.choice([2, 4])
            quotient = random.randint(4, 12)
            dividend = divisor * quotient

            latex = f"? \\div {divisor} = {quotient}"
            solution = str(dividend)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"? = {quotient} \\times {divisor}", f"? = {dividend}"],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = DivideBy1_2_Or4Generator()

    print("DIVIDE BY 1, 2, OR 4 GENERATOR TEST\n")
    print("=" * 50)

    print("\nEasy (Small dividends):")
    for problem in generator.generate_worksheet('easy', 4):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium (Larger dividends):")
    for problem in generator.generate_worksheet('medium', 4):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nHard (Word problems):")
    for problem in generator.generate_worksheet('hard', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge (Multi-step or missing numbers):")
    for problem in generator.generate_worksheet('challenge', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print(f"  Steps: {problem.steps}\n")


if __name__ == '__main__':
    main()
