"""
Reading Simple Graphs Generator - Kindergarten Unit 8
Generates problems about reading picture graphs and simple bar graphs
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ReadingSimpleGraphsGenerator:
    """Generates reading simple graphs problems."""

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
        item = random.choice(['apples', 'stars', 'hearts'])
        count = random.randint(2, 5)
        latex = f"\\text{{The graph shows {count} {item}. How many {item}?}}"
        solution = str(count)
        return Equation(latex=latex, solution=solution, steps=[f"{count}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        item1 = random.choice(['red', 'blue', 'green'])
        item2 = random.choice(['yellow', 'purple', 'orange'])
        count1 = random.randint(3, 6)
        count2 = random.randint(2, 5)
        latex = f"\\text{{Graph: {item1} has {count1}, {item2} has {count2}. Which has more?}}"
        solution = item1 if count1 > count2 else item2
        return Equation(latex=latex, solution=solution, steps=["compare counts"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        items = ['cats', 'dogs', 'birds']
        counts = [random.randint(2, 5) for _ in range(3)]
        total = sum(counts)
        latex = f"\\text{{How many animals total? Cats: {counts[0]}, Dogs: {counts[1]}, Birds: {counts[2]}}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{counts[0]} + {counts[1]} + {counts[2]} = {total}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        item = random.choice(['flowers', 'stars', 'toys'])
        count1 = random.randint(3, 6)
        count2 = random.randint(2, count1 - 1)
        diff = count1 - count2
        latex = f"\\text{{Red {item}: {count1}, Blue {item}: {count2}. How many more red?}}"
        solution = str(diff)
        return Equation(latex=latex, solution=solution, steps=[f"{count1} - {count2} = {diff}"], difficulty='challenge')


def main():
    generator = ReadingSimpleGraphsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
