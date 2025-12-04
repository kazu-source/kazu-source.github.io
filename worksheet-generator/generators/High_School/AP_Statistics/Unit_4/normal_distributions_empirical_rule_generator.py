"""
Normal Distributions and Empirical Rule Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class NormalDistributionsEmpiricalRuleGenerator:
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
        mean, std = 100, 15
        question = f"Normal dist: mean={mean}, SD={std}. About what % within 1 SD of mean?"
        solution = "Approximately 68%"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        mean, std = 50, 10
        lower, upper = mean - 2*std, mean + 2*std
        question = f"Normal: mean={mean}, SD={std}. Find interval containing about 95% of data"
        solution = f"[{lower}, {upper}]"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        mean, std = 500, 100
        question = f"SAT: mean={mean}, SD={std}. What % between 300 and 700?"
        lower_z, upper_z = (300-500)/100, (700-500)/100
        solution = "Between -2 and +2 SDs, approximately 95%"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "Normal distribution. 16% of data above what z-score?"
        solution = "z = 1 (84th percentile, since 68% within 1 SD, 16% above)"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = NormalDistributionsEmpiricalRuleGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
