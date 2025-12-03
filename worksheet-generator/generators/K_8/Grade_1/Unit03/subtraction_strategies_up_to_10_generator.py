"""
Subtraction Strategies Up to 10 Generator - Grade 1 Unit 3\nGenerates subtraction strategy problems up to 10
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class SubtractionStrategiesUpTo10Generator:
    """Generates subtraction strategies up to 10 problems."""

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
        a = random.randint(3, 7)
        b = random.randint(1, a)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"count back from {a}"])

def main():
    generator = SubtractionStrategiesUpTo10Generator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")

if __name__ == '__main__':
    main()
