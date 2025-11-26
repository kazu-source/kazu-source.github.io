"""
Fractions and Whole Numbers Generator - Grade 3 Unit 5
Generates problems exploring the relationship between fractions and whole numbers
Example: 4/4 = 1, 6/3 = 2, representing whole numbers as fractions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class FractionsAndWholeNumbersGenerator:
    """Generates fractions and whole numbers relationship problems."""

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
        """Generate easy problems: simple fractions equal to 1."""
        denominator = random.choice([2, 3, 4])
        numerator = denominator  # Makes it equal to 1

        problem_type = random.choice(['fraction_to_whole', 'whole_to_fraction'])

        if problem_type == 'fraction_to_whole':
            latex = f"\\frac{{{numerator}}}{{{denominator}}} = \\text{{?}}"
            solution = "1"
            steps = [f"\\text{{{numerator} out of {numerator} parts = 1 whole}}"]
        else:
            latex = f"1 = \\frac{{\\text{{?}}}}{{{denominator}}}"
            solution = str(denominator)
            steps = [f"\\text{{1 whole = }} \\frac{{{denominator}}}{{{denominator}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: fractions equal to small whole numbers."""
        whole = random.randint(2, 4)
        denominator = random.choice([2, 3, 4, 5])
        numerator = whole * denominator

        problem_type = random.choice(['fraction_to_whole', 'whole_to_fraction'])

        if problem_type == 'fraction_to_whole':
            latex = f"\\frac{{{numerator}}}{{{denominator}}} = \\text{{?}}"
            solution = str(whole)
            steps = [f"\\text{{{numerator} ÷ {denominator} = {whole}}}"]
        else:
            latex = f"{whole} = \\frac{{\\text{{?}}}}{{{denominator}}}"
            solution = str(numerator)
            steps = [f"\\text{{{whole} = }} \\frac{{{numerator}}}{{{denominator}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with fractions and whole numbers."""
        whole = random.randint(2, 5)
        denominator = random.choice([2, 3, 4, 6])
        numerator = whole * denominator

        contexts = [
            f"Maria cuts {whole} pizzas into {denominator} slices each. How many slices does she have in total? Express as a fraction.",
            f"A recipe needs {whole} cups of flour. If you measure in \\frac{{1}}{{{denominator}}} cup portions, how many portions is that?",
            f"There are {whole} boxes of crayons with {denominator} crayons in each box. Write the total as a fraction.",
            f"Tom has {whole} whole apples. He cuts each into {denominator} pieces. Write the total pieces as a fraction."
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = f"\\frac{{{numerator}}}{{{denominator}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{whole} wholes = }} \\frac{{{numerator}}}{{{denominator}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: more complex relationships."""
        whole = random.randint(3, 6)
        denominator = random.choice([4, 6, 8])
        numerator = whole * denominator

        problem_types = ['mixed_problem', 'comparison']
        problem_type = random.choice(problem_types)

        if problem_type == 'mixed_problem':
            contexts = [
                f"A baker makes {whole} cakes and cuts each into {denominator} slices. Write two ways to show the total slices: as a whole number times {denominator} and as a fraction.",
                f"If \\frac{{{numerator}}}{{{denominator}}} represents a whole number, what whole number is it?",
                f"Express {whole} as a fraction with denominator {denominator}.",
                f"A classroom has {whole} shelves with {denominator} books on each shelf. Write the total as a fraction."
            ]
            context = random.choice(contexts)

            if "what whole number" in context:
                solution = str(whole)
                steps = [f"\\frac{{{numerator}}}{{{denominator}}} = {whole}"]
            else:
                solution = f"\\frac{{{numerator}}}{{{denominator}}} \\text{{ or }} {whole}"
                steps = [f"{whole} = \\frac{{{numerator}}}{{{denominator}}}"]
        else:
            # Comparison problem
            other_whole = whole + 1
            other_numerator = other_whole * denominator
            latex = f"\\text{{Which is greater: }} \\frac{{{numerator}}}{{{denominator}}} \\text{{ or }} {other_whole}\\text{{?}}"
            solution = str(other_whole)
            steps = [f"\\frac{{{numerator}}}{{{denominator}}} = {whole}, \\text{{ and }} {whole} < {other_whole}"]

            return Equation(
                latex=latex,
                solution=solution,
                steps=steps,
                difficulty='challenge'
            )

        latex = f"\\text{{{context}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = FractionsAndWholeNumbersGenerator()

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
