"""
Fractions Introduction Generator - Grade 3 Unit 5
Generates problems focused on understanding fractions as parts of a whole
Example: What fraction is shaded? 1/2, 1/3, 1/4, etc.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class FractionsIntroGenerator:
    """Generates fractions introduction problems."""

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
        """Generate easy problems: halves, thirds, fourths."""
        denominators = [2, 3, 4]
        denominator = random.choice(denominators)
        numerator = random.randint(1, denominator)

        if numerator == denominator:
            numerator = random.randint(1, denominator - 1)  # Avoid whole numbers for now

        fraction_names = {2: "halves", 3: "thirds", 4: "fourths"}

        latex = f"\\text{{What fraction is represented: }} {numerator} \\text{{ out of }} {denominator} \\text{{ {fraction_names[denominator]}?}}"
        solution = f"\\frac{{{numerator}}}{{{denominator}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{numerator} parts out of {denominator} total = }} \\frac{{{numerator}}}{{{denominator}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: fifths, sixths, eighths."""
        denominators = [5, 6, 8]
        denominator = random.choice(denominators)
        numerator = random.randint(1, denominator - 1)

        fraction_names = {5: "fifths", 6: "sixths", 8: "eighths"}

        latex = f"\\text{{What fraction is represented: }} {numerator} \\text{{ out of }} {denominator} \\text{{ {fraction_names[denominator]}?}}"
        solution = f"\\frac{{{numerator}}}{{{denominator}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{numerator} parts out of {denominator} total = }} \\frac{{{numerator}}}{{{denominator}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with visual fraction contexts."""
        denominator = random.choice([2, 3, 4, 6, 8])
        numerator = random.randint(1, denominator - 1)

        contexts = [
            f"A pizza is cut into {denominator} equal slices. If you eat {numerator} slices, what fraction did you eat?",
            f"A chocolate bar has {denominator} equal pieces. You give away {numerator} pieces. What fraction did you give away?",
            f"A garden has {denominator} equal sections. You plant flowers in {numerator} sections. What fraction has flowers?",
            f"A ribbon is divided into {denominator} equal parts. You use {numerator} parts. What fraction did you use?"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = f"\\frac{{{numerator}}}{{{denominator}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{numerator} parts out of {denominator} total = }} \\frac{{{numerator}}}{{{denominator}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: more complex fractions and contexts."""
        denominator = random.choice([6, 8, 10, 12])
        numerator = random.randint(1, denominator - 1)

        contexts = [
            f"A class of {denominator} students goes on a field trip. {numerator} students bring lunch from home. What fraction brought lunch?",
            f"A bookshelf has {denominator} shelves. Books are on {numerator} shelves. What fraction of shelves have books?",
            f"A necklace has {denominator} beads. {numerator} beads are blue. What fraction of the beads are blue?",
            f"A parking lot has {denominator} spaces. {numerator} spaces are filled. What fraction of spaces are filled?"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = f"\\frac{{{numerator}}}{{{denominator}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{numerator} parts out of {denominator} total = }} \\frac{{{numerator}}}{{{denominator}}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = FractionsIntroGenerator()

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
