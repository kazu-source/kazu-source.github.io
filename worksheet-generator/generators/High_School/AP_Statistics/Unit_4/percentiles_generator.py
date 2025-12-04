"""
Percentiles Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PercentilesGenerator:
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
        score = random.randint(70, 90)
        percentile = random.randint(60, 85)
        question = f"\\text{{A score of {score} is at the {percentile}th percentile.}}\\\\"\
                   f"\\text{{What does this mean?}}"
        solution = f"{percentile}% of scores are below {score}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        total = 200
        percentile = 75
        position = int(total * percentile / 100)
        question = f"\\text{{In a class of {total} students, you're at 75th percentile.}}\\\\"\
                   f"\\text{{How many students scored below you?}}"
        solution = f"Approximately {position} students"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        data = sorted([random.randint(60, 100) for _ in range(20)])
        percentile = 80
        position = int(len(data) * percentile / 100)
        value = data[position-1] if position > 0 else data[0]
        question = f"\\text{{Find the 80th percentile of:}}\\\\"\
                   f"\\text{{{', '.join(map(str, data))}}}"
        solution = f"80th percentile is approximately {value}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = f"\\text{{Explain the difference between:}}\\\\"\
                   f"\\text{{(a) 90th percentile}}\\\\"\
                   f"\\text{{(b) Top 10%}}\\\\"\
                   f"\\text{{(c) Are they the same? Why or why not?}}"
        solution = "(a) 90th percentile: 90% score below, (b) Top 10%: upper 10% of distribution, "\
                   "(c) Yes, equivalent: 90th percentile = top 10%"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = PercentilesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
