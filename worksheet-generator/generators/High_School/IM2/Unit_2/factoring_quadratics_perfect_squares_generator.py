"""
Factoring Quadratics - Perfect Square Trinomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringQuadraticsPerfectSquaresGenerator:
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
        # Simple (x + a)² or (x - a)²
        a = random.randint(1, 8)
        sign = random.choice(['+', '-'])

        if sign == '+':
            middle = 2 * a
            const = a**2
            latex = f"\\text{{Factor: }} x^2 + {middle}x + {const}"
            solution = f"(x + {a})^2"
            steps = [
                f"Check if perfect square trinomial: a² + 2ab + b²",
                f"x² + {middle}x + {const}",
                f"First term: x² = (x)²",
                f"Last term: {const} = {a}²",
                f"Middle term: {middle}x = 2·x·{a} ✓",
                f"Answer: (x + {a})²"
            ]
        else:
            middle = 2 * a
            const = a**2
            latex = f"\\text{{Factor: }} x^2 - {middle}x + {const}"
            solution = f"(x - {a})^2"
            steps = [
                f"Check if perfect square trinomial: a² - 2ab + b²",
                f"x² - {middle}x + {const}",
                f"First term: x² = (x)²",
                f"Last term: {const} = {a}²",
                f"Middle term: -{middle}x = -2·x·{a} ✓",
                f"Answer: (x - {a})²"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # (ax + b)² or (ax - b)²
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        sign = random.choice(['+', '-'])

        coef_x2 = a**2
        middle = 2 * a * b
        const = b**2

        if sign == '+':
            latex = f"\\text{{Factor: }} {coef_x2}x^2 + {middle}x + {const}"
            solution = f"({a}x + {b})^2"
            steps = [
                f"Check if perfect square trinomial",
                f"First term: {coef_x2}x² = ({a}x)²",
                f"Last term: {const} = {b}²",
                f"Middle term: {middle}x = 2·{a}x·{b} ✓",
                f"Answer: ({a}x + {b})²"
            ]
        else:
            latex = f"\\text{{Factor: }} {coef_x2}x^2 - {middle}x + {const}"
            solution = f"({a}x - {b})^2"
            steps = [
                f"Check if perfect square trinomial",
                f"First term: {coef_x2}x² = ({a}x)²",
                f"Last term: {const} = {b}²",
                f"Middle term: -{middle}x = -2·{a}x·{b} ✓",
                f"Answer: ({a}x - {b})²"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Factor out GCF first, then perfect square
        gcf = random.randint(2, 4)
        a = random.randint(1, 4)
        b = random.randint(1, 5)
        sign = random.choice(['+', '-'])

        coef_x2 = gcf * a**2
        middle = gcf * 2 * a * b
        const = gcf * b**2

        if sign == '+':
            latex = f"\\text{{Factor completely: }} {coef_x2}x^2 + {middle}x + {const}"
            solution = f"{gcf}({a}x + {b})^2"
            steps = [
                f"Factor out GCF = {gcf}",
                f"{gcf}({a**2}x² + {2*a*b}x + {b**2})",
                f"Check if perfect square trinomial:",
                f"({a}x)² + 2·{a}x·{b} + {b}²",
                f"{gcf}({a}x + {b})²"
            ]
        else:
            latex = f"\\text{{Factor completely: }} {coef_x2}x^2 - {middle}x + {const}"
            solution = f"{gcf}({a}x - {b})^2"
            steps = [
                f"Factor out GCF = {gcf}",
                f"{gcf}({a**2}x² - {2*a*b}x + {b**2})",
                f"Check if perfect square trinomial:",
                f"({a}x)² - 2·{a}x·{b} + {b}²",
                f"{gcf}({a}x - {b})²"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Higher degree perfect squares
        a = random.randint(1, 3)
        power = random.choice([2, 3])
        b = random.randint(1, 4)
        sign = random.choice(['+', '-'])

        coef_x = a**2
        total_power = 2 * power
        middle_power = power
        middle_coef = 2 * a * b
        const = b**2

        if sign == '+':
            latex = f"\\text{{Factor: }} {coef_x}x^{total_power} + {middle_coef}x^{middle_power} + {const}"
            solution = f"({a}x^{power} + {b})^2"
            steps = [
                f"Check if perfect square trinomial",
                f"First: {coef_x}x^{total_power} = ({a}x^{power})²",
                f"Last: {const} = {b}²",
                f"Middle: {middle_coef}x^{middle_power} = 2·{a}x^{power}·{b} ✓",
                f"Answer: ({a}x^{power} + {b})²"
            ]
        else:
            latex = f"\\text{{Factor: }} {coef_x}x^{total_power} - {middle_coef}x^{middle_power} + {const}"
            solution = f"({a}x^{power} - {b})^2"
            steps = [
                f"Check if perfect square trinomial",
                f"First: {coef_x}x^{total_power} = ({a}x^{power})²",
                f"Last: {const} = {b}²",
                f"Middle: -{middle_coef}x^{middle_power} = -2·{a}x^{power}·{b} ✓",
                f"Answer: ({a}x^{power} - {b})²"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FactoringQuadraticsPerfectSquaresGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
