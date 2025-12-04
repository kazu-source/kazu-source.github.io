"""
Multiplying Binomials (Quadratics) Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiplyingBinomialsQuadraticsGenerator:
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
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        sign1 = random.choice(['+', '-'])
        sign2 = random.choice(['+', '-'])

        latex = f"(x {sign1} {a})(x {sign2} {b})"

        # Use FOIL
        first = 1  # x * x = x^2
        outer = b if sign2 == '+' else -b  # x * b
        inner = a if sign1 == '+' else -a  # a * x
        last = a * b if (sign1 == sign2) else -a * b  # a * b

        middle = outer + inner

        solution = f"x^2 {'+' if middle >= 0 else ''}{middle}x {'+' if last >= 0 else ''}{last}"
        steps = [
            "Use FOIL method:",
            f"First: x · x = x²",
            f"Outer: x · {b if sign2 == '+' else f'(-{b})'} = {outer}x",
            f"Inner: {a if sign1 == '+' else f'(-{a})'} · x = {inner}x",
            f"Last: {a if sign1 == '+' else f'(-{a})'} · {b if sign2 == '+' else f'(-{b})'} = {last}",
            f"Combine: x² + {outer}x + {inner}x {'+' if last >= 0 else ''}{last}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        c = random.randint(2, 5)
        d = random.randint(1, 6)
        sign1 = random.choice(['+', '-'])
        sign2 = random.choice(['+', '-'])

        latex = f"({a}x {sign1} {b})({c}x {sign2} {d})"

        # FOIL
        first_coef = a * c
        outer_coef = a * d if sign2 == '+' else -a * d
        inner_coef = b * c if sign1 == '+' else -b * c
        last_term = b * d if (sign1 == sign2) else -b * d

        middle_coef = outer_coef + inner_coef

        solution = f"{first_coef}x^2 {'+' if middle_coef >= 0 else ''}{middle_coef}x {'+' if last_term >= 0 else ''}{last_term}"
        steps = [
            "Use FOIL method:",
            f"First: {a}x · {c}x = {first_coef}x²",
            f"Outer: {a}x · {d if sign2 == '+' else f'(-{d})'} = {outer_coef}x",
            f"Inner: {b if sign1 == '+' else f'(-{b})'} · {c}x = {inner_coef}x",
            f"Last: {b if sign1 == '+' else f'(-{b})'} · {d if sign2 == '+' else f'(-{d})'} = {last_term}",
            f"Combine middle terms: {outer_coef}x + {inner_coef}x = {middle_coef}x",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(2, 6)
        d = random.randint(1, 8)
        sign1 = random.choice(['+', '-'])
        sign2 = random.choice(['+', '-'])

        latex = f"({a}x {sign1} {b})({c}x {sign2} {d})"

        first_coef = a * c
        outer_coef = a * d if sign2 == '+' else -a * d
        inner_coef = b * c if sign1 == '+' else -b * c
        last_term = b * d if (sign1 == sign2) else -b * d
        middle_coef = outer_coef + inner_coef

        solution = f"{first_coef}x^2 {'+' if middle_coef >= 0 else ''}{middle_coef}x {'+' if last_term >= 0 else ''}{last_term}"
        steps = [
            f"({a}x {sign1} {b})({c}x {sign2} {d})",
            f"F: {a}x · {c}x = {first_coef}x²",
            f"O: {a}x · {d if sign2 == '+' else f'(-{d})'} = {outer_coef}x",
            f"I: {b if sign1 == '+' else f'(-{b})'} · {c}x = {inner_coef}x",
            f"L: {b if sign1 == '+' else f'(-{b})'} · {d if sign2 == '+' else f'(-{d})'} = {last_term}",
            f"= {first_coef}x² + ({outer_coef}x + {inner_coef}x) {'+' if last_term >= 0 else ''}{last_term}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        c = random.randint(2, 5)
        d = random.randint(1, 6)
        e = random.randint(1, 4)
        sign1 = random.choice(['+', '-'])
        sign2 = random.choice(['+', '-'])

        latex = f"({a}x {sign1} {b})({c}x {sign2} {d}) + {e}x^2"

        # First multiply binomials
        first_coef = a * c
        outer_coef = a * d if sign2 == '+' else -a * d
        inner_coef = b * c if sign1 == '+' else -b * c
        last_term = b * d if (sign1 == sign2) else -b * d
        middle_coef = outer_coef + inner_coef

        # Add ex^2
        final_x2 = first_coef + e

        solution = f"{final_x2}x^2 {'+' if middle_coef >= 0 else ''}{middle_coef}x {'+' if last_term >= 0 else ''}{last_term}"
        steps = [
            f"First multiply ({a}x {sign1} {b})({c}x {sign2} {d}):",
            f"= {first_coef}x² {'+' if middle_coef >= 0 else ''}{middle_coef}x {'+' if last_term >= 0 else ''}{last_term}",
            f"Then add {e}x²:",
            f"= {first_coef}x² + {e}x² {'+' if middle_coef >= 0 else ''}{middle_coef}x {'+' if last_term >= 0 else ''}{last_term}",
            f"= {final_x2}x² {'+' if middle_coef >= 0 else ''}{middle_coef}x {'+' if last_term >= 0 else ''}{last_term}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = MultiplyingBinomialsQuadraticsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
