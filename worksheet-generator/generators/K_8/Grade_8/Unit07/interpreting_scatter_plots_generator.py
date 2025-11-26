"""
Interpreting Scatter Plots Generator - Grade 8 Unit 7
Generates problems about interpreting scatter plots
Example: Describe the relationship shown in the scatter plot.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class InterpretingScatterPlotsGenerator:
    """Generates interpreting scatter plots problems."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        latex = "\\text{A scatter plot shows strong positive correlation. What does this mean?}"
        solution = "\\text{As x increases, y increases consistently}"
        steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{Data points are widely scattered with no pattern. What's the correlation?}"
        solution = "\\text{No correlation}"
        steps = [
            "\\text{No clear pattern = no correlation}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Strong negative correlation between study time and errors. Interpret this.}"
        solution = "\\text{More study time leads to fewer errors}"
        steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Can correlation prove causation?}"
        solution = "\\text{No, correlation does not imply causation}"
        steps = [
            "\\text{Correlation shows association, not cause}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = InterpretingScatterPlotsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
