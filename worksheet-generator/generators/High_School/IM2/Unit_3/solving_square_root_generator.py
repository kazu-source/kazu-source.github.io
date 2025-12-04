"""
Solving by Square Root Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation
import math

class SolvingSquareRootGenerator:
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
        perfect_square = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        sqrt_val = int(math.sqrt(perfect_square))
        latex = f"\\text{{Solve: }} x^2 = {perfect_square}"
        solution = f"x = \\pm {sqrt_val}"
        steps = [
            f"x² = {perfect_square}",
            f"Take square root of both sides",
            f"x = ±√{perfect_square}",
            f"x = ±{sqrt_val}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        perfect_square = random.choice([4, 9, 16, 25, 36, 49])
        sqrt_val = int(math.sqrt(perfect_square))
        total = a * perfect_square
        latex = f"\\text{{Solve: }} x^2 = {total}"
        solution = f"x = \\pm {a * sqrt_val}"
        steps = [
            f"x² = {total}",
            f"Take square root of both sides",
            f"x = ±√{total}",
            f"x = ±√({a**2}·{perfect_square})",
            f"x = ±{a}√{perfect_square}",
            f"x = ±{a * sqrt_val}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        h = random.randint(-5, 5)
        k = random.choice([4, 9, 16, 25])
        sqrt_k = int(math.sqrt(k))
        latex = f"\\text{{Solve: }} (x {'-' if h < 0 else '+'} {abs(h)})^2 = {k}"
        solution = f"x = {h - sqrt_k}, x = {h + sqrt_k}"
        steps = [
            f"(x {'-' if h < 0 else '+'} {abs(h)})² = {k}",
            f"Take square root: x {'-' if h < 0 else '+'} {abs(h)} = ±{sqrt_k}",
            f"x = {h} ± {sqrt_k}",
            f"x = {h - sqrt_k} or x = {h + sqrt_k}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        h = random.randint(-4, 4)
        k = random.choice([4, 9, 16, 25])
        sqrt_k = int(math.sqrt(k))
        latex = f"\\text{{Solve: }} {a}(x {'-' if h < 0 else '+'} {abs(h)})^2 = {a * k}"
        sol1 = h - sqrt_k
        sol2 = h + sqrt_k
        solution = f"x = {sol1}, x = {sol2}"
        steps = [
            f"{a}(x {'-' if h < 0 else '+'} {abs(h)})² = {a * k}",
            f"Divide by {a}: (x {'-' if h < 0 else '+'} {abs(h)})² = {k}",
            f"Take square root: x {'-' if h < 0 else '+'} {abs(h)} = ±{sqrt_k}",
            f"x = {h} ± {sqrt_k}",
            f"x = {sol1} or x = {sol2}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingSquareRootGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
