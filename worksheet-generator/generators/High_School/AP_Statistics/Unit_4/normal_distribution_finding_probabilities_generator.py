"""
Normal Distribution - Finding Probabilities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class NormalDistributionFindingProbabilitiesGenerator:
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
        question = "Standard normal. P(z < 1)?"
        solution = "Approximately 0.8413 or 84.13%"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        question = "Standard normal. P(z > -1.5)?"
        solution = "Approximately 0.9332 or 93.32%"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = "Normal: mean=70, SD=8. P(X < 78)?"
        z = (78-70)/8
        question = f"Z = {z}. P(z < 1)?"
        solution = "Approximately 0.8413"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "Normal: mean=100, SD=15. Find P(85 < X < 115)"
        solution = "P(-1 < z < 1) = 0.68"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = NormalDistributionFindingProbabilitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
