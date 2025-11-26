"""Analyzing Relationships Between Variables Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class AnalyzingRelationshipsBetweenVariablesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        rate = random.randint(5, 15)
        time = random.randint(2, 8)
        distance = rate * time
        latex = f"\\text{{If speed is }}{rate}\\text{{ mph for }}{time}\\text{{ hours, distance?}}"
        return Equation(latex=latex, solution=f"{distance} miles", steps=[f"{rate} \\times {time} = {distance}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        cost_per = random.randint(3, 10)
        latex = f"\\text{{Cost = }}\\${cost_per} \\times n\\text{{. If }} n = 5\\text{{, cost?}}"
        return Equation(latex=latex, solution=f"\\${cost_per*5}", steps=[f"{cost_per} \\times 5 = {cost_per*5}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        rate = random.randint(8, 15)
        hours = random.randint(5, 10)
        pay = rate * hours
        latex = f"\\text{{Pay = }}\\${rate}/\\text{{hr}} \\times h\\text{{. For }}{hours}\\text{{ hrs?}}"
        return Equation(latex=latex, solution=f"\\${pay}", steps=[f"{rate} \\times {hours} = {pay}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        base, rate = random.randint(20, 50), random.randint(10, 20)
        weeks = random.randint(3, 8)
        total = base + rate * weeks
        latex = f"\\text{{Savings = }}\\${base} + \\${rate}/\\text{{week}} \\times w\\text{{. After }}{weeks}\\text{{ weeks?}}"
        return Equation(latex=latex, solution=f"\\${total}", steps=[f"{base} + {rate} \\times {weeks} = {total}"], difficulty='challenge')

def main():
    gen = AnalyzingRelationshipsBetweenVariablesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
