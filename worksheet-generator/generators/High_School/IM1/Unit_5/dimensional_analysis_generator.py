"""
Dimensional Analysis Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DimensionalAnalysisGenerator:
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
        feet = random.randint(12, 96)
        inches = feet * 12

        latex = f"\\text{{Convert {feet} feet to inches (12 inches = 1 foot)}}"
        solution = f"{inches} \\text{{ inches}}"
        steps = [f"{feet} \\text{{ ft}} × \\frac{{12 \\text{{ in}}}}{{1 \\text{{ ft}}}}", f"= {inches} inches"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        hours = random.randint(2, 6)
        minutes = hours * 60

        latex = f"\\text{{Convert {hours} hours to minutes (60 minutes = 1 hour)}}"
        solution = f"{minutes} \\text{{ minutes}}"
        steps = [f"{hours} \\text{{ hr}} × \\frac{{60 \\text{{ min}}}}{{1 \\text{{ hr}}}}", f"= {minutes} minutes"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        days = random.randint(2, 5)
        hours = days * 24
        minutes = hours * 60

        latex = f"\\text{{Convert {days} days to minutes}}"
        solution = f"{minutes} \\text{{ minutes}}"
        steps = [f"{days} \\text{{ days}} × \\frac{{24 \\text{{ hr}}}}{{1 \\text{{ day}}}} × \\frac{{60 \\text{{ min}}}}{{1 \\text{{ hr}}}}", f"= {days} × 24 × 60", f"= {minutes} minutes"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        miles = random.randint(2, 5)
        feet = miles * 5280

        latex = f"\\text{{Convert {miles} miles to feet (1 mile = 5,280 feet)}}"
        solution = f"{feet:,} \\text{{ feet}}"
        steps = [f"{miles} \\text{{ mi}} × \\frac{{5280 \\text{{ ft}}}}{{1 \\text{{ mi}}}}", f"= {feet:,} feet"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = DimensionalAnalysisGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
