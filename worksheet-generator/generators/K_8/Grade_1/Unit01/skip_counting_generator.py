"""
Skip Counting Generator - Grade 1 Unit 1
Generates skip counting problems (by 2s, 5s, 10s)
Note: K-2 generators do not use difficulty levels.
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

    def generate_worksheet(self, difficulty: str = None, num_problems: int = 8) -> List[Equation]:
        """Generate worksheet problems. Note: difficulty parameter is ignored for K-2."""
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem()
            problems.append(problem)
        return problems

    def _generate_problem(self) -> Equation:
        start = random.choice([2, 4, 6, 8])
        skip = 2
        next_num = start + skip
        latex = f"\\text{{Skip count by 2s: }} {start}, {next_num}, \\_"
        solution = str(next_num + skip)
        return Equation(latex=latex, solution=solution, steps=[f"add {skip}"])

def main():
    generator = SkipCountingGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
