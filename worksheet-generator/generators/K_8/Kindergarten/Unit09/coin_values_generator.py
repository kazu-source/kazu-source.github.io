"""
Coin Values Generator - Kindergarten Unit 9
Generates problems about coin values and simple counting
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class CoinValuesGenerator:
    """Generates coin values problems."""

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
        num_pennies = random.randint(1, 5)
        latex = f"\text{{How many cents in {num_pennies} penn{'y' if num_pennies == 1 else 'ies'}?}}"
        solution = f"{num_pennies} cents"
        return Equation(latex=latex, solution=solution, steps=[f"{num_pennies} × 1 = {num_pennies}"])

def main():
    generator = CoinValuesGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
