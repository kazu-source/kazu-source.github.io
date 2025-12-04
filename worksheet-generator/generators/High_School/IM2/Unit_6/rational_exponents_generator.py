"""
Rational Exponents Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RationalExponentsGenerator:
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
        base = random.choice([4, 8, 9, 16, 25, 27])
        n = 2 if base in [4, 9, 16, 25] else 3
        result = int(base ** (1/n))
        latex = f"{base}^{{1/{n}}}"
        solution = f"{result}"
        steps = [f"{base}^{{1/{n}}} = \\sqrt[{n}]{{{base}}} = {result}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        base = random.choice([8, 16, 27, 32])
        nums = {8: (2,3,4), 16: (2,4,2), 27: (3,3,9), 32: (2,5,4)}
        result, n, power = nums[base]
        latex = f"{base}^{{2/{n}}}"
        solution = f"{result**2}"
        steps = [f"{base}^{{2/{n}}} = (\\sqrt[{n}]{{{base}}})^2 = {result}^2 = {result**2}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 6)
        m = random.randint(2, 5)
        n = random.randint(2, 4)
        latex = f"x^{{{m}/{n}}}"
        solution = f"\\sqrt[{n}]{{x^{m}}}"
        steps = [f"x^{{{m}/{n}}} = \\sqrt[{n}]{{x^{m}}} = (x^{m})^{{1/{n}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        m = random.randint(1, 4)
        n = random.randint(2, 4)
        latex = f"({a}x)^{{{m}/{n}}}"
        solution = f"\\sqrt[{n}]{{({a}x)^{m}}}"
        steps = [f"({a}x)^{{{m}/{n}}} = \\sqrt[{n}]{{({a}x)^{m}}} = \\sqrt[{n}]{{{a**m}x^{m}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = RationalExponentsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
