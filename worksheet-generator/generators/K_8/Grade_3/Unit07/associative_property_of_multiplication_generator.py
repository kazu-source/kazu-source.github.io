"""
Associative Property of Multiplication Generator - Grade 3 Unit 7
Generates problems showing (a × b) × c = a × (b × c)
Example: (2 × 3) × 4 = 2 × (3 × 4)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AssociativePropertyGenerator:
    """Generates problems demonstrating the associative property of multiplication."""

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
        """Generate easy problems: small numbers, showing both groupings."""
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        c = random.randint(2, 4)

        first_product = a * b
        second_product = b * c
        answer = a * b * c

        # Show the grouping calculation
        problem_type = random.choice(['left_first', 'right_first'])

        if problem_type == 'left_first':
            latex = f"({a} \\times {b}) \\times {c}"
            steps = [
                f"{a} \\times {b} = {first_product}",
                f"{first_product} \\times {c} = {answer}"
            ]
        else:
            latex = f"{a} \\times ({b} \\times {c})"
            steps = [
                f"{b} \\times {c} = {second_product}",
                f"{a} \\times {second_product} = {answer}"
            ]

        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: compare both groupings or fill in missing number."""
        problem_type = random.choice(['compare', 'fill_blank'])

        if problem_type == 'compare':
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 6)

            first_product = a * b
            second_product = b * c
            answer = a * b * c

            latex = f"({a} \\times {b}) \\times {c} = {a} \\times ({b} \\times {c})"
            solution = str(answer)
            steps = [
                f"\\text{{Left side: }} {a} \\times {b} = {first_product}, \\text{{ then }} {first_product} \\times {c} = {answer}",
                f"\\text{{Right side: }} {b} \\times {c} = {second_product}, \\text{{ then }} {a} \\times {second_product} = {answer}",
                f"\\text{{Both equal }} {answer}"
            ]

        else:  # fill_blank
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 6)

            first_product = a * b
            second_product = b * c
            answer = a * b * c

            # Ask for the missing result
            side = random.choice(['left', 'right'])
            if side == 'left':
                latex = f"({a} \\times {b}) \\times {c} = \\text{{?}}"
                steps = [
                    f"{a} \\times {b} = {first_product}",
                    f"{first_product} \\times {c} = {answer}"
                ]
            else:
                latex = f"{a} \\times ({b} \\times {c}) = \\text{{?}}"
                steps = [
                    f"{b} \\times {c} = {second_product}",
                    f"{a} \\times {second_product} = {answer}"
                ]

            solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: larger numbers and identifying easier grouping."""
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        c = random.randint(2, 8)

        first_product = a * b
        second_product = b * c
        answer = a * b * c

        problem_type = random.choice(['choose_easier', 'complete_equation', 'word_problem'])

        if problem_type == 'choose_easier':
            # Present both options and ask which is easier
            latex = f"\\text{{Which is easier to calculate: }} ({a} \\times {b}) \\times {c} \\text{{ or }} {a} \\times ({b} \\times {c})\\text{{? Find the answer.}}"

            # Determine which is actually easier (smaller intermediate product)
            if first_product <= second_product:
                easier = f"({a} \\times {b}) \\times {c}"
                steps = [
                    f"\\text{{Easier: }} ({a} \\times {b}) \\times {c}",
                    f"{a} \\times {b} = {first_product}",
                    f"{first_product} \\times {c} = {answer}"
                ]
            else:
                easier = f"{a} \\times ({b} \\times {c})"
                steps = [
                    f"\\text{{Easier: }} {a} \\times ({b} \\times {c})",
                    f"{b} \\times {c} = {second_product}",
                    f"{a} \\times {second_product} = {answer}"
                ]

            solution = str(answer)

        elif problem_type == 'complete_equation':
            # Give left side, ask for right side calculation
            latex = f"({a} \\times {b}) \\times {c} = {a} \\times (\\text{{?}} \\times {c})"
            solution = str(b)
            steps = [
                f"\\text{{The missing number is }} {b}",
                f"\\text{{Both sides equal }} {answer}"
            ]

        else:  # word_problem
            contexts = [
                f"A store has {a} shelves, each with {b} boxes, and each box has {c} items. How many items total?",
                f"There are {a} classrooms with {b} tables in each classroom. Each table has {c} students. How many students?",
                f"A baker makes {a} batches of cookies. Each batch has {b} trays, and each tray has {c} cookies. How many cookies?",
                f"A garden has {a} sections. Each section has {b} rows, and each row has {c} plants. How many plants?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(answer)
            steps = [
                f"\\text{{Method 1: }} ({a} \\times {b}) \\times {c} = {first_product} \\times {c} = {answer}",
                f"\\text{{Method 2: }} {a} \\times ({b} \\times {c}) = {a} \\times {second_product} = {answer}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex applications with larger numbers."""
        problem_type = random.choice(['strategic_grouping', 'missing_value', 'application'])

        if problem_type == 'strategic_grouping':
            # Create a problem where one grouping is much easier
            # Use numbers like 5×2 = 10 or 4×25 = 100
            easy_pairs = [(5, 2), (2, 5), (4, 25), (25, 4), (10, 10), (5, 4), (4, 5)]
            b, c = random.choice(easy_pairs)
            a = random.randint(3, 9)

            first_product = a * b
            second_product = b * c
            answer = a * b * c

            latex = f"\\text{{Use the associative property to find }} {a} \\times {b} \\times {c}"
            solution = str(answer)
            steps = [
                f"\\text{{Group strategically: }} {a} \\times ({b} \\times {c})",
                f"{b} \\times {c} = {second_product}",
                f"{a} \\times {second_product} = {answer}",
                f"\\text{{This is easier than }} ({a} \\times {b}) \\times {c} = {first_product} \\times {c}"
            ]

        elif problem_type == 'missing_value':
            a = random.randint(3, 9)
            b = random.randint(3, 9)
            c = random.randint(3, 9)
            answer = a * b * c

            # Give the final answer and ask for verification
            latex = f"\\text{{If }} ({a} \\times {b}) \\times {c} = {answer}, \\text{{ does }} {a} \\times ({b} \\times {c}) = {answer}\\text{{?}}"
            solution = "Yes"

            first_product = a * b
            second_product = b * c
            steps = [
                f"\\text{{Check left: }} {a} \\times {b} = {first_product}, {first_product} \\times {c} = {answer}",
                f"\\text{{Check right: }} {b} \\times {c} = {second_product}, {a} \\times {second_product} = {answer}",
                f"\\text{{Yes, both equal }} {answer}"
            ]

        else:  # application
            a = random.randint(4, 10)
            b = random.randint(4, 10)
            c = random.randint(4, 10)
            answer = a * b * c

            contexts = [
                f"A warehouse has {a} floors. Each floor has {b} aisles, and each aisle has {c} boxes. How many boxes in total?",
                f"A library has {a} bookcases. Each bookcase has {b} shelves, and each shelf has {c} books. How many books?",
                f"A parking lot has {a} levels. Each level has {b} sections, and each section has {c} parking spots. How many spots?",
                f"An orchard has {a} sections. Each section has {b} rows of trees, and each row has {c} trees. How many trees?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(answer)

            first_product = a * b
            second_product = b * c
            steps = [
                f"\\text{{Method 1: }} ({a} \\times {b}) \\times {c} = {first_product} \\times {c} = {answer}",
                f"\\text{{Method 2: }} {a} \\times ({b} \\times {c}) = {a} \\times {second_product} = {answer}",
                f"\\text{{Both methods give the same answer!}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AssociativePropertyGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")

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
