"""
Coin Recognition Generator - Kindergarten Unit 9
Generates problems about recognizing coins (penny, nickel, dime, quarter)
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class CoinRecognitionGenerator:
    """Generates coin recognition problems."""

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
        coin = random.choice(['penny', 'nickel', 'dime', 'quarter'])
        latex = f"\text{{What coin is this? (shows a {coin})}}"
        solution = coin
        return Equation(latex=latex, solution=solution, steps=[coin])

def main():
    generator = CoinRecognitionGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
