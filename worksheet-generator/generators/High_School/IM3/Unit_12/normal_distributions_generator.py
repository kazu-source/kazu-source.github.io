"""
Normal Distributions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class NormalDistributionsGenerator:
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
        # Empirical rule
        latex = "\\text{In a normal distribution, what percent of data is within 1 standard deviation?}"
        solution = "68%"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Calculate z-score
        mean = random.randint(50, 100)
        sd = random.randint(5, 15)
        x = mean + random.randint(-2, 2) * sd

        latex = f"\\text{{Find z-score: }} \\mu = {mean}, \\sigma = {sd}, x = {x}"
        solution = f"z = \\frac{{{x} - {mean}}}{{{sd}}} = {(x-mean)//sd}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Find percentile
        mean = random.randint(500, 600)
        sd = random.randint(50, 100)

        latex = f"\\text{{SAT scores: }} \\mu = {mean}, \\sigma = {sd}\\text{{. What score is 84th percentile?}}"
        solution = f"\\text{{Use z-table: z }} \\approx 1, x = {mean} + {sd} = {mean + sd}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Application with two values
        mean = random.randint(100, 120)
        sd = random.randint(10, 20)
        lower = mean - sd
        upper = mean + sd

        latex = f"\\text{{IQ: }} \\mu = {mean}, \\sigma = {sd}\\text{{. P({lower} < X < {upper})?}}"
        solution = "68% (within 1 standard deviation)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = NormalDistributionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
