"""
Properties of Numbers Generator - Grade 6 Unit 6
Generates problems on commutative, associative, and distributive properties
Example: Which property: 3 + 5 = 5 + 3?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PropertiesOfNumbersGenerator:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problems.append(self._generate_problem(difficulty))
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
        a, b = random.randint(2, 9), random.randint(2, 9)
        latex = f"\\text{{Which property: }} {a} + {b} = {b} + {a}"
        solution = "Commutative Property of Addition"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b = random.randint(2, 9), random.randint(2, 9)
        latex = f"\\text{{Which property: }} {a} \\times {b} = {b} \\times {a}"
        solution = "Commutative Property of Multiplication"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a, b, c = random.randint(2, 6), random.randint(2, 6), random.randint(2, 6)
        latex = f"\\text{{Which property: }} ({a} + {b}) + {c} = {a} + ({b} + {c})"
        solution = "Associative Property of Addition"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a, b, c = random.randint(2, 6), random.randint(2, 6), random.randint(2, 6)
        latex = f"\\text{{Which property: }} {a} \\times ({b} + {c}) = {a} \\times {b} + {a} \\times {c}"
        solution = "Distributive Property"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


def main():
    generator = PropertiesOfNumbersGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
