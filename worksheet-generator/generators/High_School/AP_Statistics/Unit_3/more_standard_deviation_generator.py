"""
More on Standard Deviation Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MoreStandardDeviationGenerator:
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
        data = [10, 10, 10, 10, 10]
        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\\\text{{What is the standard deviation?}}"
        solution = "s = 0 (no variability)"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        data1 = [8, 9, 10, 11, 12]
        data2 = [2, 6, 10, 14, 18]
        question = f"\\text{{Dataset A: {', '.join(map(str, data1))}}}\\\\"\
                   f"\\text{{Dataset B: {', '.join(map(str, data2))}}}\\\\"\
                   f"\\text{{Both have mean 10. Which has larger std dev?}}"
        solution = "Dataset B (more spread from mean)"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        data = [4, 6, 8, 10, 12]
        mean = sum(data) / len(data)
        deviations = [(x - mean)**2 for x in data]
        variance = sum(deviations) / (len(data) - 1)
        std = round(variance ** 0.5, 2)
        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{Calculate standard deviation step-by-step.}}"
        solution = f"Mean = {mean}, Deviations squared: {deviations}, Variance = {variance}, s = {std}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = f"\\text{{Two datasets have same mean but different std devs.}}\\\\"\
                   f"\\text{{Create example datasets and explain what std dev measures.}}"
        solution = "Example: A=[5,5,5] s=0, B=[3,5,7] s=2. Std dev measures average distance from mean; larger s means more variability"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MoreStandardDeviationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
