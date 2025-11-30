"""
Extending Patterns Generator - Kindergarten Unit 3
Generates problems about extending simple patterns
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ExtendingPatternsGenerator:
    """Generates extending patterns problems."""

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
        elem1, elem2 = random.choice([('●', '○'), ('A', 'B'), ('△', '○')])
        latex = f"\\text{{Continue: {elem1}, {elem2}, {elem1}, {elem2}, {elem1}, ___}}"
        solution = elem2
        return Equation(latex=latex, solution=solution, steps=[f"{elem1}, {elem2} pattern"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        pattern = random.choice([
            (['red', 'red', 'blue'], 'red'),
            (['1', '2', '1'], '2'),
            (['●', '●', '○'], '●')
        ])
        pat, ans = pattern
        seq = pat + pat
        latex = f"\\text{{What comes next: {', '.join(seq)}, ___}}"
        solution = ans
        return Equation(latex=latex, solution=solution, steps=[f"pattern: {', '.join(pat)}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        elem1 = random.choice(['A', '●', 'red'])
        elem2 = random.choice(['B', '○', 'blue'])
        elem3 = random.choice(['C', '△', 'green'])
        latex = f"\\text{{Extend: {elem1}, {elem2}, {elem3}, {elem1}, {elem2}, ___}}"
        solution = elem3
        return Equation(latex=latex, solution=solution, steps=[f"{elem1}, {elem2}, {elem3} pattern"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        numbers = list(range(1, 6))
        start = random.choice(numbers[:3])
        pattern = [str(start), str(start + 1), str(start + 2)]
        latex = f"\\text{{Continue counting: {', '.join(pattern)}, ___}}"
        solution = str(start + 3)
        return Equation(latex=latex, solution=solution, steps=["counting pattern"], difficulty='challenge')


def main():
    generator = ExtendingPatternsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
