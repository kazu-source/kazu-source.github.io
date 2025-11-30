"""
Days and Weeks Generator - Kindergarten Unit 7
Generates problems about days of the week
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class DaysAndWeeksGenerator:
    """Generates days and weeks problems."""

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
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = random.choice(days)
        latex = f"\\text{{What day is {day}?}}"
        solution = day
        return Equation(latex=latex, solution=solution, steps=[day], difficulty='easy')

    def _generate_medium(self) -> Equation:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        idx = random.randint(0, 5)
        latex = f"\\text{{What day comes after {days[idx]}?}}"
        solution = days[idx + 1]
        return Equation(latex=latex, solution=solution, steps=[f"{days[idx + 1]}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = f"\\text{{How many days are in a week?}}"
        solution = "7"
        return Equation(latex=latex, solution=solution, steps=["7 days"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        day = random.choice(days)
        latex = f"\\text{{Is {day} a weekday or weekend?}}"
        solution = "weekday"
        return Equation(latex=latex, solution=solution, steps=["weekday"], difficulty='challenge')


def main():
    generator = DaysAndWeeksGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
