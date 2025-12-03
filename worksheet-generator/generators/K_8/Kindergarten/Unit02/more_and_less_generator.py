"""
More and Less Generator - Kindergarten Unit 2
Generates problems about comparing quantities using more and less
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class MoreAndLessGenerator:
    """Generates more and less comparison problems."""

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
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        while num1 == num2:
            num2 = random.randint(1, 5)
        if num1 > num2:
            latex = f"\text{{Which is more: }} {num1} \text{{ or }} {num2}?"
            solution = str(num1)
        else:
            latex = f"\text{{Which is more: }} {num1} \text{{ or }} {num2}?"
            solution = str(num2)
        return Equation(latex=latex, solution=solution, steps=[f"{solution} is more"])

def main():
    generator = MoreAndLessGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
