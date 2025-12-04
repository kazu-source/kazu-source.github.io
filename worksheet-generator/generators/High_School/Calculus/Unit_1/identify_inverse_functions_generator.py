"""
Identify Inverse Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class IdentifyInverseFunctionsGenerator:
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
        a = random.randint(2, 5)

        latex = f"\\text{{Are }} f(x) = {a}x \\text{{ and }} g(x) = \\frac{{x}}{{{a}}} \\text{{ inverses?}}"
        solution = "Yes"
        steps = [
            f"(f \\circ g)(x) = f\\left(\\frac{{x}}{{{a}}}\\right) = {a} \\cdot \\frac{{x}}{{{a}}} = x",
            f"(g \\circ f)(x) = g({a}x) = \\frac{{{a}x}}{{{a}}} = x",
            "\\text{Both compositions equal } x, \\text{ so they are inverses}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 6)

        latex = f"\\text{{Are }} f(x) = x + {b} \\text{{ and }} g(x) = x - {b} \\text{{ inverses?}}"
        solution = "Yes"
        steps = [
            f"(f \\circ g)(x) = f(x - {b}) = (x - {b}) + {b} = x",
            f"(g \\circ f)(x) = g(x + {b}) = (x + {b}) - {b} = x",
            "\\text{Both compositions equal } x, \\text{ so they are inverses}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        is_inverse = random.choice([True, False])

        if is_inverse:
            latex = f"\\text{{Are }} f(x) = {a}x + {b} \\text{{ and }} g(x) = \\frac{{x - {b}}}{{{a}}} \\text{{ inverses?}}"
            solution = "Yes"
            steps = [
                f"(f \\circ g)(x) = f\\left(\\frac{{x - {b}}}{{{a}}}\\right)",
                f"= {a} \\cdot \\frac{{x - {b}}}{{{a}}} + {b}",
                f"= (x - {b}) + {b} = x",
                f"(g \\circ f)(x) = g({a}x + {b})",
                f"= \\frac{{({a}x + {b}) - {b}}}{{{a}}} = \\frac{{{a}x}}{{{a}}} = x",
                "\\text{Both compositions equal } x, \\text{ so they are inverses}"
            ]
        else:
            wrong_b = b + random.randint(1, 3)
            latex = f"\\text{{Are }} f(x) = {a}x + {b} \\text{{ and }} g(x) = \\frac{{x - {wrong_b}}}{{{a}}} \\text{{ inverses?}}"
            solution = "No"
            steps = [
                f"(f \\circ g)(x) = f\\left(\\frac{{x - {wrong_b}}}{{{a}}}\\right)",
                f"= {a} \\cdot \\frac{{x - {wrong_b}}}{{{a}}} + {b}",
                f"= (x - {wrong_b}) + {b} = x + {b - wrong_b} \\neq x",
                "\\text{Composition does not equal } x, \\text{ so they are not inverses}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)

        latex = f"\\text{{Verify }} f(x) = x^{{{a}}} \\text{{ and }} g(x) = \\sqrt[{a}]{{x}} \\text{{ are inverses for }} x \\geq 0."
        solution = "Yes, they are inverses"
        steps = [
            f"(f \\circ g)(x) = f(\\sqrt[{a}]{{x}}) = (\\sqrt[{a}]{{x}})^{{{a}}} = x",
            f"(g \\circ f)(x) = g(x^{{{a}}}) = \\sqrt[{a}]{{x^{{{a}}}}} = x",
            "\\text{Both compositions equal } x \\text{ for } x \\geq 0",
            "\\text{Therefore, they are inverses}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = IdentifyInverseFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
