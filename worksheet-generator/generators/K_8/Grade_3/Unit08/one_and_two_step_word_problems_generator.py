"""
One and Two-Step Word Problems Generator - Grade 3 Unit 8
Generates mixed one and two-step word problems with all operations
Example: One-step: "24 cookies shared among 6 friends", Two-step: "5 bags of 8 apples, then 3 more"
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class OneAndTwoStepWordProblemsGenerator:
    """Generates one and two-step word problems."""

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
        """Generate easy problems: simple one-step problems."""
        operation = random.choice(['addition', 'subtraction', 'multiplication', 'division'])

        if operation == 'addition':
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
            answer = num1 + num2

            contexts = [
                f"Sarah has {num1} stickers. She gets {num2} more. How many stickers does she have now?",
                f"A store has {num1} red balloons and {num2} blue balloons. How many balloons total?",
                f"There are {num1} boys and {num2} girls in a class. How many students total?",
                f"A library has {num1} fiction books and {num2} non-fiction books. How many books total?"
            ]

            context = random.choice(contexts)
            steps = [f"{num1} + {num2} = {answer}"]

        elif operation == 'subtraction':
            num1 = random.randint(20, 60)
            num2 = random.randint(10, num1 - 5)
            answer = num1 - num2

            contexts = [
                f"There are {num1} cookies. If {num2} are eaten, how many are left?",
                f"A school has {num1} students. If {num2} go home early, how many remain?",
                f"Tom has {num1} pencils and gives away {num2}. How many does he have left?",
                f"A store has {num1} toys. If {num2} are sold, how many are left?"
            ]

            context = random.choice(contexts)
            steps = [f"{num1} - {num2} = {answer}"]

        elif operation == 'multiplication':
            num1 = random.randint(3, 8)
            num2 = random.randint(3, 8)
            answer = num1 * num2

            contexts = [
                f"Each box has {num2} crayons. If there are {num1} boxes, how many crayons total?",
                f"A garden has {num1} rows with {num2} plants in each row. How many plants total?",
                f"There are {num1} bags with {num2} apples in each bag. How many apples total?",
                f"Each shelf has {num2} books. If there are {num1} shelves, how many books total?"
            ]

            context = random.choice(contexts)
            steps = [f"{num1} \\times {num2} = {answer}"]

        else:  # division
            divisor = random.randint(3, 8)
            quotient = random.randint(3, 10)
            dividend = divisor * quotient
            answer = quotient

            contexts = [
                f"There are {dividend} cookies to share equally among {divisor} friends. How many does each get?",
                f"A teacher has {dividend} pencils to divide into {divisor} equal groups. How many per group?",
                f"If {dividend} students sit in {divisor} equal rows, how many students per row?",
                f"There are {dividend} apples packed equally into {divisor} bags. How many per bag?"
            ]

            context = random.choice(contexts)
            steps = [f"{dividend} \\div {divisor} = {answer}"]

        latex = f"\\text{{{context}}}"
        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: mix of one-step and simple two-step problems."""
        problem_type = random.choice(['one_step_harder', 'two_step_add_mult', 'two_step_mult_add'])

        if problem_type == 'one_step_harder':
            # Harder one-step with larger numbers
            operation = random.choice(['multiplication', 'division'])

            if operation == 'multiplication':
                num1 = random.randint(5, 12)
                num2 = random.randint(5, 12)
                answer = num1 * num2

                contexts = [
                    f"A store has {num1} boxes. Each box contains {num2} toys. How many toys total?",
                    f"Each page has {num2} stickers. If there are {num1} pages, how many stickers?",
                    f"A parking lot has {num1} rows with {num2} cars in each row. How many cars?",
                    f"Each basket has {num2} oranges. If there are {num1} baskets, how many oranges?"
                ]

                context = random.choice(contexts)
                steps = [f"{num1} \\times {num2} = {answer}"]

            else:  # division
                divisor = random.randint(5, 12)
                quotient = random.randint(5, 12)
                dividend = divisor * quotient
                answer = quotient

                contexts = [
                    f"There are {dividend} books to place equally on {divisor} shelves. How many per shelf?",
                    f"A farmer has {dividend} eggs to pack into {divisor} cartons equally. How many per carton?",
                    f"If {dividend} chairs are arranged into {divisor} equal rows, how many per row?",
                    f"A baker has {dividend} cookies to pack into {divisor} equal boxes. How many per box?"
                ]

                context = random.choice(contexts)
                steps = [f"{dividend} \\div {divisor} = {answer}"]

        elif problem_type == 'two_step_add_mult':
            # Multiply then add
            num_groups = random.randint(3, 8)
            per_group = random.randint(4, 9)
            additional = random.randint(5, 15)

            product = num_groups * per_group
            answer = product + additional

            contexts = [
                f"There are {num_groups} boxes with {per_group} books in each box, plus {additional} extra books. How many books total?",
                f"A baker makes {num_groups} trays with {per_group} cookies on each tray, then bakes {additional} more. How many cookies?",
                f"A class has {num_groups} tables with {per_group} students at each table, plus {additional} students standing. How many students?",
                f"There are {num_groups} bags with {per_group} marbles each, plus {additional} loose marbles. How many marbles?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Step 1: }} {num_groups} \\times {per_group} = {product}",
                f"\\text{{Step 2: }} {product} + {additional} = {answer}"
            ]

        else:  # two_step_mult_add
            # Add then multiply
            num1 = random.randint(3, 8)
            num2 = random.randint(3, 8)
            multiplier = random.randint(2, 5)

            sum_val = num1 + num2
            answer = sum_val * multiplier

            contexts = [
                f"Sarah has {num1} red pens and {num2} blue pens. If she buys {multiplier} sets like this, how many pens total?",
                f"A box has {num1} apples and {num2} oranges. If there are {multiplier} boxes, how many fruits total?",
                f"One bag has {num1} toys and another has {num2} toys. If there are {multiplier} pairs of bags, how many toys?",
                f"Team A has {num1} players and Team B has {num2} players. If there are {multiplier} games, how many total player-games?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Step 1: }} {num1} + {num2} = {sum_val}",
                f"\\text{{Step 2: }} {sum_val} \\times {multiplier} = {answer}"
            ]

        latex = f"\\text{{{context}}}"
        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: two-step problems with all operations."""
        problem_type = random.choice(['mult_subtract', 'div_add', 'mult_div', 'comparison'])

        if problem_type == 'mult_subtract':
            # Multiply then subtract
            groups = random.randint(5, 10)
            per_group = random.randint(5, 10)
            subtract = random.randint(10, 30)

            product = groups * per_group
            answer = product - subtract

            contexts = [
                f"A store has {groups} boxes with {per_group} items in each. If {subtract} items are sold, how many remain?",
                f"A baker makes {groups} trays with {per_group} muffins each. If {subtract} are given away, how many are left?",
                f"A library has {groups} shelves with {per_group} books on each. If {subtract} books are checked out, how many remain?",
                f"A garden has {groups} rows with {per_group} plants each. If {subtract} plants die, how many are left?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Step 1: }} {groups} \\times {per_group} = {product}",
                f"\\text{{Step 2: }} {product} - {subtract} = {answer}"
            ]

        elif problem_type == 'div_add':
            # Divide then add
            divisor = random.randint(4, 8)
            quotient = random.randint(5, 12)
            dividend = divisor * quotient
            additional = random.randint(5, 20)
            answer = quotient + additional

            contexts = [
                f"There are {dividend} cookies shared equally among {divisor} friends, then each gets {additional} more. How many does each have?",
                f"A teacher divides {dividend} pencils equally among {divisor} students, then gives each student {additional} more. How many per student?",
                f"A baker divides {dividend} muffins into {divisor} equal boxes, then adds {additional} more to each box. How many per box?",
                f"A group of {divisor} people share {dividend} dollars equally, then each person gets ${additional} more. How much does each have?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Step 1: }} {dividend} \\div {divisor} = {quotient}",
                f"\\text{{Step 2: }} {quotient} + {additional} = {answer}"
            ]

        elif problem_type == 'mult_div':
            # Multiply then divide
            num1 = random.randint(4, 8)
            num2 = random.randint(4, 8)
            divisor = random.randint(2, 4)

            product = num1 * num2
            # Make sure it divides evenly
            product = (product // divisor) * divisor
            answer = product // divisor

            contexts = [
                f"A store has {num1} boxes with {num2} items each. If all items are divided equally into {divisor} sections, how many per section?",
                f"There are {num1} bags with {num2} marbles each. If shared equally among {divisor} friends, how many does each get?",
                f"A baker makes {num1} trays with {num2} cookies each. If packed into {divisor} equal boxes, how many per box?",
                f"A teacher has {num1} groups of {num2} students each. If rearranged into {divisor} equal classes, how many per class?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Step 1: }} {num1} \\times {num2} = {product}",
                f"\\text{{Step 2: }} {product} \\div {divisor} = {answer}"
            ]

        else:  # comparison
            groups1 = random.randint(4, 8)
            per_group1 = random.randint(5, 10)
            groups2 = random.randint(4, 8)
            per_group2 = random.randint(5, 10)

            total1 = groups1 * per_group1
            total2 = groups2 * per_group2
            answer = abs(total1 - total2)

            contexts = [
                f"Store A has {groups1} shelves with {per_group1} items each. Store B has {groups2} shelves with {per_group2} items each. How many more items does one store have?",
                f"Garden A has {groups1} rows of {per_group1} plants. Garden B has {groups2} rows of {per_group2} plants. What is the difference?",
                f"Team A scored {per_group1} points in each of {groups1} games. Team B scored {per_group2} points in each of {groups2} games. What is the difference?",
                f"Class A has {groups1} tables with {per_group1} students each. Class B has {groups2} tables with {per_group2} students each. How many more students in one class?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{First group: }} {groups1} \\times {per_group1} = {total1}",
                f"\\text{{Second group: }} {groups2} \\times {per_group2} = {total2}",
                f"\\text{{Difference: }} |{total1} - {total2}| = {answer}"
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
        """Generate challenge problems: complex multi-step with strategic thinking."""
        problem_type = random.choice(['three_step', 'complex_comparison', 'mixed_operations'])

        if problem_type == 'three_step':
            # Three operations
            groups = random.randint(4, 8)
            per_group = random.randint(5, 9)
            add_amount = random.randint(10, 20)
            divisor = random.randint(2, 4)

            product = groups * per_group
            sum_val = product + add_amount
            # Make sure it divides evenly
            sum_val = (sum_val // divisor) * divisor
            answer = sum_val // divisor

            contexts = [
                f"A warehouse has {groups} shelves with {per_group} boxes on each. After adding {add_amount} more boxes, all boxes are divided equally into {divisor} trucks. How many per truck?",
                f"A baker makes {groups} trays with {per_group} cookies each, then bakes {add_amount} more. If divided equally into {divisor} bags, how many per bag?",
                f"A school has {groups} classes with {per_group} students each. After {add_amount} new students join, all are divided into {divisor} equal grade levels. How many per level?",
                f"A garden has {groups} sections with {per_group} plants each. After planting {add_amount} more, all are divided into {divisor} equal areas. How many per area?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Step 1: }} {groups} \\times {per_group} = {product}",
                f"\\text{{Step 2: }} {product} + {add_amount} = {sum_val}",
                f"\\text{{Step 3: }} {sum_val} \\div {divisor} = {answer}"
            ]

        elif problem_type == 'complex_comparison':
            # Compare after operations
            groups1 = random.randint(5, 10)
            per1 = random.randint(6, 12)
            subtract1 = random.randint(10, 25)

            groups2 = random.randint(5, 10)
            per2 = random.randint(6, 12)
            add2 = random.randint(10, 25)

            total1 = groups1 * per1 - subtract1
            total2 = groups2 * per2 + add2
            answer = abs(total1 - total2)

            contexts = [
                f"Store A has {groups1} boxes with {per1} items each, but {subtract1} are damaged. Store B has {groups2} boxes with {per2} items each, plus {add2} extra. How many more items does one store have?",
                f"Team A scores {per1} points in each of {groups1} games, but loses {subtract1} points for penalties. Team B scores {per2} points in each of {groups2} games, plus {add2} bonus points. What is the difference?",
                f"Garden A has {groups1} rows of {per1} plants, but {subtract1} die. Garden B has {groups2} rows of {per2} plants, plus {add2} more planted. What is the difference?",
                f"Class A has {groups1} tables with {per1} supplies each, but uses {subtract1}. Class B has {groups2} tables with {per2} supplies each, plus receives {add2} more. What is the difference?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{First: }} {groups1} \\times {per1} - {subtract1} = {groups1 * per1} - {subtract1} = {total1}",
                f"\\text{{Second: }} {groups2} \\times {per2} + {add2} = {groups2 * per2} + {add2} = {total2}",
                f"\\text{{Difference: }} |{total1} - {total2}| = {answer}"
            ]

        else:  # mixed_operations
            # All four operations
            start = random.randint(40, 80)
            add = random.randint(15, 30)
            multiplier = random.randint(2, 4)
            subtract = random.randint(20, 40)
            divisor = random.randint(2, 5)

            step1 = start + add
            step2 = step1 * multiplier
            step3 = step2 - subtract
            # Make sure it divides evenly
            step3 = (step3 // divisor) * divisor
            answer = step3 // divisor

            contexts = [
                f"A store starts with {start} items, receives {add} more, then orders {multiplier} times that amount. After selling {subtract} items, the rest are packed into {divisor} equal boxes. How many per box?",
                f"A baker has {start} cookies, bakes {add} more, then makes {multiplier} batches of that size. After giving away {subtract} cookies, the rest go into {divisor} equal bags. How many per bag?",
                f"A library has {start} books, receives {add} more, then gets {multiplier} shipments of that size. After {subtract} are checked out, the rest go on {divisor} equal shelves. How many per shelf?",
                f"A farmer has {start} plants, grows {add} more, then plants {multiplier} fields of that size. After {subtract} die, the rest are divided into {divisor} equal sections. How many per section?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Step 1: }} {start} + {add} = {step1}",
                f"\\text{{Step 2: }} {step1} \\times {multiplier} = {step2}",
                f"\\text{{Step 3: }} {step2} - {subtract} = {step3}",
                f"\\text{{Step 4: }} {step3} \\div {divisor} = {answer}"
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
    generator = OneAndTwoStepWordProblemsGenerator()

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
