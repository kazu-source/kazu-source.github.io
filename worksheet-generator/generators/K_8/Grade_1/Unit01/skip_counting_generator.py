"""
Skip Counting Generator - Grade 1 Unit 1
Generates skip counting problems (by 2s, 5s, 10s)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SkipCountingGenerator:
    """Generates skip counting problems."""

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
        start = random.choice([2, 4, 6, 8])
        skip = 2
        next_num = start + skip
        latex = f"\\text{{Skip count by 2s: }} {start}, {next_num}, \\_ "
        solution = str(next_num + skip)
        return Equation(latex=latex, solution=solution, steps=[f"add {skip}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        skip = 5
        start = random.choice([5, 10, 15, 20])
        sequence = [str(start + i * skip) for i in range(4)]
        latex = f"\\text{{Skip count by 5s: }} {', '.join(sequence)}, \\_ "
        solution = str(start + 4 * skip)
        return Equation(latex=latex, solution=solution, steps=[f"add {skip}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        skip = 10
        start = random.choice([10, 20, 30])
        sequence = [str(start + i * skip) for i in range(3)]
        latex = f"\\text{{Skip count by 10s: }} {', '.join(sequence)}, \\_ "
        solution = str(start + 3 * skip)
        return Equation(latex=latex, solution=solution, steps=[f"add {skip}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        skip = random.choice([2, 5, 10])
        start = skip * random.randint(1, 5)
        missing_pos = random.randint(1, 3)
        sequence = [str(start + i * skip) if i != missing_pos else '___' for i in range(5)]
        solution = str(start + missing_pos * skip)
        latex = f"\\text{{Fill in: }} {', '.join(sequence)}"
        return Equation(latex=latex, solution=solution, steps=[f"skip by {skip}"], difficulty='challenge')


def main():
    generator = SkipCountingGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
