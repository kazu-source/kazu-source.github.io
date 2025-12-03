"""
Comparing Sizes Generator - Kindergarten Unit 2
Generates problems about comparing sizes (bigger, smaller, same size)
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ComparingSizesGenerator:
    """Generates comparing sizes problems."""

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
        obj1 = random.choice(['ball', 'box', 'car'])
        obj2 = random.choice(['ball', 'box', 'car'])
        latex = f"\text{{Which is bigger: a big {obj1} or a small {obj2}?}}"
        solution = f"big {obj1}"
        return Equation(latex=latex, solution=solution, steps=["bigger object"])

def main():
    generator = ComparingSizesGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
