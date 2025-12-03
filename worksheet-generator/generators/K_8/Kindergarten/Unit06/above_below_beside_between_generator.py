"""
Above Below Beside Between Generator - Kindergarten Unit 6
Generates problems about positional words
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class AboveBelowBesideBetweenGenerator:
    """Generates above, below, beside, between problems."""

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
        position = random.choice(['above', 'below'])
        obj1 = random.choice(['bird', 'cloud', 'sun'])
        obj2 = random.choice(['tree', 'house', 'car'])
        latex = f"\text{{The {obj1} is {position} the {obj2}}}"
        solution = position
        return Equation(latex=latex, solution=solution, steps=[f"{obj1} is {position}"])

def main():
    generator = AboveBelowBesideBetweenGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
