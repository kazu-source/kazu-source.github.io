"""
Classifying Objects Generator - Kindergarten Unit 8
Generates problems about classifying objects into categories
Note: K-2 generators do not use difficulty levels.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ClassifyingObjectsGenerator:
    """Generates classifying objects problems."""

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
        category = random.choice(['animals', 'toys', 'food'])
        item = random.choice(['dog', 'ball', 'apple'])
        latex = f"\text{{Is a {item} a type of {category}?}}"
        solution = "Yes" if (category == 'animals' and item == 'dog') or (category == 'toys' and item == 'ball') or (category == 'food' and item == 'apple') else "No"
        return Equation(latex=latex, solution=solution, steps=[solution])

def main():
    generator = ClassifyingObjectsGenerator()
    print("Problems:")
    for problem in generator.generate_worksheet(num_problems=3):
        print(f"  {problem.latex} = {problem.solution}")
    

if __name__ == '__main__':
    main()
