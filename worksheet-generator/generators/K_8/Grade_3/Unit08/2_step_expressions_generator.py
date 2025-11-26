"""
Two-Step Expressions Generator - Grade 3 Unit 8
Generates two-step expressions with mixed operations
Example: 5 + 3 × 2, (8 - 2) × 4
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class TwoStepExpressionsGenerator:
    """Generates two-step expression problems."""

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
        """Generate easy problems: addition/subtraction followed by multiplication (with parentheses)."""
        num1 = random.randint(2, 8)
        num2 = random.randint(1, 5)
        multiplier = random.randint(2, 5)

        operation = random.choice(['+', '-'])

        if operation == '+':
            intermediate = num1 + num2
            answer = intermediate * multiplier
            latex = f"({num1} + {num2}) \\times {multiplier}"
            steps = [
                f"\\text{{Step 1: }} {num1} + {num2} = {intermediate}",
                f"\\text{{Step 2: }} {intermediate} \\times {multiplier} = {answer}"
            ]
        else:
            if num1 < num2:
                num1, num2 = num2, num1
            intermediate = num1 - num2
            answer = intermediate * multiplier
            latex = f"({num1} - {num2}) \\times {multiplier}"
            steps = [
                f"\\text{{Step 1: }} {num1} - {num2} = {intermediate}",
                f"\\text{{Step 2: }} {intermediate} \\times {multiplier} = {answer}"
            ]

        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: mixed operations including division, order of operations."""
        problem_type = random.choice(['multiply_first', 'divide_first', 'parentheses_division'])

        if problem_type == 'multiply_first':
            # a + b × c (multiplication first)
            a = random.randint(2, 10)
            b = random.randint(2, 6)
            c = random.randint(2, 6)

            intermediate = b * c
            answer = a + intermediate

            latex = f"{a} + {b} \\times {c}"
            steps = [
                f"\\text{{Step 1 (multiply): }} {b} \\times {c} = {intermediate}",
                f"\\text{{Step 2 (add): }} {a} + {intermediate} = {answer}"
            ]

        elif problem_type == 'divide_first':
            # a + b ÷ c (division first)
            c = random.randint(2, 6)
            quotient = random.randint(2, 8)
            b = c * quotient
            a = random.randint(2, 10)

            intermediate = b // c
            answer = a + intermediate

            latex = f"{a} + {b} \\div {c}"
            steps = [
                f"\\text{{Step 1 (divide): }} {b} \\div {c} = {intermediate}",
                f"\\text{{Step 2 (add): }} {a} + {intermediate} = {answer}"
            ]

        else:  # parentheses_division
            # (a + b) ÷ c
            c = random.randint(2, 5)
            quotient = random.randint(3, 10)
            sum_val = c * quotient
            a = random.randint(2, sum_val - 2)
            b = sum_val - a

            answer = quotient

            latex = f"({a} + {b}) \\div {c}"
            steps = [
                f"\\text{{Step 1 (add): }} {a} + {b} = {sum_val}",
                f"\\text{{Step 2 (divide): }} {sum_val} \\div {c} = {answer}"
            ]

        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: more complex expressions or word problems."""
        problem_type = random.choice(['complex_order', 'word_problem', 'three_numbers'])

        if problem_type == 'complex_order':
            # a × b + c × d (two multiplications then add)
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 6)
            d = random.randint(2, 6)

            product1 = a * b
            product2 = c * d
            answer = product1 + product2

            latex = f"{a} \\times {b} + {c} \\times {d}"
            steps = [
                f"\\text{{Step 1: }} {a} \\times {b} = {product1}",
                f"\\text{{Step 2: }} {c} \\times {d} = {product2}",
                f"\\text{{Step 3: }} {product1} + {product2} = {answer}"
            ]

        elif problem_type == 'word_problem':
            # Word problem requiring two operations
            num_groups = random.randint(3, 8)
            per_group = random.randint(3, 8)
            additional = random.randint(5, 15)

            total = num_groups * per_group + additional

            contexts = [
                f"There are {num_groups} boxes with {per_group} books in each box, plus {additional} extra books. How many books total?",
                f"A class has {num_groups} tables with {per_group} students at each table, plus {additional} students standing. How many students?",
                f"A baker makes {num_groups} trays with {per_group} cookies on each tray, then bakes {additional} more cookies. How many cookies total?",
                f"There are {num_groups} bags with {per_group} apples each, plus {additional} loose apples. How many apples total?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            answer = total

            product = num_groups * per_group
            steps = [
                f"\\text{{Step 1: }} {num_groups} \\times {per_group} = {product}",
                f"\\text{{Step 2: }} {product} + {additional} = {answer}"
            ]

        else:  # three_numbers
            # (a + b) × c - d
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 5)

            sum_val = a + b
            product = sum_val * c
            d = random.randint(1, min(10, product - 1))
            answer = product - d

            latex = f"({a} + {b}) \\times {c} - {d}"
            steps = [
                f"\\text{{Step 1: }} {a} + {b} = {sum_val}",
                f"\\text{{Step 2: }} {sum_val} \\times {c} = {product}",
                f"\\text{{Step 3: }} {product} - {d} = {answer}"
            ]

        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex multi-step with all operations."""
        problem_type = random.choice(['four_operations', 'complex_word', 'nested_parentheses'])

        if problem_type == 'four_operations':
            # a × b + c ÷ d
            a = random.randint(2, 7)
            b = random.randint(2, 7)
            d = random.randint(2, 6)
            quotient = random.randint(2, 8)
            c = d * quotient

            product = a * b
            div_result = c // d
            answer = product + div_result

            latex = f"{a} \\times {b} + {c} \\div {d}"
            steps = [
                f"\\text{{Step 1 (multiply): }} {a} \\times {b} = {product}",
                f"\\text{{Step 2 (divide): }} {c} \\div {d} = {div_result}",
                f"\\text{{Step 3 (add): }} {product} + {div_result} = {answer}"
            ]

        elif problem_type == 'complex_word':
            # Complex word problem
            groups = random.randint(4, 8)
            per_group = random.randint(4, 8)
            multiplier = random.randint(2, 4)

            total_items = groups * per_group
            answer = total_items * multiplier

            contexts = [
                f"A store has {groups} shelves with {per_group} items on each shelf. If each item costs ${multiplier}, what is the total value?",
                f"There are {groups} classrooms with {per_group} students in each. If each student has {multiplier} pencils, how many pencils total?",
                f"A garden has {groups} rows with {per_group} plants each. If each plant produces {multiplier} flowers, how many flowers total?",
                f"A library has {groups} sections with {per_group} books in each section. If each book has {multiplier} bookmarks, how many bookmarks?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"

            steps = [
                f"\\text{{Step 1: }} {groups} \\times {per_group} = {total_items}",
                f"\\text{{Step 2: }} {total_items} \\times {multiplier} = {answer}"
            ]

        else:  # nested_parentheses
            # (a × b + c) ÷ d
            d = random.randint(2, 5)
            quotient = random.randint(4, 12)
            sum_val = d * quotient

            a = random.randint(2, 5)
            b = random.randint(2, 5)
            product = a * b

            if product >= sum_val:
                c = 1
                sum_val = product + c
                quotient = sum_val // d
                if sum_val % d != 0:
                    sum_val = d * quotient
                    c = sum_val - product
            else:
                c = sum_val - product

            answer = quotient

            latex = f"({a} \\times {b} + {c}) \\div {d}"
            steps = [
                f"\\text{{Step 1: }} {a} \\times {b} = {product}",
                f"\\text{{Step 2: }} {product} + {c} = {sum_val}",
                f"\\text{{Step 3: }} {sum_val} \\div {d} = {answer}"
            ]

        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = TwoStepExpressionsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
