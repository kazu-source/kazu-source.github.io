"""
Divide by 3 or 6 Generator - Grade 3 Unit 4
Generates division problems focusing on dividing by 3 or 6
Builds fluency with these important division facts
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DivideBy3Or6Generator:
    """Generates division problems with divisors 3 or 6."""

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
        """Generate easy problems: small dividends (up to 30)."""
        divisor = random.choice([3, 6])

        if divisor == 3:
            quotient = random.randint(1, 10)
        else:  # divisor == 6
            quotient = random.randint(1, 5)

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
        """Generate medium problems: larger dividends (up to 60)."""
        divisor = random.choice([3, 6])

        if divisor == 3:
            quotient = random.randint(5, 20)
        else:  # divisor == 6
            quotient = random.randint(3, 10)

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
        divisor = random.choice([3, 6])

        if divisor == 3:
            quotient = random.randint(4, 12)
        else:  # divisor == 6
            quotient = random.randint(3, 10)

        dividend = divisor * quotient

        if divisor == 3:
            contexts = [
                f"A triangle has 3 sides. If the perimeter is {dividend} cm and all sides are equal, how long is each side?",
                f"There are {dividend} students who need to form groups of {divisor}. How many groups can they make?",
                f"A pizza is cut into {dividend} slices. {divisor} friends share it equally. How many slices does each get?",
                f"The library has {dividend} books to place on {divisor} shelves equally. How many books per shelf?"
            ]
        else:  # divisor == 6
            contexts = [
                f"A carton holds 6 eggs. How many cartons are needed for {dividend} eggs?",
                f"There are {dividend} muffins to pack into boxes of {divisor}. How many boxes are needed?",
                f"A hexagon has 6 sides. If the perimeter is {dividend} inches and all sides are equal, how long is each side?",
                f"The bakery made {dividend} cupcakes and packs them {divisor} to a box. How many boxes do they fill?"
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
        """Generate challenge problems: multi-step, relationship between 3 and 6, or remainders."""
        problem_type = random.choice(['multi_step', 'relationship', 'remainder'])

        if problem_type == 'multi_step':
            # Multiply then divide or divide different numbers
            divisor = random.choice([3, 6])
            quotient1 = random.randint(3, 8)
            dividend1 = divisor * quotient1

            operation = random.choice(['subtract', 'add'])

            if operation == 'subtract':
                subtract_amount = random.randint(divisor, dividend1 - divisor)
                # Make sure result is divisible by divisor
                remainder_check = (dividend1 - subtract_amount) % divisor
                subtract_amount += remainder_check
                result = (dividend1 - subtract_amount) // divisor

                contexts = [
                    f"There were {dividend1} apples. After eating {subtract_amount}, the rest are divided into groups of {divisor}",
                    f"A store had {dividend1} toys. {subtract_amount} were sold. The remaining toys are packed {divisor} per box"
                ]

                context = random.choice(contexts)
                latex = f"\\text{{{context}. How many groups/boxes?}}"
                solution = str(result)

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[f"{dividend1} - {subtract_amount} = {dividend1 - subtract_amount}", f"{dividend1 - subtract_amount} \\div {divisor} = {result}"],
                    difficulty='challenge'
                )
            else:
                # Add then divide
                num1 = divisor * random.randint(2, 5)
                num2 = divisor * random.randint(2, 5)
                total = num1 + num2
                result = total // divisor

                contexts = [
                    f"Box A has {num1} items and Box B has {num2} items. All items are divided into groups of {divisor}",
                    f"Monday's collection: {num1} cans. Tuesday's collection: {num2} cans. All cans packed {divisor} per bag"
                ]

                context = random.choice(contexts)
                latex = f"\\text{{{context}. How many groups/bags total?}}"
                solution = str(result)

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[f"{num1} + {num2} = {total}", f"{total} \\div {divisor} = {result}"],
                    difficulty='challenge'
                )

        elif problem_type == 'relationship':
            # Explore relationship: dividing by 6 vs dividing by 3
            quotient_by_6 = random.randint(3, 8)
            dividend = 6 * quotient_by_6
            quotient_by_3 = dividend // 3

            latex = f"\\text{{If {dividend} \\div 6 = {quotient_by_6}, what is {dividend} \\div 3?}}"
            solution = str(quotient_by_3)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"{dividend} \\div 3 = {quotient_by_3}", f"\\text{{Note: {quotient_by_3} = 2 \\times {quotient_by_6}}}"],
                difficulty='challenge'
            )

        else:  # remainder
            divisor = random.choice([3, 6])
            quotient = random.randint(4, 10)
            remainder = random.randint(1, divisor - 1)
            dividend = divisor * quotient + remainder

            contexts = [
                f"{dividend} pencils shared among {divisor} students",
                f"{dividend} cookies divided into groups of {divisor}",
                f"{dividend} toys packed {divisor} per box"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. How many each and how many left over?}}"
            solution = f"{quotient} R{remainder}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"{dividend} \\div {divisor} = {quotient} \\text{{ R}} {remainder}"],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = DivideBy3Or6Generator()

    print("DIVIDE BY 3 OR 6 GENERATOR TEST\n")
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

    print("\nChallenge (Multi-step, relationships, or remainders):")
    for problem in generator.generate_worksheet('challenge', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print(f"  Steps: {problem.steps}\n")


if __name__ == '__main__':
    main()
