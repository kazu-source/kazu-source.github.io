"""
Samples and Surveys Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SamplesSurveysGenerator:
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
        # Identify sampling method
        latex = "\\text{Identify sampling method: Every 10th student in alphabetical order}"
        solution = "Systematic sampling"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Identify bias
        latex = "\\text{A survey about school lunch is given only to football players. Identify bias.}"
        solution = "Selection bias - not representative of all students"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Sample size calculation
        pop = random.randint(500, 2000)
        margin = random.choice([3, 5])

        latex = f"\\text{{Population: {pop}, desired margin: {margin}%. Discuss sample size needed.}}"
        solution = f"\\text{{Larger sample reduces margin of error}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Design survey
        latex = "\\text{Design a survey to determine favorite lunch item among 1000 students.}"
        solution = "Random sample, stratified by grade level, unbiased questions"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SamplesSurveysGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
