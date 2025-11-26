'''
Subtracting Negatives Intro Generator - Grade 7 Unit03
'''

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToSubtractingNegativeNumbersGenerator:
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
        num = random.randint(1, 10)
        return Equation(latex=str(num), solution=str(num), steps=["Step 1"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(10, 50)
        return Equation(latex=str(num), solution=str(num), steps=["Step 1"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(50, 100)
        return Equation(latex=str(num), solution=str(num), steps=["Step 1"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num = random.randint(100, 500)
        return Equation(latex=str(num), solution=str(num), steps=["Step 1"], difficulty='challenge')


def main():
    generator = IntroToSubtractingNegativeNumbersGenerator()
    print("Testing generator")


if __name__ == '__main__':
    main()
