"""
Quadratic Formula Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation
import math

class QuadraticFormulaGenerator:
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
        a, b, c = 1, random.randint(-6, 6), random.randint(-8, 8)
        disc = b**2 - 4*a*c
        if disc < 0:
            c = -abs(c)
            disc = b**2 - 4*a*c
        latex = f"\\text{{Use quadratic formula to solve: }} x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c} = 0"
        if disc >= 0 and math.sqrt(disc) == int(math.sqrt(disc)):
            sqrt_d = int(math.sqrt(disc))
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)
            solution = f"x = {x1:.1f}, x = {x2:.1f}"
        else:
            solution = f"x = \\frac{{-{b} \\pm \\sqrt{{{disc}}}}}{{{2*a}}}"
        steps = [
            f"a = {a}, b = {b}, c = {c}",
            f"x = \\frac{{-b \\pm \\sqrt{{b² - 4ac}}}}{{2a}}",
            f"x = \\frac{{-({b}) \\pm \\sqrt{{({b})² - 4({a})({c})}}}}{{2({a})}}",
            f"x = \\frac{{-{b} \\pm \\sqrt{{{disc}}}}}{{{2*a}}}",
            solution
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(-8, 8)
        c = random.randint(-8, 8)
        disc = b**2 - 4*a*c
        latex = f"\\text{{Solve using quadratic formula: }} {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c} = 0"
        solution = f"x = \\frac{{-{b} \\pm \\sqrt{{{disc}}}}}{{{2*a}}}"
        steps = [
            f"a = {a}, b = {b}, c = {c}",
            f"Discriminant: b² - 4ac = {b}² - 4({a})({c}) = {disc}",
            f"x = \\frac{{-{b} \\pm \\sqrt{{{disc}}}}}{{{2*a}}}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        disc = b**2 - 4*a*c
        latex = f"\\text{{Solve: }} {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c} = 0"
        if disc >= 0 and math.sqrt(disc) == int(math.sqrt(disc)):
            sqrt_d = int(math.sqrt(disc))
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)
            solution = f"x = {x1:.2f}, x = {x2:.2f}"
        else:
            solution = f"x = \\frac{{-{b} \\pm \\sqrt{{{disc}}}}}{{{2*a}}}"
        steps = [
            f"Use quadratic formula",
            f"Discriminant = {disc}",
            solution
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(-6, 6)
        c = random.randint(1, 8)
        disc = b**2 - 4*a*c
        if disc < 0:
            latex = f"\\text{{Solve: }} {a}x^2 {'+' if b >= 0 else ''}{b}x + {c} = 0"
            solution = f"No real solutions (discriminant = {disc} < 0)"
            steps = [
                f"Calculate discriminant: {b}² - 4({a})({c}) = {disc}",
                "Since discriminant < 0, no real solutions",
                "Complex solutions exist"
            ]
        else:
            latex = f"\\text{{Solve: }} {a}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c} = 0"
            solution = f"x = \\frac{{-{b} \\pm \\sqrt{{{disc}}}}}{{{2*a}}}"
            steps = [
                f"Discriminant = {disc}",
                solution
            ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = QuadraticFormulaGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
