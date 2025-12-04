"""
Word Problems Slope Intercept Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WordProblemsSlopeInterceptGenerator:
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
        rate = random.randint(30, 70)
        initial = random.randint(50, 200)

        latex = f"\\text{{A plumber charges \\${initial} plus \\${rate}/hour. Write the equation.}}"
        solution = f"y = {rate}x + {initial}"
        steps = [f"Rate (slope) = {rate}", f"Initial fee (y-intercept) = {initial}", f"y = {rate}x + {initial}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        rate = random.randint(10, 25)
        initial = random.randint(100, 300)
        hours = random.randint(3, 8)
        total = rate * hours + initial

        latex = f"\\text{{Gym membership: \\${initial} signup + \\${rate}/month. Cost after {hours} months?}}"
        solution = f"\\${total}"
        steps = [f"y = {rate}x + {initial}", f"x = {hours}", f"y = {rate}({hours}) + {initial} = {total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        rate = random.randint(5, 15)
        initial = random.randint(20, 80)
        total = random.randint(150, 300)
        time = (total - initial) / rate

        latex = f"\\text{{A candle is {initial}cm tall, burns {rate}cm/hr. When is it {total}cm? (Error: grows)}}"
        # Fix the problem - candle should get shorter
        initial = random.randint(200, 300)
        total = random.randint(50, 150)
        time = (initial - total) / rate
        latex = f"\\text{{A candle is {initial}cm tall, burns {rate}cm/hr. When is it {total}cm?}}"
        solution = f"{time:.1f} \\text{{ hours}}"
        steps = [f"Height: y = {initial} - {rate}x", f"{total} = {initial} - {rate}x", f"{rate}x = {initial - total}", f"x = {time:.1f} hours"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        rate1 = random.randint(40, 70)
        rate2 = random.randint(30, 60)
        fee1 = random.randint(20, 60)
        fee2 = random.randint(40, 100)

        if rate1 == rate2:
            rate2 += 10

        hours = (fee2 - fee1) / (rate1 - rate2)

        latex = f"\\text{{Plumber A: \\${fee1} + \\${rate1}/hr. Plumber B: \\${fee2} + \\${rate2}/hr. When equal?}}"
        solution = f"{hours:.1f} \\text{{ hours}}"
        steps = [f"A: y = {rate1}x + {fee1}", f"B: y = {rate2}x + {fee2}", f"Set equal: {rate1}x + {fee1} = {rate2}x + {fee2}", f"x = {hours:.1f} hours"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WordProblemsSlopeInterceptGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
