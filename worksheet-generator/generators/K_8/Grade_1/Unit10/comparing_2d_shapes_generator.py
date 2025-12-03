"""
Comparing 2d Shapes Generator - Grade 1 Unit10
Generates comparing 2D shapes problems
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class Comparing2dShapesGenerator:
    """Generates comparing 2D shapes problems."""

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
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        latex = f"{a} + {b} = "
        solution = str(a + b)
        return Equation(latex=latex, solution=solution, steps=["step"])

def main():
    generator = Comparing2dShapesGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")

if __name__ == '__main__':
    main()
