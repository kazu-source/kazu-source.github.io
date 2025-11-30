"""
Seasons Generator - Kindergarten Unit 7
Generates problems about the four seasons
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SeasonsGenerator:
    """Generates seasons problems."""

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
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        season = random.choice(seasons)
        latex = f"\\text{{Name a season: {season}}}"
        solution = season
        return Equation(latex=latex, solution=solution, steps=[season], difficulty='easy')

    def _generate_medium(self) -> Equation:
        season_activities = {
            'Spring': 'flowers bloom',
            'Summer': 'hot and sunny',
            'Fall': 'leaves fall',
            'Winter': 'cold and snowy'
        }
        season, activity = random.choice(list(season_activities.items()))
        latex = f"\\text{{In which season do we see {activity}?}}"
        solution = season
        return Equation(latex=latex, solution=solution, steps=[season], difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = f"\\text{{How many seasons are there in a year?}}"
        solution = "4"
        return Equation(latex=latex, solution=solution, steps=["4 seasons"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        idx = random.randint(0, 2)
        latex = f"\\text{{What season comes after {seasons[idx]}?}}"
        solution = seasons[idx + 1]
        return Equation(latex=latex, solution=solution, steps=[seasons[idx + 1]], difficulty='challenge')


def main():
    generator = SeasonsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
