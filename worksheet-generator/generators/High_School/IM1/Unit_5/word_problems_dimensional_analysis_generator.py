"""
Word Problems Dimensional Analysis Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WordProblemsDimensionalAnalysisGenerator:
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
        price_per_lb = random.randint(2, 8)
        pounds = random.randint(3, 10)
        total = price_per_lb * pounds

        latex = f"\\text{{Apples cost \\${price_per_lb} per pound. How much do {pounds} pounds cost?}}"
        solution = f"\\${total}"
        steps = [f"{pounds} \\text{{ lb}} × \\frac{{\\${price_per_lb}}}{{1 \\text{{ lb}}}}", f"= \\${total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        mph = random.randint(50, 70)
        hours = random.randint(3, 6)
        miles = mph * hours

        latex = f"\\text{{A car travels at {mph} mph for {hours} hours. How many miles does it travel?}}"
        solution = f"{miles} \\text{{ miles}}"
        steps = [f"{hours} \\text{{ hr}} × \\frac{{{mph} \\text{{ mi}}}}{{1 \\text{{ hr}}}}", f"= {miles} miles"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        rate = random.randint(12, 25)
        hours = random.randint(6, 10)
        days = random.randint(3, 7)
        total = rate * hours * days

        latex = f"\\text{{A worker earns \\${rate}/hour, works {hours} hours/day for {days} days. Total earnings?}}"
        solution = f"\\${total}"
        steps = [f"{days} \\text{{ days}} × \\frac{{{hours} \\text{{ hr}}}}{{1 \\text{{ day}}}} × \\frac{{\\${rate}}}{{1 \\text{{ hr}}}}", f"= {days} × {hours} × {rate}", f"= \\${total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        liters_per_min = random.randint(2, 6)
        hours = random.randint(2, 5)
        total_liters = liters_per_min * 60 * hours

        latex = f"\\text{{A pump fills {liters_per_min} liters/minute. How many liters in {hours} hours?}}"
        solution = f"{total_liters} \\text{{ liters}}"
        steps = [f"{hours} \\text{{ hr}} × \\frac{{60 \\text{{ min}}}}{{1 \\text{{ hr}}}} × \\frac{{{liters_per_min} \\text{{ L}}}}{{1 \\text{{ min}}}}", f"= {hours} × 60 × {liters_per_min}", f"= {total_liters} liters"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WordProblemsDimensionalAnalysisGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
