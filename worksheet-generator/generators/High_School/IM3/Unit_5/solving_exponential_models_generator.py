"""
Solving Exponential Models Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingExponentialModelsGenerator:
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
        # Simple growth model
        initial = random.randint(100, 500)
        rate = random.choice([1.05, 1.1, 1.15, 1.2])
        target = initial * 2

        latex = f"\\text{{When does }} P = {initial}({rate})^t \\text{{ reach }} {target}?"
        solution = f"t = \\frac{{\\ln({target}/{initial})}}{{\\ln({rate})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Decay model
        initial = random.randint(500, 1000)
        rate = random.choice([0.9, 0.85, 0.8, 0.75])
        target = initial // 2

        latex = f"\\text{{When does }} P = {initial}({rate})^t \\text{{ reach }} {target}?"
        solution = f"t = \\frac{{\\ln({target}/{initial})}}{{\\ln({rate})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Compound interest
        principal = random.randint(1000, 5000)
        rate = random.choice([0.04, 0.05, 0.06, 0.07])
        target = principal * 2

        latex = f"\\text{{When does }} A = {principal}(1+{rate})^t \\text{{ reach }} {target}?"
        solution = f"t = \\frac{{\\ln(2)}}{{\\ln(1+{rate})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Population growth with continuous compounding
        initial = random.randint(10000, 50000)
        rate = random.choice([0.02, 0.03, 0.04])
        target = initial * random.choice([2, 3])

        latex = f"\\text{{When does }} P = {initial}e^{{{rate}t}} \\text{{ reach }} {target}?"
        solution = f"t = \\frac{{\\ln({target}/{initial})}}{{{rate}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SolvingExponentialModelsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
