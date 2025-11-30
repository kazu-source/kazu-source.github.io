"""
Above Below Beside Between Generator - Kindergarten Unit 6
Generates problems about positional words
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AboveBelowBesideBetweenGenerator:
    """Generates above, below, beside, between problems."""

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
        position = random.choice(['above', 'below'])
        obj1 = random.choice(['bird', 'cloud', 'sun'])
        obj2 = random.choice(['tree', 'house', 'car'])
        latex = f"\\text{{The {obj1} is {position} the {obj2}}}"
        solution = position
        return Equation(latex=latex, solution=solution, steps=[f"{obj1} is {position}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        position = random.choice(['beside', 'next to'])
        obj1 = random.choice(['cat', 'dog', 'ball'])
        obj2 = random.choice(['box', 'chair', 'door'])
        latex = f"\\text{{Where is the {obj1}? It is {position} the {obj2}.}}"
        solution = position
        return Equation(latex=latex, solution=solution, steps=[f"{position} the {obj2}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        obj1 = random.choice(['apple', 'star', 'toy'])
        obj2 = random.choice(['tree', 'box', 'shelf'])
        obj3 = random.choice(['orange', 'circle', 'block'])
        latex = f"\\text{{The {obj1} is between the {obj2} and the {obj3}}}"
        solution = "between"
        return Equation(latex=latex, solution=solution, steps=["between two objects"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        positions = ['above', 'below', 'beside', 'between']
        position = random.choice(positions)
        latex = f"\\text{{Draw a circle {position} the square}}"
        solution = position
        return Equation(latex=latex, solution=solution, steps=[f"place {position}"], difficulty='challenge')


def main():
    generator = AboveBelowBesideBetweenGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
