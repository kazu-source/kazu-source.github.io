"""
Introduction to Scatter Plots Generator - Grade 8 Unit 7
Generates problems introducing scatter plots
Example: Does this scatter plot show positive, negative, or no correlation?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroductionToScatterPlotsGenerator:
    """Generates introduction to scatter plots problems."""

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
        correlation = random.choice(['positive', 'negative', 'no'])

        descriptions = {
            'positive': "As hours studied increases, test scores increase.",
            'negative': "As hours of TV watched increases, test scores decrease.",
            'no': "Shoe size and test scores show no pattern."
        }

        latex = f"\\text{{What correlation: {descriptions[correlation]}}}"
        solution = f"\\text{{{correlation.capitalize()} correlation}}"
        steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{Which shows positive correlation: (A) Temperature vs ice cream sales (B) Age vs hair color?}"
        solution = "\\text{(A) Positive correlation}"
        steps = [
            "\\text{Temperature increases, ice cream sales increase}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{A scatter plot shows points trending upward. What's the correlation?}"
        solution = "\\text{Positive correlation}"
        steps = [
            "\\text{Upward trend = positive correlation}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{What does an outlier in a scatter plot represent?}"
        solution = "\\text{A data point far from the general pattern}"
        steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = IntroductionToScatterPlotsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
