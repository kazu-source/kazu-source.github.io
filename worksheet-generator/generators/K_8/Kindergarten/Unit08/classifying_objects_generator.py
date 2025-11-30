"""
Classifying Objects Generator - Kindergarten Unit 8
Generates problems about classifying objects into categories
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

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        category = random.choice(['animals', 'toys', 'food'])
        item = random.choice(['dog', 'ball', 'apple'])
        latex = f"\\text{{Is a {item} a type of {category}?}}"
        solution = "Yes" if (category == 'animals' and item == 'dog') or (category == 'toys' and item == 'ball') or (category == 'food' and item == 'apple') else "No"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        categories = {
            'fruits': ['apple', 'banana', 'orange'],
            'shapes': ['circle', 'square', 'triangle'],
            'colors': ['red', 'blue', 'green']
        }
        category = random.choice(list(categories.keys()))
        item = random.choice(categories[category])
        latex = f"\\text{{A {item} belongs to which group?}}"
        solution = category
        return Equation(latex=latex, solution=solution, steps=[category], difficulty='medium')

    def _generate_hard(self) -> Equation:
        obj1 = random.choice(['cat', 'dog', 'bird'])
        obj2 = random.choice(['car', 'truck', 'bike'])
        latex = f"\\text{{What do {obj1} and dog have in common?}}"
        solution = "animals"
        return Equation(latex=latex, solution=solution, steps=["both are animals"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        items = ['apple', 'car', 'banana', 'truck']
        latex = f"\\text{{Group these items: {', '.join(items)}}}"
        solution = "fruits: apple, banana; vehicles: car, truck"
        return Equation(latex=latex, solution=solution, steps=["classify into groups"], difficulty='challenge')


def main():
    generator = ClassifyingObjectsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
