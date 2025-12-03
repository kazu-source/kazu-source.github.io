"""
Comparing Lengths Generator - Kindergarten Unit 9
Generates problems about comparing lengths
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ComparingLengthsGenerator:
    """Generates comparing lengths problems."""

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
        obj1 = random.choice(['pencil', 'stick', 'ribbon'])
        obj2 = random.choice(['crayon', 'twig', 'string'])
        latex = f"\text{{Which is longer: a {obj1} or a {obj2}?}}"
        solution = obj1
        return Equation(latex=latex, solution=solution, steps=["compare lengths"])

def main():
    generator = ComparingLengthsGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
