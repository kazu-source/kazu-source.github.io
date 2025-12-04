"""
Evaluating Exponents and Radicals Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EvaluatingExponentsRadicalsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
                num = random.choice([4, 9, 16, 25, 36])
                latex = f"\\sqrt{{{num}}}"
                solution = f"{int(num ** 0.5)}"
                steps = [f"Find square root of {num}", f"Answer: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                num = random.choice([8, 27, 64, 125])
                latex = f"\\sqrt[3]{{{num}}}"
                solution = f"{int(round(num ** (1/3)))}"
                steps = [f"Find cube root of {num}", f"Answer: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                base = random.randint(2, 5)
                num = base ** random.randint(2, 4)
                latex = f"{num}^{{1/2}}"
                solution = f"{int(num ** 0.5)}"
                steps = [f"Fractional exponent 1/2 means square root", f"\\sqrt{{{num}}} = {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                base = random.randint(2, 4)
                exp = random.randint(2, 3)
                num = base ** (2 * exp)
                latex = f"{num}^{{2/{2*exp}}}"
                solution = f"{base}^2 = {base*base}"
                steps = [f"Simplify exponent: 2/{2*exp} = 1/{exp}", f"{num}^{{1/{exp}}} = {base}", f"But we have ({base})^2 = {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EvaluatingExponentsRadicalsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
