"""
Addition Word Problems Up To 10 Generator - Grade 1 Unit02
Generates addition word problems up to 10 problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AdditionWordProblemsUpTo10Generator:
    """Generates addition word problems up to 10 problems."""

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
        a = random.randint(1, 4)
        b = random.randint(1, 5)
        total = a + b
        item = random.choice(["apples", "toys", "books"])
        latex = f"\\text{{{{Tom has {a} {item}. He gets {b} more. How many now?}}}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 8)
        total = a + b
        if total > 10:
            b = 10 - a
            total = a + b
        latex = f"\\text{{{{Sara has {a} crayons. Ben has {b} crayons. How many total?}}}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {total}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        total = random.randint(7, 10)
        a = random.randint(3, total - 2)
        b = total - a
        latex = f"\\text{{{{There are {total} birds. {a} are red. How many are blue?}}}}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"{total} - {a} = {b}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c = random.randint(1, 3)
        total = a + b + c
        if total > 10:
            c = 1
            total = a + b + c
        latex = f"\\text{{{{Ann has {a} pencils, Bob has {b}, and Cal has {c}. How many total?}}}}"
        solution = str(total)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} + {c} = {total}"], difficulty='challenge')


def main():
    generator = AdditionWordProblemsUpTo10Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
