"""
Recognizing Patterns Generator - Kindergarten Unit 3
Generates problems about recognizing simple patterns
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class RecognizingPatternsGenerator:
    """Generates recognizing patterns problems."""

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
        pattern = random.choice([
            ('A', 'B', 'A', 'B'),
            ('red', 'blue', 'red', 'blue'),
            ('○', '●', '○', '●')
        ])
        latex = f"\text{{Pattern: {pattern[0]}, {pattern[1]}, {pattern[2]}, {pattern[3]}, ___}}"
        solution = pattern[0]
        return Equation(latex=latex, solution=solution, steps=[f"pattern repeats: {pattern[0]}, {pattern[1]}"])

def main():
    generator = RecognizingPatternsGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
