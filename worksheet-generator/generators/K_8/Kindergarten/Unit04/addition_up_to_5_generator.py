"""
Addition Up to 5 Generator - Kindergarten Unit 4
Generates basic addition problems with sums up to 5
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class AdditionUpTo5Generator:
    """Generates addition up to 5 problems."""

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
        a = random.randint(1, 2)
        b = random.randint(1, 3)
        total = a + b
        if total <= 5:
            latex = f"{a} + {b} = "
            solution = str(total)
            return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"])
        else:
            return self._generate_easy()

def main():
    generator = AdditionUpTo5Generator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
