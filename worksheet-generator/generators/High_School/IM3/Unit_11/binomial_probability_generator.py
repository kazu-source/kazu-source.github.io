"""
Binomial Probability Generator
"""
import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class BinomialProbabilityGenerator:
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
        # Identify binomial situation
        latex = "\\text{Is flipping a coin 10 times and counting heads a binomial experiment?}"
        solution = "Yes - fixed trials, two outcomes, independent, constant probability"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Calculate binomial probability
        n = random.randint(5, 10)
        k = random.randint(0, n)
        p = random.choice([0.5, 0.3, 0.6])

        latex = f"\\text{{Find }} P(X = {k}) \\text{{ for }} n = {n}, p = {p}"
        solution = f"\\binom{{{n}}}{{{k}}} ({p})^{{{k}}} (1-{p})^{{{n-k}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Expected value and variance
        n = random.randint(10, 20)
        p = random.choice([0.3, 0.4, 0.6, 0.7])

        latex = f"\\text{{For binomial with }} n = {n}, p = {p}\\text{{, find mean and standard deviation}}"
        solution = f"\\mu = {n*p}, \\sigma = \\sqrt{{{n*p*(1-p)}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Application problem
        n = random.randint(15, 25)
        p = random.choice([0.2, 0.3, 0.4])
        k = random.randint(5, 10)

        latex = f"\\text{{If {int(p*100)}% pass test, find P(at least {k} of {n} pass)}}"
        solution = f"P(X \\geq {k}) = 1 - P(X < {k})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = BinomialProbabilityGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
