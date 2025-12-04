"""
Completing the Square Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CompletingTheSquareGenerator:
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
        b = random.choice([2, 4, 6, 8, 10])
        half_b = b // 2
        c_to_add = half_b ** 2
        latex = f"\\text{{Complete the square: }} x^2 + {b}x + \\underline{{\\hspace{{1cm}}}}"
        solution = f"{c_to_add}"
        steps = [
            f"Take half of b-coefficient: {b}/2 = {half_b}",
            f"Square it: ({half_b})² = {c_to_add}",
            f"Add {c_to_add} to complete the square",
            f"x² + {b}x + {c_to_add} = (x + {half_b})²"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        b = random.randint(-10, 10)
        if b == 0:
            b = 4
        c = random.randint(-8, 8)
        half_b = b / 2
        c_needed = half_b ** 2
        h = -half_b
        k = c - c_needed
        latex = f"\\text{{Complete the square: }} x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}"
        solution = f"(x {'-' if h < 0 else '+'} {abs(h):.1f})^2 {'+' if k >= 0 else ''}{k:.1f}"
        steps = [
            f"x² {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}",
            f"Take half of {b}: {b}/2 = {half_b}",
            f"Square it: ({half_b})² = {c_needed}",
            f"Add and subtract {c_needed}:",
            f"x² {'+' if b >= 0 else ''}{b}x + {c_needed} - {c_needed} {'+' if c >= 0 else ''}{c}",
            f"(x {'+' if half_b >= 0 else ''}{half_b})² {'+' if k >= 0 else ''}{k:.1f}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(-8, 8)
        c = random.randint(-8, 8)
        b_over_a = b / a
        half_b_over_a = b_over_a / 2
        c_needed = half_b_over_a ** 2
        h = -half_b_over_a
        k = c / a - c_needed
        latex = f"\\text{{Complete the square: }} {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}"
        solution = f"{a}(x {'-' if h < 0 else '+'} {abs(h):.2f})^2 {'+' if a*k >= 0 else ''}{a*k:.2f}"
        steps = [
            f"Factor out {a}: {a}(x² {'+' if b_over_a >= 0 else ''}{b_over_a:.1f}x {'+' if c/a >= 0 else ''}{c/a:.1f})",
            f"Complete square inside: half of {b_over_a:.1f} is {half_b_over_a:.2f}",
            f"({half_b_over_a:.2f})² = {c_needed:.2f}",
            solution
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        h = -b / (2 * a)
        k = c - (b ** 2) / (4 * a)
        latex = f"\\text{{Solve by completing the square: }} {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c} = 0"
        k_val = -k
        if k_val < 0:
            solution = "No real solutions"
            steps = [
                f"Complete the square to get {a}(x - {h:.2f})² = {k_val:.2f}",
                f"Since {k_val:.2f} < 0, no real solutions"
            ]
        else:
            import math
            sqrt_val = math.sqrt(abs(k_val / a))
            sol1 = h + sqrt_val
            sol2 = h - sqrt_val
            solution = f"x = {sol1:.2f}, x = {sol2:.2f}"
            steps = [
                f"Complete square: {a}(x - {h:.2f})² + {k:.2f} = 0",
                f"(x - {h:.2f})² = {k_val/a:.2f}",
                f"x - {h:.2f} = ±{sqrt_val:.2f}",
                solution
            ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CompletingTheSquareGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
