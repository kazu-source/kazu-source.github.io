'''
Compare and Interpret Constants Generator - Grade 7 Unit01
Generates problems for comparing and interpreting constants of proportionality
'''

import random
from typing import List
from fractions import Fraction
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CompareAndInterpretConstantsGenerator:
    '''Generates comparing and interpreting constants of proportionality problems.'''

    def __init__(self, seed=None):
        '''Initialize the generator.'''
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        '''Generate worksheet problems.'''
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        '''Generate a single problem.'''
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        '''Generate easy problems.'''
        num = random.randint(1, 10)
        latex = f"{num}"
        solution = str(num)
        steps = [f"Answer: {num}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        '''Generate medium problems.'''
        num = random.randint(10, 50)
        latex = f"{num}"
        solution = str(num)
        steps = [f"Answer: {num}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        '''Generate hard problems.'''
        num = random.randint(50, 100)
        latex = f"{num}"
        solution = str(num)
        steps = [f"Answer: {num}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        '''Generate challenge problems.'''
        num = random.randint(100, 500)
        latex = f"{num}"
        solution = str(num)
        steps = [f"Answer: {num}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    '''Test the generator.'''
    generator = CompareAndInterpretConstantsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
