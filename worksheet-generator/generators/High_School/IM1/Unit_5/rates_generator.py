"""
Rates Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RatesGenerator:
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
        distance = random.randint(60, 200)
        time = random.randint(2, 8)
        rate = distance // time

        latex = f"\\text{{A car travels {distance} miles in {time} hours. What is the rate in mph?}}"
        solution = f"{rate} \\text{{ mph}}"
        steps = [f"Rate = Distance / Time", f"Rate = {distance} / {time}", f"Rate = {rate} mph"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        items = random.randint(80, 200)
        time = random.randint(4, 10)
        rate = items // time

        latex = f"\\text{{A factory produces {items} items in {time} hours. What is the rate per hour?}}"
        solution = f"{rate} \\text{{ items/hour}}"
        steps = [f"Rate = Items / Time", f"Rate = {items} / {time}", f"Rate = {rate} items per hour"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        cost = random.randint(15, 40)
        items = random.randint(3, 8)
        rate = cost / items

        latex = f"\\text{{If {items} notebooks cost \\${cost}, what is the unit price per notebook?}}"
        solution = f"\\${rate:.2f} \\text{{ per notebook}}"
        steps = [f"Unit price = Total cost / Number of items", f"Unit price = {cost} / {items}", f"Unit price = \\${rate:.2f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        rate = random.randint(50, 80)
        time = random.randint(3, 7)
        distance = rate * time

        latex = f"\\text{{If a train travels at {rate} mph for {time} hours, how far does it go?}}"
        solution = f"{distance} \\text{{ miles}}"
        steps = [f"Distance = Rate × Time", f"Distance = {rate} × {time}", f"Distance = {distance} miles"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = RatesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
