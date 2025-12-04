"""
Sums and Products of Rational and Irrational Numbers Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SumsProductsRationalIrrationalGenerator:
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
        a = random.randint(1, 8)
        b = random.choice([2, 3, 5])
        latex = f"\\text{{Is }} {a} + \\sqrt{{{b}}} \\text{{ rational or irrational?}}"
        solution = "Irrational"
        steps = [
            f"Sum of rational ({a}) and irrational (√{b})",
            "Rational + Irrational = Irrational",
            "Answer: Irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.choice([2, 3, 5])
        latex = f"\\text{{Is }} {a} \\cdot \\sqrt{{{b}}} \\text{{ rational or irrational?}}"
        solution = "Irrational"
        steps = [
            f"Product of rational ({a}) and irrational (√{b})",
            "Rational × Irrational = Irrational (when rational ≠ 0)",
            "Answer: Irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.choice([2, 3, 5])
        b = random.choice([2, 3, 5])
        latex = f"\\text{{Is }} \\sqrt{{{a}}} + \\sqrt{{{b}}} \\text{{ rational or irrational?}}"
        solution = "Irrational"
        steps = [
            f"√{a} is irrational",
            f"√{b} is irrational",
            "Sum of two irrational numbers is typically irrational",
            f"√{a} + √{b} is irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 4)
        b = random.choice([2, 3, 5])
        c = random.randint(1, 4)
        latex = f"\\text{{Is }} ({a} + \\sqrt{{{b}}})({c} - \\sqrt{{{b}}}) \\text{{ rational or irrational?}}"
        product = a * c - b
        solution = f"Rational (equals {product + a*c})"
        steps = [
            f"Expand: {a}·{c} - {a}√{b} + {c}√{b} - {b}",
            f"= {a*c} + ({c-a})√{b} - {b}",
            f"= {a*c - b} + ({c-a})√{b}",
            "If c-a = 0, result is rational" if c == a else f"Result is irrational"
        ]
        if c == a:
            solution = f"Rational (equals {a*c - b})"
        else:
            solution = "Irrational"
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SumsProductsRationalIrrationalGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
