"""
Visualize Percents Generator - Grade 6 Unit 3
Generates problems visualizing percents with grids and models
Example: If 40 out of 100 squares are shaded, what percent is shaded?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class VisualizePercentsGenerator:
    """Generates visualize percents problems."""

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
        """Generate easy problems: 100-square grids."""
        shaded = random.choice([10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90])
        percent = shaded

        latex = f"\\text{{A 100-square grid has {shaded} squares shaded. What percent is shaded?}}"
        solution = f"{percent}\\%"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\frac{{{shaded}}}{{100}} = {percent}\\%"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: finding part given percent."""
        percent = random.choice([10, 20, 25, 30, 40, 50, 60, 75, 80])
        total = 100
        part = (percent * total) // 100

        latex = f"\\text{{If {percent}\\% of a 100-square grid is shaded, how many squares are shaded?}}"
        solution = f"{part} squares"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{percent}\\% \\text{{ of }} 100 = \\frac{{{percent}}}{{100}} \\times 100 = {part}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: grids not equal to 100."""
        totals = [50, 25, 20, 40, 80]
        total = random.choice(totals)
        percents = [20, 25, 40, 50, 60, 75, 80]
        percent = random.choice([p for p in percents if (p * total) % 100 == 0])
        shaded = (percent * total) // 100

        latex = f"\\text{{A grid has {total} squares total. If {shaded} squares are shaded, what percent is shaded?}}"
        solution = f"{percent}\\%"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\frac{{{shaded}}}{{{total}}} = \\frac{{{shaded} \\times 100}}{{{total} \\times 100}} = \\frac{{{shaded * 100 // total}}}{{100}} = {percent}\\%"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing two percents visually."""
        shaded1 = random.choice([15, 20, 25, 35, 45])
        total1 = random.choice([50, 100])
        percent1 = (shaded1 * 100) // total1

        shaded2 = random.choice([10, 15, 20, 30, 40])
        total2 = random.choice([25, 50])
        percent2 = (shaded2 * 100) // total2

        greater = "Grid A" if percent1 > percent2 else "Grid B" if percent2 > percent1 else "Equal"

        latex = f"\\text{{Grid A: {shaded1} of {total1} squares shaded. Grid B: {shaded2} of {total2} squares shaded.}}"
        latex += f"\\text{{ Which grid has a greater percent shaded?}}"
        solution = greater

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Grid A: }} \\frac{{{shaded1}}}{{{total1}}} = {percent1}\\%",
                f"\\text{{Grid B: }} \\frac{{{shaded2}}}{{{total2}}} = {percent2}\\%",
                f"\\text{{Greater: }} {greater}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = VisualizePercentsGenerator()

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
