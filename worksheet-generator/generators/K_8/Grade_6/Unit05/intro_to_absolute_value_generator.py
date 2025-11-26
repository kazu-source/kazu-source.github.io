"""
Intro to Absolute Value Generator - Grade 6 Unit 5
Generates problems introducing absolute value
Example: What is |−5|?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToAbsoluteValueGenerator:
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
        num = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        latex = f"\\text{{Evaluate: }} |{num}|"
        solution = str(abs(num))
        return Equation(latex=latex, solution=solution, steps=[f"|{num}| = {abs(num)}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = round(random.uniform(-10, 10), 1)
        latex = f"\\text{{Evaluate: }} |{num}|"
        solution = str(abs(num))
        return Equation(latex=latex, solution=solution, steps=[f"|{num}| = {abs(num)}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num1 = random.randint(-15, 15)
        num2 = random.randint(-15, 15)
        result = abs(num1) + abs(num2)
        latex = f"\\text{{Evaluate: }} |{num1}| + |{num2}|"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"|{num1}| + |{num2}| = {abs(num1)} + {abs(num2)} = {result}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num1 = random.randint(-10, -1)
        num2 = random.randint(1, 10)
        result = abs(num1 - num2)
        latex = f"\\text{{Evaluate: }} |{num1} - {num2}|"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"|{num1} - {num2}| = |{num1 - num2}| = {result}"], difficulty='challenge')


def main():
    generator = IntroToAbsoluteValueGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.capitalize()}:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
