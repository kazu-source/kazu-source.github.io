"""
Quadratics with Complex Solutions Generator
"""
import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class QuadraticsComplexSolutionsGenerator:
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
        # x^2 + c = 0, where c > 0
        c = random.randint(4, 25)

        latex = f"x^2 + {c} = 0"
        solution = f"x = \\pm {int(math.sqrt(c))}i" if int(math.sqrt(c))**2 == c else f"x = \\pm \\sqrt{{{c}}}i"
        steps = [
            f"x^2 = -{c}",
            f"x = \\pm \\sqrt{{-{c}}}",
            f"x = \\pm \\sqrt{{{c}}} \\cdot \\sqrt{{-1}}",
            f"x = \\pm \\sqrt{{{c}}}i",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # ax^2 + c = 0, where discriminant < 0
        a = random.randint(1, 4)
        c = random.randint(5, 20)

        latex = f"{a}x^2 + {c} = 0"

        # x^2 = -c/a, x = ±(-c/a)i
        if c % a == 0:
            val = c // a
            solution = f"x = \\pm \\sqrt{{{val}}}i" if int(math.sqrt(val))**2 != val else f"x = \\pm {int(math.sqrt(val))}i"
        else:
            solution = f"x = \\pm \\sqrt{{\\frac{{{c}}}{{{a}}}}}i"

        steps = [
            f"{a}x^2 = -{c}",
            f"x^2 = -\\frac{{{c}}}{{{a}}}",
            f"x = \\pm \\sqrt{{-\\frac{{{c}}}{{{a}}}}}",
            f"x = \\pm \\sqrt{{\\frac{{{c}}}{{{a}}}}}i",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Quadratic formula with negative discriminant
        # x^2 + bx + c = 0
        b = random.randint(2, 8) * 2  # Even number for simpler solutions
        # Choose c such that discriminant < 0
        c = (b // 2)**2 + random.randint(1, 10)

        latex = f"x^2 + {b}x + {c} = 0"
        discriminant = b*b - 4*c
        sqrt_disc = int(math.sqrt(abs(discriminant)))

        if sqrt_disc * sqrt_disc == abs(discriminant):
            solution = f"x = \\frac{{-{b} \\pm {sqrt_disc}i}}{{2}}"
        else:
            solution = f"x = \\frac{{-{b} \\pm \\sqrt{{{abs(discriminant)}}}i}}{{2}}"

        steps = [
            f"Use quadratic formula: x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}",
            f"a = 1, b = {b}, c = {c}",
            f"Discriminant: {b}^2 - 4(1)({c}) = {b*b} - {4*c} = {discriminant}",
            f"Since discriminant < 0, solutions are complex",
            f"x = \\frac{{-{b} \\pm \\sqrt{{{discriminant}}}}}{{2}}",
            f"x = \\frac{{-{b} \\pm \\sqrt{{{abs(discriminant)}}}i}}{{2}}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # General quadratic with complex solutions
        a = random.randint(2, 4)
        b = random.randint(3, 9)
        # Ensure discriminant < 0
        c = random.randint((b*b)//(4*a) + 1, (b*b)//(4*a) + 10)

        latex = f"{a}x^2 + {b}x + {c} = 0"
        discriminant = b*b - 4*a*c
        sqrt_disc = int(math.sqrt(abs(discriminant)))

        if sqrt_disc * sqrt_disc == abs(discriminant):
            solution = f"x = \\frac{{-{b} \\pm {sqrt_disc}i}}{{{2*a}}}"
        else:
            solution = f"x = \\frac{{-{b} \\pm \\sqrt{{{abs(discriminant)}}}i}}{{{2*a}}}"

        steps = [
            f"Use quadratic formula: x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}",
            f"a = {a}, b = {b}, c = {c}",
            f"b^2 - 4ac = {b}^2 - 4({a})({c}) = {b*b} - {4*a*c} = {discriminant}",
            f"\\sqrt{{{discriminant}}} = \\sqrt{{-{abs(discriminant)}}} = \\sqrt{{{abs(discriminant)}}}i",
            f"x = \\frac{{-{b} \\pm \\sqrt{{{abs(discriminant)}}}i}}{{{2*a}}}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = QuadraticsComplexSolutionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
