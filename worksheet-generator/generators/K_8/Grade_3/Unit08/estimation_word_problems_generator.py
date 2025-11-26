"""
Estimation Word Problems Generator - Grade 3 Unit 8
Generates word problems requiring estimation
Example: "About how many apples in 4 bags of 29 apples each?"
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EstimationWordProblemsGenerator:
    """Generates estimation word problems."""

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

    def _round_to_nearest_ten(self, num):
        """Round number to nearest 10."""
        return round(num / 10) * 10

    def _round_to_nearest_hundred(self, num):
        """Round number to nearest 100."""
        return round(num / 100) * 100

    def _generate_easy(self) -> Equation:
        """Generate easy problems: simple addition or subtraction estimation."""
        operation = random.choice(['addition', 'subtraction'])

        if operation == 'addition':
            # Round numbers close to tens
            num1_base = random.randint(2, 8) * 10
            num2_base = random.randint(2, 8) * 10
            num1 = num1_base + random.choice([-2, -1, 1, 2])
            num2 = num2_base + random.choice([-2, -1, 1, 2])

            rounded1 = self._round_to_nearest_ten(num1)
            rounded2 = self._round_to_nearest_ten(num2)
            estimate = rounded1 + rounded2

            contexts = [
                f"About how many apples are there if you have {num1} red apples and {num2} green apples?",
                f"A store has about {num1} books on one shelf and {num2} books on another. About how many books total?",
                f"Sam has {num1} stickers and Emma has {num2} stickers. About how many stickers do they have together?",
                f"There are about {num1} students in one grade and {num2} in another. About how many students total?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
                f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
                f"{rounded1} + {rounded2} = {estimate}"
            ]

        else:  # subtraction
            num1_base = random.randint(5, 9) * 10
            num2_base = random.randint(2, num1_base // 10 - 1) * 10
            num1 = num1_base + random.choice([-2, -1, 1, 2])
            num2 = num2_base + random.choice([-2, -1, 1, 2])

            rounded1 = self._round_to_nearest_ten(num1)
            rounded2 = self._round_to_nearest_ten(num2)
            estimate = rounded1 - rounded2

            contexts = [
                f"There are {num1} cookies. If {num2} are eaten, about how many are left?",
                f"A school has {num1} students. If {num2} are absent, about how many are present?",
                f"You have {num1} pencils and give away {num2}. About how many do you have left?",
                f"A library has {num1} books. If {num2} are checked out, about how many remain?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
                f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
                f"{rounded1} - {rounded2} = {estimate}"
            ]

        latex = f"\\text{{{context}}}"
        solution = str(estimate)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: multiplication estimation."""
        # Multiply a small number by a number close to a ten
        multiplier = random.randint(3, 9)
        base = random.randint(3, 9) * 10
        num = base + random.choice([-3, -2, -1, 1, 2, 3])

        rounded_num = self._round_to_nearest_ten(num)
        estimate = multiplier * rounded_num

        contexts = [
            f"Each box has about {num} crayons. If there are {multiplier} boxes, about how many crayons total?",
            f"A book has about {num} pages in each chapter. If there are {multiplier} chapters, about how many pages?",
            f"Each bag contains about {num} marbles. If you have {multiplier} bags, about how many marbles?",
            f"Each shelf has about {num} books. If there are {multiplier} shelves, about how many books total?"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(estimate)

        steps = [
            f"\\text{{Round }} {num} \\text{{ to }} {rounded_num}",
            f"{multiplier} \\times {rounded_num} = {estimate}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: larger numbers or division estimation."""
        problem_type = random.choice(['large_multiplication', 'division', 'two_step'])

        if problem_type == 'large_multiplication':
            # Multiply two numbers that round to tens or hundreds
            num1 = random.randint(15, 45)
            num2 = random.randint(15, 45)

            rounded1 = self._round_to_nearest_ten(num1)
            rounded2 = self._round_to_nearest_ten(num2)
            estimate = rounded1 * rounded2

            contexts = [
                f"A store sells about {num1} items per day. About how many items in {num2} days?",
                f"Each classroom has about {num1} students. If there are {num2} classrooms, about how many students?",
                f"A farmer picks about {num1} apples from each tree. With {num2} trees, about how many apples?",
                f"Each box weighs about {num1} pounds. If there are {num2} boxes, about how many pounds total?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
                f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
                f"{rounded1} \\times {rounded2} = {estimate}"
            ]

        elif problem_type == 'division':
            # Division estimation
            divisor = random.randint(4, 9)
            quotient_base = random.randint(8, 20)
            dividend = divisor * quotient_base + random.randint(-3, 3)

            rounded_dividend = self._round_to_nearest_ten(dividend)
            estimate = rounded_dividend // divisor

            contexts = [
                f"About how many ${divisor} items can you buy with ${dividend}?",
                f"If {dividend} students are divided into {divisor} equal groups, about how many per group?",
                f"About how many {divisor}-packs can you make from {dividend} items?",
                f"If {dividend} cookies are shared equally among {divisor} people, about how many each?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Round }} {dividend} \\text{{ to }} {rounded_dividend}",
                f"{rounded_dividend} \\div {divisor} \\approx {estimate}"
            ]

        else:  # two_step
            # Two-step estimation
            num1 = random.randint(25, 55)
            num2 = random.randint(25, 55)
            multiplier = random.randint(2, 5)

            rounded1 = self._round_to_nearest_ten(num1)
            rounded2 = self._round_to_nearest_ten(num2)
            sum_rounded = rounded1 + rounded2
            estimate = sum_rounded * multiplier

            contexts = [
                f"A store has {num1} red pencils and {num2} blue pencils. If they order {multiplier} times this amount, about how many pencils?",
                f"Class A has {num1} students and Class B has {num2} students. If the school has {multiplier} pairs of classes like this, about how many students?",
                f"One bag has {num1} marbles and another has {num2} marbles. If there are {multiplier} pairs of bags like this, about how many marbles?",
                f"Monday had {num1} visitors and Tuesday had {num2} visitors. If this pattern continues for {multiplier} weeks, about how many visitors?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
                f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
                f"{rounded1} + {rounded2} = {sum_rounded}",
                f"{sum_rounded} \\times {multiplier} = {estimate}"
            ]

        latex = f"\\text{{{context}}}"
        solution = str(estimate)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex estimation with reasoning."""
        problem_type = random.choice(['hundreds', 'complex_two_step', 'comparison'])

        if problem_type == 'hundreds':
            # Work with hundreds
            num1 = random.randint(150, 450)
            num2 = random.randint(150, 450)

            rounded1 = self._round_to_nearest_hundred(num1)
            rounded2 = self._round_to_nearest_hundred(num2)

            operation = random.choice(['add', 'subtract'])
            if operation == 'add':
                estimate = rounded1 + rounded2

                contexts = [
                    f"A school has {num1} students in the lower grades and {num2} in the upper grades. About how many students total?",
                    f"One warehouse has {num1} boxes and another has {num2} boxes. About how many boxes total?",
                    f"A library has {num1} fiction books and {num2} non-fiction books. About how many books total?",
                    f"A town has {num1} houses on the north side and {num2} on the south side. About how many houses total?"
                ]

                context = random.choice(contexts)
                steps = [
                    f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
                    f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
                    f"{rounded1} + {rounded2} = {estimate}"
                ]

            else:
                if num1 < num2:
                    num1, num2 = num2, num1
                    rounded1, rounded2 = rounded2, rounded1
                estimate = rounded1 - rounded2

                contexts = [
                    f"A stadium has {num1} seats. If {num2} are filled, about how many are empty?",
                    f"A store had {num1} items. After selling {num2}, about how many remain?",
                    f"A town has {num1} people. If {num2} move away, about how many are left?",
                    f"A farmer has {num1} plants. After harvesting {num2}, about how many remain?"
                ]

                context = random.choice(contexts)
                steps = [
                    f"\\text{{Round }} {num1} \\text{{ to }} {rounded1}",
                    f"\\text{{Round }} {num2} \\text{{ to }} {rounded2}",
                    f"{rounded1} - {rounded2} = {estimate}"
                ]

        elif problem_type == 'complex_two_step':
            # Complex two-step with larger numbers
            items_per = random.randint(35, 75)
            groups = random.randint(8, 15)
            additional = random.randint(25, 55)

            rounded_items = self._round_to_nearest_ten(items_per)
            rounded_groups = self._round_to_nearest_ten(groups)
            rounded_additional = self._round_to_nearest_ten(additional)

            product = rounded_items * rounded_groups
            estimate = product + rounded_additional

            contexts = [
                f"Each of {groups} classes has about {items_per} students, and there are {additional} staff members. About how many people total?",
                f"A warehouse has {groups} shelves with about {items_per} boxes on each, plus {additional} boxes on the floor. About how many boxes?",
                f"Each of {groups} stores sells about {items_per} items per day. After {additional} online sales, about how many total sales?",
                f"A school has {groups} classrooms with about {items_per} books in each, plus {additional} books in the library. About how many books?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Round }} {items_per} \\text{{ to }} {rounded_items}",
                f"\\text{{Round }} {groups} \\text{{ to }} {rounded_groups}",
                f"{rounded_items} \\times {rounded_groups} = {product}",
                f"\\text{{Round }} {additional} \\text{{ to }} {rounded_additional}",
                f"{product} + {rounded_additional} = {estimate}"
            ]

        else:  # comparison
            # Compare two products
            a1 = random.randint(15, 45)
            b1 = random.randint(15, 45)
            a2 = random.randint(15, 45)
            b2 = random.randint(15, 45)

            rounded_a1 = self._round_to_nearest_ten(a1)
            rounded_b1 = self._round_to_nearest_ten(b1)
            rounded_a2 = self._round_to_nearest_ten(a2)
            rounded_b2 = self._round_to_nearest_ten(b2)

            product1 = rounded_a1 * rounded_b1
            product2 = rounded_a2 * rounded_b2
            estimate = abs(product1 - product2)

            contexts = [
                f"Store A sells {a1} items at ${b1} each. Store B sells {a2} items at ${b2} each. About how much more does one store make?",
                f"Garden A has {a1} rows of {b1} plants. Garden B has {a2} rows of {b2} plants. About how many more plants in one garden?",
                f"Team A scored {a1} points in each of {b1} games. Team B scored {a2} points in each of {b2} games. About how many more points for one team?",
                f"Book A has {a1} pages per chapter for {b1} chapters. Book B has {a2} pages per chapter for {b2} chapters. About how many more pages in one book?"
            ]

            context = random.choice(contexts)
            steps = [
                f"\\text{{Store/Item 1: }} {rounded_a1} \\times {rounded_b1} = {product1}",
                f"\\text{{Store/Item 2: }} {rounded_a2} \\times {rounded_b2} = {product2}",
                f"\\text{{Difference: }} |{product1} - {product2}| = {estimate}"
            ]

        latex = f"\\text{{{context}}}"
        solution = str(estimate)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EstimationWordProblemsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 2):
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
