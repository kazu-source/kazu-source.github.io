"""
Reading Clocks Introduction Generator - Kindergarten Unit 7
Generates basic clock reading problems (hour only)
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ReadingClocksIntroductionGenerator:
    """Generates introduction to clock reading problems."""

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
        hour = random.randint(1, 12)
        latex = f"\text{{The clock shows {hour} o'clock}}"
        solution = f"{hour} o'clock"
        return Equation(latex=latex, solution=solution, steps=[f"{hour}:00"])

def main():
    generator = ReadingClocksIntroductionGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
