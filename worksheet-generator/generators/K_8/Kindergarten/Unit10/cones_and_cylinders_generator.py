"""
Cones and Cylinders Generator - Kindergarten Unit 10
Generates problems about identifying 3D shapes: cones and cylinders
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ConesAndCylindersGenerator:
    """Generates cones and cylinders problems."""

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
        shape = random.choice(['cone', 'cylinder'])
        example = random.choice(['ice cream cone', 'party hat']) if shape == 'cone' else random.choice(['can', 'tube'])
        latex = f"\text{{Is a {example} shaped like a cone or cylinder?}}"
        solution = shape
        return Equation(latex=latex, solution=solution, steps=[shape])

def main():
    generator = ConesAndCylindersGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
