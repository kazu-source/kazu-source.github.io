"""
Reading Clocks Introduction Generator - Kindergarten Unit 7
Generates basic clock reading problems (hour only)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ReadingClocksIntroductionGenerator:
    """Generates introduction to clock reading problems."""

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
        hour = random.randint(1, 12)
        latex = f"\\text{{The clock shows {hour} o'clock}}"
        solution = f"{hour} o'clock"
        return Equation(latex=latex, solution=solution, steps=[f"{hour}:00"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        hour = random.randint(1, 12)
        latex = f"\\text{{What time is it? The hour hand points to {hour}}}"
        solution = f"{hour} o'clock"
        return Equation(latex=latex, solution=solution, steps=[f"{hour}:00"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        hour = random.randint(1, 12)
        latex = f"\\text{{Draw the hour hand pointing to {hour}}}"
        solution = f"{hour} o'clock"
        return Equation(latex=latex, solution=solution, steps=["draw hour hand"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        hour1 = random.randint(1, 11)
        hour2 = hour1 + 1
        latex = f"\\text{{The hour hand is between {hour1} and {hour2}. What hour just passed?}}"
        solution = f"{hour1}"
        return Equation(latex=latex, solution=solution, steps=[f"{hour1} o'clock"], difficulty='challenge')


def main():
    generator = ReadingClocksIntroductionGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
