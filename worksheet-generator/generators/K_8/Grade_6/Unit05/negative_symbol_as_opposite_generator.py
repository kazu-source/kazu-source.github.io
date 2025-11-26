"""
Negative Symbol as Opposite Generator - Grade 6 Unit 5
Generates problems on understanding negative as opposite
Example: Evaluate -(-5)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class NegativeSymbolAsOppositeGenerator:
    """Generates negative symbol as opposite problems."""

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
        num = random.randint(1, 20)
        latex = f"\\text{{Evaluate: }} -(-{num})"
        solution = str(num)
        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"-(-{num}) = {num}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        num = random.randint(1, 25)
        if random.choice([True, False]):
            latex = f"\\text{{Evaluate: }} -({num})"
            solution = f"-{num}"
        else:
            latex = f"\\text{{Evaluate: }} -(-(-{num}))"
            solution = f"-{num}"
        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Result: }} {solution}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        num = random.randint(5, 30)
        layers = random.randint(4, 5)
        result = num if layers % 2 == 0 else -num
        neg_str = "-(" * layers + str(num) + ")" * layers
        latex = f"\\text{{Evaluate: }} {neg_str}"
        solution = str(result)
        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Result: }} {solution}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        a = random.randint(3, 12)
        b = random.randint(3, 12)
        result = -a + b
        latex = f"\\text{{Evaluate: }} -({a}) + {b}"
        solution = str(result)
        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"-({a}) = -{a}",
                f"-{a} + {b} = {result}"
            ],
            difficulty='challenge'
        )


def main():
    generator = NegativeSymbolAsOppositeGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
