"""
Solving Exponential Equations Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingExponentialEquationsGenerator:
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
                base = random.randint(2, 5)
                exp = random.randint(2, 4)
                result = base ** exp
                latex = f"{base}^x = {result}"
                solution = f"x = {exp}"
                steps = [f"Recognize {result} = {base}^{exp}", f"Therefore x = {exp}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                base = random.randint(2, 4)
                exp = random.randint(2, 5)
                latex = f"{base}^{{2x}} = {base}^{{{exp}}}"
                solution = f"x = {exp/2}"
                steps = [f"Same base, set exponents equal", f"2x = {exp}", f"x = {exp/2}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                base = random.randint(2, 4)
                a = random.randint(2, 5)
                b = random.randint(1, 4)
                exp = a + b
                latex = f"{base}^{{x + {b}}} = {base}^{{{exp}}}"
                solution = f"x = {a}"
                steps = [f"Set exponents equal", f"x + {b} = {exp}", f"x = {exp} - {b} = {a}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                base1 = random.randint(2, 3)
                base2 = base1 ** 2
                exp = random.randint(3, 6)
                latex = f"{base2}^x = {base1}^{{{exp}}}"
                solution = f"x = {exp/2}"
                steps = [f"Rewrite {base2} = {base1}^2", f"({base1}^2)^x = {base1}^{exp}", f"{base1}^{{2x}} = {base1}^{exp}", f"2x = {exp}, x = {exp/2}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingExponentialEquationsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
