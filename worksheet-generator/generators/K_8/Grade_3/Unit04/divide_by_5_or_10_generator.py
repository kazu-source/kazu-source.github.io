"""
Divide by 5 or 10 Generator - Grade 3 Unit 4
Generates division problems focusing on dividing by 5 or 10
Emphasizes patterns and place value understanding
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DivideBy5Or10Generator:
    """Generates division problems with divisors 5 or 10."""

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
        """Generate easy problems: small dividends (up to 50)."""
        divisor = random.choice([5, 10])

        if divisor == 5:
            quotient = random.randint(1, 10)
        else:  # divisor == 10
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
        """Generate medium problems: larger dividends (up to 100)."""
        divisor = random.choice([5, 10])

        if divisor == 5:
            quotient = random.randint(5, 20)
        else:  # divisor == 10
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
        divisor = random.choice([5, 10])

        if divisor == 5:
            quotient = random.randint(4, 15)
        else:  # divisor == 10
            quotient = random.randint(3, 10)

        dividend = divisor * quotient

        if divisor == 5:
            contexts = [
                f"A nickel is worth 5 cents. How many nickels equal {dividend} cents?",
                f"There are {dividend} students in the gym. They form teams of {divisor}. How many teams are there?",
                f"A farmer picks {dividend} strawberries and puts {divisor} in each basket. How many baskets does she need?",
                f"A book has {dividend} pages. If you read {divisor} pages each day, how many days to finish?"
            ]
        else:  # divisor == 10
            contexts = [
                f"A dime is worth 10 cents. How many dimes equal {dividend} cents?",
                f"There are {dividend} eggs to pack in cartons of {divisor}. How many cartons are needed?",
                f"A rope is {dividend} meters long. It's cut into pieces of {divisor} meters each. How many pieces?",
                f"The school collected {dividend} cans for recycling. They pack {divisor} cans per box. How many boxes?"
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
        """Generate challenge problems: multi-step, patterns, or comparison problems."""
        problem_type = random.choice(['multi_step', 'comparison', 'pattern'])

        if problem_type == 'multi_step':
            # Add then divide or divide then add
            operation_order = random.choice(['add_divide', 'divide_add'])

            if operation_order == 'add_divide':
                num1 = random.randint(10, 30)
                num2 = random.randint(10, 30)
                total = num1 + num2
                divisor = random.choice([5, 10])
                # Make sure total is divisible
                quotient = total // divisor
                total = divisor * quotient

                contexts = [
                    f"Sarah has {num1} marbles and John has {total - num1} marbles. They combine them and share equally among {divisor} friends",
                    f"Two boxes contain {num1} and {total - num1} pencils. All pencils are divided into groups of {divisor}"
                ]

                context = random.choice(contexts)
                latex = f"\\text{{{context}. How many in each group?}}"
                solution = str(quotient)

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[f"{num1} + {total - num1} = {total}", f"{total} \\div {divisor} = {quotient}"],
                    difficulty='challenge'
                )
            else:
                # Divide then add
                divisor = random.choice([5, 10])
                quotient1 = random.randint(3, 8)
                dividend1 = divisor * quotient1
                extra = random.randint(2, 10)

                contexts = [
                    f"{dividend1} cookies are shared among {divisor} children. Then each child gets {extra} more cookies",
                    f"A teacher divides {dividend1} stickers among {divisor} students. Later, she gives each student {extra} more stickers"
                ]

                context = random.choice(contexts)
                latex = f"\\text{{{context}. How many does each have now?}}"
                solution = str(quotient1 + extra)

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[f"{dividend1} \\div {divisor} = {quotient1}", f"{quotient1} + {extra} = {quotient1 + extra}"],
                    difficulty='challenge'
                )

        elif problem_type == 'comparison':
            divisor = random.choice([5, 10])
            quotient1 = random.randint(4, 10)
            quotient2 = quotient1 + random.randint(2, 5)
            dividend1 = divisor * quotient1
            dividend2 = divisor * quotient2

            contexts = [
                f"Box A has {dividend1} items and Box B has {dividend2} items. Each box is divided into groups of {divisor}. How many more groups does Box B have?",
                f"Team A scored {dividend1} points and Team B scored {dividend2} points. If each touchdown is {divisor} points, how many more touchdowns did Team B score?"
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

        else:  # pattern
            # Missing number in pattern
            divisor = random.choice([5, 10])
            start_quotient = random.randint(2, 5)
            quotients = [start_quotient + i for i in range(4)]
            dividends = [q * divisor for q in quotients]

            # Hide one dividend
            hidden_index = random.randint(1, 2)
            pattern_str = ", ".join(str(d) if i != hidden_index else "?" for i, d in enumerate(dividends))

            latex = f"\\text{{Complete the pattern (dividing by {divisor}): {pattern_str}}}"
            solution = str(dividends[hidden_index])

            return Equation(
                latex=latex,
                solution=solution,
                steps=[f"\\text{{Pattern: }} {dividends[0]}, {dividends[1]}, {dividends[2]}, {dividends[3]}", f"\\text{{Missing: }} {dividends[hidden_index]}"],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = DivideBy5Or10Generator()

    print("DIVIDE BY 5 OR 10 GENERATOR TEST\n")
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

    print("\nChallenge (Multi-step, comparison, or patterns):")
    for problem in generator.generate_worksheet('challenge', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print(f"  Steps: {problem.steps}\n")


if __name__ == '__main__':
    main()
