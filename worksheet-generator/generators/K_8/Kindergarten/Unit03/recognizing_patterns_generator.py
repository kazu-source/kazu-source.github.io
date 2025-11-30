"""
Recognizing Patterns Generator - Kindergarten Unit 3
Generates problems about recognizing simple patterns
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RecognizingPatternsGenerator:
    """Generates recognizing patterns problems."""

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
        pattern = random.choice([
            ('A', 'B', 'A', 'B'),
            ('red', 'blue', 'red', 'blue'),
            ('○', '●', '○', '●')
        ])
        latex = f"\\text{{Pattern: {pattern[0]}, {pattern[1]}, {pattern[2]}, {pattern[3]}, ___}}"
        solution = pattern[0]
        return Equation(latex=latex, solution=solution, steps=[f"pattern repeats: {pattern[0]}, {pattern[1]}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        patterns = [
            (['●', '○', '○'], '●'),
            (['△', '△', '○'], '△'),
            (['A', 'B', 'C'], 'A')
        ]
        pattern, answer = random.choice(patterns)
        latex = f"\\text{{What comes next: {', '.join(pattern)}, {', '.join(pattern)}, ___}}"
        solution = answer
        return Equation(latex=latex, solution=solution, steps=[f"pattern: {', '.join(pattern)}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        colors = random.sample(['red', 'blue', 'green', 'yellow'], 2)
        latex = f"\\text{{The pattern is {colors[0]}, {colors[1]}, {colors[0]}, {colors[1]}. What is the pattern?}}"
        solution = f"{colors[0]}, {colors[1]}"
        return Equation(latex=latex, solution=solution, steps=["AB pattern"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        pattern = random.choice([
            (['A', 'B', 'B'], 'A'),
            (['1', '2', '3'], '1'),
            (['●', '○', '●', '●'], '○')
        ])
        pat, ans = pattern
        latex = f"\\text{{Continue the pattern: {', '.join(pat * 2)}, ___}}"
        solution = ans
        return Equation(latex=latex, solution=solution, steps=[f"pattern: {', '.join(pat)}"], difficulty='challenge')


def main():
    generator = RecognizingPatternsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
