"""
Divide by 7, 8, or 9 Generator - Grade 3 Unit 4
Generates division problems focusing on dividing by 7, 8, or 9
Builds fluency with more challenging division facts
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DivideBy7_8_Or9Generator:
    """Generates division problems with divisors 7, 8, or 9."""

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
        """Generate easy problems: small dividends (up to 40)."""
        divisor = random.choice([7, 8, 9])

        if divisor == 7:
            quotient = random.randint(1, 5)
        elif divisor == 8:
            quotient = random.randint(1, 5)
        else:  # divisor == 9
            quotient = random.randint(1, 4)

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
        """Generate medium problems: larger dividends (up to 90)."""
        divisor = random.choice([7, 8, 9])

        if divisor == 7:
            quotient = random.randint(3, 12)
        elif divisor == 8:
            quotient = random.randint(3, 11)
        else:  # divisor == 9
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
        divisor = random.choice([7, 8, 9])

        if divisor == 7:
            quotient = random.randint(3, 10)
        elif divisor == 8:
            quotient = random.randint(3, 9)
        else:  # divisor == 9
            quotient = random.randint(3, 9)

        dividend = divisor * quotient

        if divisor == 7:
            contexts = [
                f"There are 7 days in a week. How many weeks are in {dividend} days?",
                f"A heptagon has 7 sides. If the perimeter is {dividend} cm and all sides are equal, how long is each side?",
                f"The class has {dividend} students sitting at tables of {divisor}. How many tables are there?",
                f"A garden has {dividend} flowers planted in {divisor} rows. How many flowers per row?"
            ]
        elif divisor == 8:
            contexts = [
                f"An octopus has 8 legs. How many octopuses have {dividend} legs total?",
                f"Crayons come in boxes of {divisor}. How many boxes are needed for {dividend} crayons?",
                f"A spider has 8 legs. If there are {dividend} legs total, how many spiders are there?",
                f"The school bought {dividend} markers packed {divisor} per pack. How many packs did they buy?"
            ]
        else:  # divisor == 9
            contexts = [
                f"Baseball has 9 players per team. How many teams can be formed from {dividend} players?",
                f"A nonagon has 9 sides. If the perimeter is {dividend} inches and all sides are equal, how long is each side?",
                f"The cafeteria has {dividend} students seated at tables of {divisor}. How many tables are full?",
                f"There are {dividend} pencils to distribute equally to {divisor} classrooms. How many per classroom?"
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
        """Generate challenge problems: multi-step, mixed operations, or remainders."""
        problem_type = random.choice(['multi_step', 'mixed_operations', 'remainder', 'comparison'])

        if problem_type == 'multi_step':
            # Two-step division or multiply then divide
            divisor1 = random.choice([7, 8, 9])
            quotient1 = random.randint(3, 8)
            dividend1 = divisor1 * quotient1

            operation = random.choice(['add_divide', 'subtract_divide'])

            if operation == 'add_divide':
                extra = divisor1 * random.randint(1, 3)
                total = dividend1 + extra
                final_result = total // divisor1

                contexts = [
                    f"A store had {dividend1} items. They received {extra} more. All items are packed {divisor1} per box",
                    f"Monday: {dividend1} students. Tuesday: {extra} more students join. All divided into teams of {divisor1}"
                ]

                context = random.choice(contexts)
                latex = f"\\text{{{context}. How many boxes/teams?}}"
                solution = str(final_result)

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[f"{dividend1} + {extra} = {total}", f"{total} \\div {divisor1} = {final_result}"],
                    difficulty='challenge'
                )
            else:
                # Subtract then divide
                total = divisor1 * random.randint(5, 10)
                subtract = divisor1 * random.randint(1, 3)
                result = (total - subtract) // divisor1

                contexts = [
                    f"There were {total} cookies. After eating {subtract}, the rest are shared among {divisor1} children",
                    f"A library had {total} books. {subtract} were checked out. The rest are divided among {divisor1} shelves"
                ]

                context = random.choice(contexts)
                latex = f"\\text{{{context}. How many each?}}"
                solution = str(result)

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[f"{total} - {subtract} = {total - subtract}", f"{total - subtract} \\div {divisor1} = {result}"],
                    difficulty='challenge'
                )

        elif problem_type == 'mixed_operations':
            # Multiply two numbers, then divide
            factor1 = random.randint(2, 5)
            factor2 = random.randint(3, 6)
            product = factor1 * factor2

            divisor = random.choice([7, 8, 9])
            # Adjust product to be divisible by divisor
            quotient = max(2, product // divisor)
            product = divisor * quotient

            contexts = [
                f"A classroom has {factor1} rows with {product // factor1} chairs each. The chairs are rearranged into {divisor} equal sections",
                f"There are {factor1} boxes with {product // factor1} items each. All items divided among {divisor} students"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. How many in each section/per student?}}"
            solution = str(quotient)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"{factor1} \\times {product // factor1} = {product}", f"{product} \\div {divisor} = {quotient}"],
                difficulty='challenge'
            )

        elif problem_type == 'comparison':
            # Compare two division problems
            divisor = random.choice([7, 8, 9])
            quotient1 = random.randint(4, 8)
            quotient2 = quotient1 + random.randint(2, 4)
            dividend1 = divisor * quotient1
            dividend2 = divisor * quotient2

            contexts = [
                f"Class A has {dividend1} students and Class B has {dividend2} students. Both form teams of {divisor}. How many more teams does Class B have?",
                f"Store A sold {dividend1} items and Store B sold {dividend2} items. Each box holds {divisor} items. How many more boxes did Store B fill?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(quotient2 - quotient1)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"{dividend1} \\div {divisor} = {quotient1}", f"{dividend2} \\div {divisor} = {quotient2}", f"{quotient2} - {quotient1} = {quotient2 - quotient1}"],
                difficulty='challenge'
            )

        else:  # remainder
            divisor = random.choice([7, 8, 9])
            quotient = random.randint(4, 9)
            remainder = random.randint(1, divisor - 1)
            dividend = divisor * quotient + remainder

            contexts = [
                f"{dividend} pencils shared equally among {divisor} students",
                f"{dividend} books placed on {divisor} shelves equally",
                f"{dividend} candies divided into bags of {divisor}"
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
    generator = DivideBy7_8_Or9Generator()

    print("DIVIDE BY 7, 8, OR 9 GENERATOR TEST\n")
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

    print("\nChallenge (Multi-step, mixed operations, or remainders):")
    for problem in generator.generate_worksheet('challenge', 4):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print(f"  Steps: {problem.steps}\n")


if __name__ == '__main__':
    main()
