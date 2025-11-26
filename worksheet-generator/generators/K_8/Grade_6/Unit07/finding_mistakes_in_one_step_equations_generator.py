"""Finding Mistakes in One Step Equations Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class FindingMistakesInOneStepEquationsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, b = random.randint(3, 12), random.randint(2, 8)
        wrong = x + b
        latex = f"\\text{{Student solved }} x + {b} = {x+b} \\text{{ and got }} x = {wrong}\\text{{. Find the error.}}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"Error: should subtract {b}, correct answer: x = {x}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x, a = random.randint(2, 10), random.randint(2, 6)
        wrong = a * x
        latex = f"\\text{{Student solved }} {a}x = {a*x} \\text{{ and got }} x = {wrong}\\text{{. Find the error.}}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"Error: should divide by {a}, correct answer: x = {x}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, b = random.randint(8, 20), random.randint(3, 10)
        wrong = x - b * 2
        latex = f"\\text{{Student solved }} x - {b} = {x-b} \\text{{ and got }} x = {wrong}\\text{{. What's wrong?}}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"Error: should add {b}, correct answer: x = {x}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        a, quotient = random.randint(3, 8), random.randint(4, 10)
        x = a * quotient
        wrong = quotient * a * 2
        latex = f"\\text{{Student solved }} x/{a} = {quotient} \\text{{ and got }} x = {wrong}\\text{{. Correct it.}}"
        return Equation(latex=latex, solution=f"x = {x}", steps=[f"Error: multiplied incorrectly, correct answer: x = {x}"], difficulty='challenge')

def main():
    gen = FindingMistakesInOneStepEquationsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
