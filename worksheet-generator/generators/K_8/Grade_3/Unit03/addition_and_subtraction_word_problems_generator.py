"""
Addition and Subtraction Word Problems Generator - Grade 3 Unit 3
Generates realistic word problems involving addition and subtraction within 1000
Includes various contexts appropriate for Grade 3 students
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AdditionAndSubtractionWordProblemsGenerator:
    """Generates addition and subtraction word problems."""

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
        """Generate easy problems: single-step addition or subtraction with 2-digit numbers."""
        operation = random.choice(['add', 'subtract'])

        if operation == 'add':
            num1 = random.randint(10, 75)
            num2 = random.randint(10, 75)
            result = num1 + num2

            contexts = [
                f"Emma has {num1} stickers. Her friend gives her {num2} more stickers. How many stickers does Emma have now?",
                f"There are {num1} books on one shelf and {num2} books on another shelf. How many books are there in total?",
                f"Tom collected {num1} rocks and {num2} shells at the beach. How many items did he collect?",
                f"A store sold {num1} apples in the morning and {num2} apples in the afternoon. How many apples were sold?",
                f"There are {num1} red balloons and {num2} blue balloons. How many balloons are there altogether?"
            ]

            steps = [
                f"\\text{{Add: }} {num1} + {num2} = {result}"
            ]
        else:  # subtract
            num1 = random.randint(30, 99)
            num2 = random.randint(10, num1 - 5)
            result = num1 - num2

            contexts = [
                f"Jack has {num1} marbles. He gives {num2} marbles to his friend. How many marbles does Jack have left?",
                f"There are {num1} students in the cafeteria. {num2} students leave. How many students are still in the cafeteria?",
                f"A baker made {num1} cookies. He sold {num2} cookies. How many cookies are left?",
                f"Sarah has {num1} crayons. She gives {num2} crayons to her sister. How many crayons does Sarah have now?",
                f"There were {num1} birds in a tree. {num2} birds flew away. How many birds are left in the tree?"
            ]

            steps = [
                f"\\text{{Subtract: }} {num1} - {num2} = {result}"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: single-step with 3-digit numbers or 2-step with 2-digit."""
        choice = random.randint(1, 2)

        if choice == 1:
            # Single-step with 3-digit numbers
            operation = random.choice(['add', 'subtract'])

            if operation == 'add':
                num1 = random.randint(100, 600)
                num2 = random.randint(100, 300)
                result = num1 + num2

                contexts = [
                    f"A school has {num1} books in the library and receives {num2} more books. How many books does the school have now?",
                    f"A store has {num1} items on Monday and {num2} items on Tuesday. How many items in total?",
                    f"A farmer harvested {num1} apples from one tree and {num2} apples from another. How many apples total?",
                    f"There are {num1} people at the first show and {num2} people at the second show. How many people attended?"
                ]

                steps = [
                    f"\\text{{Add: }} {num1} + {num2} = {result}"
                ]
            else:  # subtract
                num1 = random.randint(200, 900)
                num2 = random.randint(100, num1 - 50)
                result = num1 - num2

                contexts = [
                    f"A factory produced {num1} toys. They shipped {num2} toys to stores. How many toys are left?",
                    f"A theater has {num1} seats. {num2} seats are taken. How many empty seats are there?",
                    f"The library has {num1} books. {num2} books are checked out. How many books remain?",
                    f"A store had {num1} items. They sold {num2} items. How many items are left?"
                ]

                steps = [
                    f"\\text{{Subtract: }} {num1} - {num2} = {result}"
                ]
        else:
            # 2-step problem with 2-digit numbers
            num1 = random.randint(20, 60)
            num2 = random.randint(15, 50)
            num3 = random.randint(10, 40)

            operation_combo = random.choice(['add_add', 'add_subtract'])

            if operation_combo == 'add_add':
                result = num1 + num2 + num3

                contexts = [
                    f"Sarah has {num1} stickers. She gets {num2} stickers from her mom and {num3} stickers from her dad. How many stickers does she have?",
                    f"A store sold {num1} books on Monday, {num2} books on Tuesday, and {num3} books on Wednesday. How many books were sold?",
                    f"Tom collected {num1} coins, then found {num2} more, and then his grandma gave him {num3} more. How many coins does he have?"
                ]

                steps = [
                    f"\\text{{Add the first two: }} {num1} + {num2} = {num1 + num2}",
                    f"\\text{{Add the third: }} {num1 + num2} + {num3} = {result}"
                ]
            else:  # add_subtract
                result = num1 + num2 - num3

                contexts = [
                    f"Emily has {num1} candies. She gets {num2} more, then gives {num3} to her friend. How many candies does she have?",
                    f"A school has {num1} students. {num2} new students enroll, but {num3} students move away. How many students now?",
                    f"A library has {num1} books. They receive {num2} new books but {num3} books are damaged. How many good books?"
                ]

                steps = [
                    f"\\text{{Add: }} {num1} + {num2} = {num1 + num2}",
                    f"\\text{{Subtract: }} {num1 + num2} - {num3} = {result}"
                ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 2-step problems with 3-digit numbers."""
        num1 = random.randint(150, 500)
        num2 = random.randint(100, 400)
        num3 = random.randint(75, 250)

        operation_combo = random.choice(['add_add', 'add_subtract', 'subtract_add'])

        if operation_combo == 'add_add':
            result = num1 + num2 + num3

            contexts = [
                f"A store had {num1} items in stock. They received {num2} items on Monday and {num3} items on Tuesday. How many items do they have now?",
                f"Three schools are combining their book collections. School A has {num1} books, School B has {num2} books, and School C has {num3} books. How many books total?",
                f"A farmer harvested {num1} apples, {num2} oranges, and {num3} pears. How many pieces of fruit in total?"
            ]

            steps = [
                f"\\text{{Add first two: }} {num1} + {num2} = {num1 + num2}",
                f"\\text{{Add third: }} {num1 + num2} + {num3} = {result}"
            ]
        elif operation_combo == 'add_subtract':
            result = num1 + num2 - num3

            contexts = [
                f"A library has {num1} books. They receive {num2} new books but {num3} books are damaged. How many books are in good condition?",
                f"A factory produced {num1} toys. They made {num2} more toys, then shipped {num3} toys to stores. How many toys remain?",
                f"A parking lot has {num1} cars. {num2} more cars arrive, then {num3} cars leave. How many cars are in the lot?"
            ]

            steps = [
                f"\\text{{Add: }} {num1} + {num2} = {num1 + num2}",
                f"\\text{{Subtract: }} {num1 + num2} - {num3} = {result}"
            ]
        else:  # subtract_add
            # Ensure we don't get negative in first step
            num1 = random.randint(300, 700)
            num2 = random.randint(100, num1 - 50)
            num3 = random.randint(75, 250)
            result = num1 - num2 + num3

            contexts = [
                f"A theater has {num1} seats. {num2} seats are broken, but they add {num3} new seats. How many working seats are there?",
                f"A store had {num1} items. They sold {num2} items, then received {num3} new items. How many items do they have?",
                f"A school has {num1} students. {num2} students go on a field trip, but {num3} students from another school visit. How many students are at school?"
            ]

            steps = [
                f"\\text{{Subtract: }} {num1} - {num2} = {num1 - num2}",
                f"\\text{{Add: }} {num1 - num2} + {num3} = {result}"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step with comparison or complex scenarios."""
        problem_type = random.choice(['comparison', 'multi_step_complex'])

        if problem_type == 'comparison':
            # Comparison problems
            num1 = random.randint(200, 600)
            num2 = random.randint(150, 500)

            if num1 > num2:
                difference = num1 - num2
                contexts = [
                    f"School A has {num1} students and School B has {num2} students. How many more students does School A have?",
                    f"A library has {num1} fiction books and {num2} non-fiction books. How many more fiction books are there?",
                    f"Store A sold {num1} items and Store B sold {num2} items. How many more items did Store A sell?",
                    f"Tom has {num1} coins and Sarah has {num2} coins. How many more coins does Tom have?"
                ]
                result = difference
                steps = [
                    f"\\text{{Find the difference: }} {num1} - {num2} = {result}"
                ]
            else:
                difference = num2 - num1
                contexts = [
                    f"School A has {num1} students and School B has {num2} students. How many more students does School B have?",
                    f"A library has {num1} fiction books and {num2} non-fiction books. How many more non-fiction books are there?",
                    f"Store A sold {num1} items and Store B sold {num2} items. How many more items did Store B sell?",
                    f"Tom has {num1} coins and Sarah has {num2} coins. How many more coins does Sarah have?"
                ]
                result = difference
                steps = [
                    f"\\text{{Find the difference: }} {num2} - {num1} = {result}"
                ]
        else:
            # Multi-step complex
            num1 = random.randint(200, 500)
            num2 = random.randint(100, 300)
            num3 = random.randint(150, 400)
            num4 = random.randint(50, 200)

            contexts = [
                f"A store starts with {num1} items. They sell {num2} items on Monday and {num3} items on Tuesday, but receive {num4} new items on Wednesday. How many items does the store have now?",
                f"A library has {num1} books. {num2} books are checked out, {num3} more are donated, and {num4} are damaged. How many books remain?",
                f"A parking lot has {num1} spaces. {num2} cars park, then {num3} more spaces are added, and {num4} cars leave. How many empty spaces are there?"
            ]

            result = num1 - num2 + num4 - num3
            if result < 0:
                result = num1 - num2 + num3 - num4
                contexts = [
                    f"A store starts with {num1} items. They sell {num2} items, receive {num3} new items, then sell {num4} more. How many items remain?",
                ]

            steps = [
                f"\\text{{Start: }} {num1}",
                f"\\text{{After first change: }} {num1} - {num2} = {num1 - num2}",
                f"\\text{{Continue calculating step by step}}",
                f"\\text{{Final answer: }} {result}"
            ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AdditionAndSubtractionWordProblemsGenerator()

    print("Easy (Single-step with 2-digit numbers):")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nMedium (Single-step 3-digit or 2-step 2-digit):")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nHard (2-step with 3-digit numbers):")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()

    print("\nChallenge (Comparison or complex multi-step):")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()


if __name__ == '__main__':
    main()
