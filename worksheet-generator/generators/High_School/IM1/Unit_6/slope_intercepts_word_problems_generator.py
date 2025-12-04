"""
Slope Intercepts Word Problems Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SlopeInterceptsWordProblemsGenerator:
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
        rate = random.randint(5, 15)
        initial = random.randint(20, 50)

        latex = f"\\text{{A phone plan costs \\${initial} plus \\${rate}/month. What is the y-intercept?}}"
        solution = f"{initial}"
        steps = ["Y-intercept is the starting value", f"Initial cost = \\${initial}", f"Answer: {initial}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        rate = random.randint(3, 12)
        initial = random.randint(15, 40)

        latex = f"\\text{{A tank has {initial} gallons and fills at {rate} gal/min. Write the equation.}}"
        solution = f"y = {rate}x + {initial}"
        steps = ["Slope = rate of change = {rate}", f"Y-intercept = initial amount = {initial}", f"y = {rate}x + {initial}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        rate = random.randint(40, 80)
        initial = random.randint(100, 300)
        time = random.randint(3, 8)
        total = rate * time + initial

        latex = f"\\text{{A car rental is \\${initial} + \\${rate}/day. Find cost for {time} days.}}"
        solution = f"\\${total}"
        steps = [f"Equation: y = {rate}x + {initial}", f"Substitute x = {time}", f"y = {rate}({time}) + {initial} = {total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        rate = random.randint(20, 50)
        total = random.randint(300, 600)
        initial = random.randint(50, 150)
        days = (total - initial) / rate

        latex = f"\\text{{A savings account has \\${initial} and saves \\${rate}/week. When will it reach \\${total}?}}"
        solution = f"{days:.1f} \\text{{ weeks}}"
        steps = [f"Equation: {total} = {rate}x + {initial}", f"Solve: {rate}x = {total - initial}", f"x = {total - initial}/{rate} = {days:.1f} weeks"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SlopeInterceptsWordProblemsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
