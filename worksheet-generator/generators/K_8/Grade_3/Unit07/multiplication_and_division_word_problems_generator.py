"""
Multiplication and Division Word Problems Generator - Grade 3 Unit 7
Generates word problems requiring multiplication or division
Example: "If 6 boxes each contain 8 pencils, how many pencils total?"
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplicationDivisionWordProblemsGenerator:
    """Generates multiplication and division word problems."""

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
        """Generate easy problems: simple multiplication word problems with small numbers."""
        num1 = random.randint(2, 5)
        num2 = random.randint(2, 5)
        answer = num1 * num2

        contexts = [
            (f"There are {num1} bags with {num2} apples in each bag. How many apples total?", f"{num1} \\times {num2}"),
            (f"A classroom has {num1} tables with {num2} students at each table. How many students?", f"{num1} \\times {num2}"),
            (f"Each basket has {num2} oranges. If there are {num1} baskets, how many oranges?", f"{num1} \\times {num2}"),
            (f"There are {num1} boxes with {num2} crayons in each box. How many crayons total?", f"{num1} \\times {num2}")
        ]

        context, equation = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(answer)

        steps = [
            f"{equation} = {answer}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: multiplication and simple division."""
        problem_type = random.choice(['multiplication', 'division'])

        if problem_type == 'multiplication':
            num1 = random.randint(3, 10)
            num2 = random.randint(3, 10)
            answer = num1 * num2

            contexts = [
                (f"Each shelf has {num2} books. If there are {num1} shelves, how many books total?", f"{num1} \\times {num2}"),
                (f"A garden has {num1} rows with {num2} plants in each row. How many plants?", f"{num1} \\times {num2}"),
                (f"There are {num1} teams with {num2} players on each team. How many players total?", f"{num1} \\times {num2}"),
                (f"Each box contains {num2} markers. If there are {num1} boxes, how many markers?", f"{num1} \\times {num2}")
            ]

            context, equation = random.choice(contexts)
            steps = [f"{equation} = {answer}"]

        else:  # division
            divisor = random.randint(3, 10)
            quotient = random.randint(2, 10)
            dividend = divisor * quotient
            answer = quotient

            contexts = [
                (f"There are {dividend} cookies to be shared equally among {divisor} friends. How many each?", f"{dividend} \\div {divisor}"),
                (f"A teacher has {dividend} pencils to divide equally into {divisor} groups. How many per group?", f"{dividend} \\div {divisor}"),
                (f"If {dividend} students sit in {divisor} equal rows, how many students per row?", f"{dividend} \\div {divisor}"),
                (f"There are {dividend} apples packed into {divisor} bags equally. How many per bag?", f"{dividend} \\div {divisor}")
            ]

            context, equation = random.choice(contexts)
            steps = [f"{equation} = {answer}"]

        latex = f"\\text{{{context}}}"
        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: more complex word problems."""
        problem_type = random.choice(['multiplication', 'division', 'mixed'])

        if problem_type == 'multiplication':
            num1 = random.randint(5, 12)
            num2 = random.randint(5, 12)
            answer = num1 * num2

            contexts = [
                f"A store has {num1} boxes. Each box contains {num2} toys. How many toys are there in total?",
                f"A parking lot has {num1} rows with {num2} cars in each row. How many cars total?",
                f"Each page in a book has {num2} pictures. If there are {num1} pages, how many pictures?",
                f"A baker makes {num1} trays of cookies. Each tray has {num2} cookies. How many cookies total?"
            ]

            context = random.choice(contexts)
            steps = [f"{num1} \\times {num2} = {answer}"]

        elif problem_type == 'division':
            divisor = random.randint(5, 12)
            quotient = random.randint(4, 12)
            dividend = divisor * quotient
            answer = quotient

            contexts = [
                f"A school has {dividend} students who need to be divided into {divisor} equal classes. How many students per class?",
                f"There are {dividend} books to place equally on {divisor} shelves. How many books per shelf?",
                f"A farmer has {dividend} eggs to pack into {divisor} cartons equally. How many eggs per carton?",
                f"If {dividend} chairs are arranged into {divisor} equal rows, how many chairs per row?"
            ]

            context = random.choice(contexts)
            steps = [f"{dividend} \\div {divisor} = {answer}"]

        else:  # mixed - find missing factor
            factor1 = random.randint(5, 12)
            answer = random.randint(4, 12)
            product = factor1 * answer

            contexts = [
                f"Books cost ${factor1} each. If you spend ${product}, how many books did you buy?",
                f"Each basket holds {factor1} apples. If there are {product} apples total, how many baskets?",
                f"Tickets cost ${factor1} each. If the total cost is ${product}, how many tickets?",
                f"Each box has {factor1} pencils. If there are {product} pencils total, how many boxes?"
            ]

            context = random.choice(contexts)
            steps = [
                f"{product} \\div {factor1} = {answer}",
                f"\\text{{Or: }} {factor1} \\times {answer} = {product}"
            ]

        latex = f"\\text{{{context}}}"
        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex multi-step thinking."""
        problem_type = random.choice(['comparison', 'two_operations', 'finding_factor'])

        if problem_type == 'comparison':
            num1 = random.randint(4, 8)
            num2 = random.randint(5, 10)
            answer1 = num1 * num2
            answer2 = answer1 + random.randint(5, 15)
            answer = answer2 - answer1

            contexts = [
                f"Amy has {num1} packs of {num2} stickers. Ben has {answer2} stickers. How many more stickers does Ben have?",
                f"A store sold {num1} boxes of {num2} pencils. Another store sold {answer2} pencils. How many more did the second store sell?",
                f"Team A scored {num1} goals in each of {num2} games. Team B scored {answer2} goals total. How many more goals did Team B score?",
                f"Sarah read {num1} pages each day for {num2} days. Tom read {answer2} pages total. How many more pages did Tom read?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{First group: }} {num1} \\times {num2} = {answer1}",
                f"\\text{{Difference: }} {answer2} - {answer1} = {answer}"
            ]

        elif problem_type == 'two_operations':
            # Total divided by groups
            items_per = random.randint(4, 8)
            groups = random.randint(5, 10)
            total = items_per * groups
            new_groups = random.randint(3, 6)

            if new_groups < groups:
                answer = total // new_groups

                contexts = [
                    f"There are {groups} bags with {items_per} marbles in each bag. If you put all the marbles into {new_groups} equal bags instead, how many marbles per bag?",
                    f"A teacher has {groups} boxes with {items_per} books in each box. If she reorganizes into {new_groups} equal boxes, how many books per box?",
                    f"There are {groups} teams with {items_per} players each. If they reorganize into {new_groups} equal teams, how many players per team?",
                    f"A store has {groups} shelves with {items_per} items on each. If they use {new_groups} shelves instead, how many items per shelf?"
                ]

                context = random.choice(contexts)
                steps = [
                    f"\\text{{Total items: }} {groups} \\times {items_per} = {total}",
                    f"\\text{{New groups: }} {total} \\div {new_groups} = {answer}"
                ]
            else:
                # Simpler version
                total = items_per * groups
                answer = total // 2
                contexts = [
                    f"There are {groups} bags with {items_per} candies each. If shared equally between 2 friends, how many candies does each get?",
                    f"A baker makes {groups} trays with {items_per} muffins each. If divided equally into 2 boxes, how many per box?"
                ]
                context = random.choice(contexts)
                steps = [
                    f"\\text{{Total: }} {groups} \\times {items_per} = {total}",
                    f"\\text{{Each person: }} {total} \\div 2 = {answer}"
                ]

        else:  # finding_factor
            factor1 = random.randint(6, 12)
            answer = random.randint(7, 15)
            product = factor1 * answer

            contexts = [
                f"A rectangular garden has {product} square feet. If one side is {factor1} feet long, how long is the other side?",
                f"An array has {product} objects arranged in {factor1} equal rows. How many objects per row?",
                f"A book has {product} pages divided into {factor1} equal chapters. How many pages per chapter?",
                f"A classroom has {product} desks arranged in {factor1} equal columns. How many desks per column?"
            ]

            context = random.choice(contexts)
            steps = [
                f"{product} \\div {factor1} = {answer}",
                f"\\text{{Check: }} {factor1} \\times {answer} = {product}"
            ]

        latex = f"\\text{{{context}}}"
        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiplicationDivisionWordProblemsGenerator()

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
