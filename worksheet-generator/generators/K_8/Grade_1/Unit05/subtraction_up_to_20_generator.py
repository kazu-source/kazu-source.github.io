"""
Subtraction Up To 20 Generator - Grade 1 Unit05
Generates subtraction up to 20 problems
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class SubtractionUpTo20Generator:
    """Generates subtraction up to 20 problems."""

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
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        result = a + b if 'addition' in 'subtraction up to 20' or 'add' in 'subtraction up to 20' else max(a, b) - min(a, b)
        latex = f"{a} + {b} = " if 'add' in 'subtraction up to 20' else f"{max(a, b)} - {min(a, b)} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{solution}"])

def main():
    generator = SubtractionUpTo20Generator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")

if __name__ == '__main__':
    main()
