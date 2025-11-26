"""
Fractions in Contexts Generator - Grade 3 Unit 5
Generates problems applying fractions to real-world situations
Example: 1/4 of 12 apples, finding parts of groups
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class FractionsInContextsGenerator:
    """Generates fractions in real-world contexts problems."""

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
        """Generate easy problems: halves and fourths of small numbers."""
        denominators = [2, 4]
        denominator = random.choice(denominators)

        # Choose total that divides evenly
        multiples = {2: [2, 4, 6, 8, 10, 12], 4: [4, 8, 12, 16, 20]}
        total = random.choice(multiples[denominator])
        numerator = 1

        result = (numerator * total) // denominator

        contexts = [
            f"apples",
            f"cookies",
            f"students",
            f"toys"
        ]
        item = random.choice(contexts)

        latex = f"\\text{{What is }} \\frac{{{numerator}}}{{{denominator}}} \\text{{ of {total} {item}?}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{numerator}}}{{{denominator}}} \\times {total} = {result}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: thirds, fifths, sixths of medium numbers."""
        denominators = [3, 5, 6]
        denominator = random.choice(denominators)

        # Choose total that divides evenly
        multiples = {3: [3, 6, 9, 12, 15, 18], 5: [5, 10, 15, 20, 25], 6: [6, 12, 18, 24]}
        total = random.choice(multiples[denominator])
        numerator = random.randint(1, denominator - 1)

        result = (numerator * total) // denominator

        contexts = [
            f"A bag contains {total} marbles",
            f"There are {total} flowers in a garden",
            f"A box has {total} crayons",
            f"A basket has {total} oranges"
        ]
        context = random.choice(contexts)

        latex = f"\\text{{{context}. What is }} \\frac{{{numerator}}}{{{denominator}}} \\text{{ of them?}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{numerator}}}{{{denominator}}} \\times {total} = {result}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: more complex word problems."""
        denominator = random.choice([2, 3, 4, 6])
        multiples = {2: [6, 8, 10, 12, 14, 16], 3: [9, 12, 15, 18, 21],
                    4: [8, 12, 16, 20, 24], 6: [12, 18, 24, 30]}
        total = random.choice(multiples[denominator])
        numerator = random.randint(1, denominator - 1)

        result = (numerator * total) // denominator

        contexts = [
            f"Sarah has {total} stickers. She gives \\frac{{{numerator}}}{{{denominator}}} to her friend. How many stickers did she give away?",
            f"A library has {total} books. \\frac{{{numerator}}}{{{denominator}}} of them are fiction. How many fiction books are there?",
            f"There are {total} students in class. \\frac{{{numerator}}}{{{denominator}}} walk to school. How many students walk?",
            f"A farmer has {total} chickens. \\frac{{{numerator}}}{{{denominator}}} are brown. How many brown chickens are there?"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{numerator}}}{{{denominator}}} \\times {total} = {result}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: larger numbers and more complex fractions."""
        denominator = random.choice([4, 6, 8, 10])
        multiples = {4: [16, 20, 24, 28, 32], 6: [18, 24, 30, 36],
                    8: [16, 24, 32, 40], 10: [20, 30, 40, 50]}
        total = random.choice(multiples[denominator])
        numerator = random.randint(1, denominator - 1)

        result = (numerator * total) // denominator

        contexts = [
            f"A school has {total} computers. \\frac{{{numerator}}}{{{denominator}}} are laptops. How many laptops does the school have?",
            f"A store sells {total} shirts in a day. \\frac{{{numerator}}}{{{denominator}}} are blue. How many blue shirts were sold?",
            f"There are {total} pages in a book. Emma has read \\frac{{{numerator}}}{{{denominator}}} of the book. How many pages has she read?",
            f"A bakery made {total} muffins. \\frac{{{numerator}}}{{{denominator}}} have chocolate chips. How many muffins have chocolate chips?"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\frac{{{numerator}}}{{{denominator}}} \\times {total} = {result}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = FractionsInContextsGenerator()

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
