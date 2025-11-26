"""
Multiplying by Tens Generator - Grade 3 Unit 7
Generates problems showing patterns when multiplying by 10, 20, 30, etc.
Example: 7 × 10 = 70, 7 × 20 = 140
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyingByTensGenerator:
    """Generates problems for multiplying by tens."""

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
        """Generate easy problems: multiply single digit by 10."""
        num = random.randint(1, 9)
        answer = num * 10

        latex = f"{num} \\times 10"
        solution = str(answer)

        steps = [
            f"{num} \\times 10 = {answer}",
            f"\\text{{Pattern: Add a zero to }} {num}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: multiply by 20, 30, 40, etc."""
        num = random.randint(2, 9)
        tens_multiplier = random.randint(2, 9)
        tens_value = tens_multiplier * 10

        answer = num * tens_value

        latex = f"{num} \\times {tens_value}"
        solution = str(answer)

        intermediate = num * tens_multiplier

        steps = [
            f"{num} \\times {tens_value} = {num} \\times ({tens_multiplier} \\times 10)",
            f"{num} \\times {tens_multiplier} = {intermediate}",
            f"{intermediate} \\times 10 = {answer}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: two-digit × tens or word problems."""
        problem_type = random.choice(['two_digit', 'word_problem', 'pattern'])

        if problem_type == 'two_digit':
            num = random.randint(10, 20)
            tens_multiplier = random.randint(2, 9)
            tens_value = tens_multiplier * 10

            answer = num * tens_value

            latex = f"{num} \\times {tens_value}"
            solution = str(answer)

            intermediate = num * tens_multiplier

            steps = [
                f"{num} \\times {tens_value} = {num} \\times ({tens_multiplier} \\times 10)",
                f"{num} \\times {tens_multiplier} = {intermediate}",
                f"{intermediate} \\times 10 = {answer}"
            ]

        elif problem_type == 'word_problem':
            num = random.randint(3, 9)
            tens_multiplier = random.randint(2, 9)
            tens_value = tens_multiplier * 10
            answer = num * tens_value

            contexts = [
                f"Each box contains {tens_value} pencils. If there are {num} boxes, how many pencils total?",
                f"A book has {num} chapters. Each chapter has {tens_value} pages. How many pages total?",
                f"There are {num} bags with ${tens_value} in each bag. How much money total?",
                f"A school has {num} classrooms. Each classroom has {tens_value} crayons. How many crayons total?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(answer)

            intermediate = num * tens_multiplier
            steps = [
                f"{num} \\times {tens_value} = {num} \\times ({tens_multiplier} \\times 10)",
                f"{num} \\times {tens_multiplier} = {intermediate}",
                f"{intermediate} \\times 10 = {answer}"
            ]

        else:  # pattern
            num = random.randint(3, 9)
            answer1 = num
            answer2 = num * 10
            answer3 = num * 100

            latex = f"\\text{{Complete the pattern: }} {num} \\times 1 = {answer1}, \\; {num} \\times 10 = \\text{{?}}, \\; {num} \\times 100 = \\text{{?}}"
            solution = f"{answer2}, {answer3}"

            steps = [
                f"{num} \\times 10 = {answer2}",
                f"{num} \\times 100 = {answer3}",
                f"\\text{{Pattern: Add zeros}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex applications and larger numbers."""
        problem_type = random.choice(['hundreds', 'comparison', 'application', 'missing_factor'])

        if problem_type == 'hundreds':
            num = random.randint(2, 9)
            hundreds_multiplier = random.randint(1, 9)
            hundreds_value = hundreds_multiplier * 100

            answer = num * hundreds_value

            latex = f"{num} \\times {hundreds_value}"
            solution = str(answer)

            intermediate = num * hundreds_multiplier

            steps = [
                f"{num} \\times {hundreds_value} = {num} \\times ({hundreds_multiplier} \\times 100)",
                f"{num} \\times {hundreds_multiplier} = {intermediate}",
                f"{intermediate} \\times 100 = {answer}"
            ]

        elif problem_type == 'comparison':
            num = random.randint(4, 9)
            tens_multiplier = random.randint(3, 7)
            tens_value = tens_multiplier * 10

            answer1 = num * tens_multiplier
            answer2 = num * tens_value
            difference = answer2 - answer1

            latex = f"\\text{{How much larger is }} {num} \\times {tens_value} \\text{{ than }} {num} \\times {tens_multiplier}\\text{{?}}"
            solution = str(difference)

            steps = [
                f"{num} \\times {tens_value} = {answer2}",
                f"{num} \\times {tens_multiplier} = {answer1}",
                f"{answer2} - {answer1} = {difference}"
            ]

        elif problem_type == 'application':
            num = random.randint(5, 12)
            tens_multiplier = random.randint(3, 9)
            tens_value = tens_multiplier * 10
            answer = num * tens_value

            contexts = [
                f"A warehouse has {num} shelves. Each shelf holds {tens_value} boxes. How many boxes can the warehouse hold?",
                f"A school orders {num} packs of paper. Each pack contains {tens_value} sheets. How many sheets total?",
                f"A farmer has {num} fields. Each field can grow {tens_value} plants. How many plants total?",
                f"A store sells {num} cases of water. Each case has {tens_value} bottles. How many bottles total?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(answer)

            intermediate = num * tens_multiplier
            steps = [
                f"{num} \\times {tens_value}",
                f"= {num} \\times ({tens_multiplier} \\times 10)",
                f"= {intermediate} \\times 10",
                f"= {answer}"
            ]

        else:  # missing_factor
            # Given product and one factor (a multiple of 10), find other factor
            num = random.randint(3, 9)
            tens_multiplier = random.randint(2, 9)
            tens_value = tens_multiplier * 10
            product = num * tens_value

            latex = f"\\text{{?}} \\times {tens_value} = {product}"
            solution = str(num)

            steps = [
                f"{product} \\div {tens_value} = \\text{{?}}",
                f"{product} \\div {tens_value} = {product} \\div 10 \\div {tens_multiplier}",
                f"= {product // 10} \\div {tens_multiplier}",
                f"= {num}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiplyingByTensGenerator()

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
