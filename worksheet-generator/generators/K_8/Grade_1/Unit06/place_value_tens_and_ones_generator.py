"""
Place Value Tens And Ones Generator - Grade 1 Unit06
Generates place value tens and ones problems
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class PlaceValueTensAndOnesGenerator:
    """Generates place value tens and ones problems."""

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
        tens = random.randint(1, 5)
        ones = random.randint(0, 9)
        num = tens * 10 + ones
        latex = f"\text{{{tens} tens and {ones} ones = ?}}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{tens} × 10 + {ones} = {num}"])

def main():
    generator = PlaceValueTensAndOnesGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")

if __name__ == '__main__':
    main()
