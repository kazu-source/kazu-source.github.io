"""
Multiplying Monomials and Polynomials (Quadratics) Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiplyingMonomialsPolynomialsQuadraticsGenerator:
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
        problem_type = random.choice(['monomial_binomial', 'simple_distribute'])

        if problem_type == 'monomial_binomial':
            a = random.randint(2, 6)
            b = random.randint(1, 8)
            c = random.randint(1, 8)
            sign = random.choice(['+', '-'])

            latex = f"{a}x({b}x {sign} {c})"

            if sign == '+':
                result_b = a * b
                result_c = a * c
                solution = f"{result_b}x^2 + {result_c}x"
                steps = [
                    f"Distribute {a}x to each term:",
                    f"{a}x · {b}x + {a}x · {c}",
                    f"{result_b}x² + {result_c}x"
                ]
            else:
                result_b = a * b
                result_c = a * c
                solution = f"{result_b}x^2 - {result_c}x"
                steps = [
                    f"Distribute {a}x to each term:",
                    f"{a}x · {b}x - {a}x · {c}",
                    f"{result_b}x² - {result_c}x"
                ]
        else:  # simple_distribute
            a = random.randint(1, 5)
            b = random.randint(1, 7)
            c = random.randint(1, 7)

            latex = f"{a}(x^2 + {b}x + {c})"
            solution = f"{a}x^2 + {a*b}x + {a*c}"
            steps = [
                f"Distribute {a} to each term:",
                f"{a} · x² + {a} · {b}x + {a} · {c}",
                f"{a}x² + {a*b}x + {a*c}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['monomial_trinomial', 'negative_monomial'])

        if problem_type == 'monomial_trinomial':
            a = random.randint(2, 5)
            b = random.randint(1, 6)
            c = random.randint(1, 6)
            d = random.randint(1, 6)
            sign1 = random.choice(['+', '-'])
            sign2 = random.choice(['+', '-'])

            latex = f"{a}x({b}x^2 {sign1} {c}x {sign2} {d})"

            term1 = a * b
            term2 = a * c if sign1 == '+' else -a * c
            term3 = a * d if sign2 == '+' else -a * d

            solution = f"{term1}x^3 {'+' if term2 >= 0 else ''}{term2}x^2 {'+' if term3 >= 0 else ''}{term3}x"
            steps = [
                f"Distribute {a}x to each term:",
                f"{a}x · {b}x² {sign1} {a}x · {c}x {sign2} {a}x · {d}",
                f"{term1}x³ {sign1} {a*c}x² {sign2} {a*d}x",
                solution
            ]
        else:  # negative_monomial
            a = random.randint(2, 6)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            sign = random.choice(['+', '-'])

            latex = f"-{a}x({b}x {sign} {c})"

            term1 = -a * b
            term2 = -a * c if sign == '+' else a * c

            solution = f"{term1}x^2 {'+' if term2 >= 0 else ''}{term2}x"
            steps = [
                f"Distribute -{a}x to each term:",
                f"-{a}x · {b}x {'+' if sign == '+' else '-'} ({-a}x) · {c}",
                f"{term1}x² {'+' if term2 >= 0 else ''}{term2}x"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['coefficient_with_power', 'complex_distribution'])

        if problem_type == 'coefficient_with_power':
            a = random.randint(2, 5)
            exp = random.randint(2, 3)
            b = random.randint(1, 6)
            c = random.randint(1, 6)
            d = random.randint(1, 6)
            sign1 = random.choice(['+', '-'])
            sign2 = random.choice(['+', '-'])

            latex = f"{a}x^{exp}({b}x^2 {sign1} {c}x {sign2} {d})"

            term1_exp = exp + 2
            term2_exp = exp + 1
            term3_exp = exp

            term1_coef = a * b
            term2_coef = a * c if sign1 == '+' else -a * c
            term3_coef = a * d if sign2 == '+' else -a * d

            solution = f"{term1_coef}x^{term1_exp} {'+' if term2_coef >= 0 else ''}{term2_coef}x^{term2_exp} {'+' if term3_coef >= 0 else ''}{term3_coef}x^{term3_exp}"
            steps = [
                f"Distribute {a}x^{exp} to each term:",
                f"{a}x^{exp} · {b}x² {sign1} {a}x^{exp} · {c}x {sign2} {a}x^{exp} · {d}",
                f"{term1_coef}x^{term1_exp} {sign1} {a*c}x^{term2_exp} {sign2} {a*d}x^{term3_exp}",
                solution
            ]
        else:  # complex_distribution
            a = random.randint(2, 4)
            b = random.randint(2, 4)
            c = random.randint(1, 5)
            d = random.randint(1, 5)
            e = random.randint(1, 5)

            latex = f"{a}x^2(x^2 - {b}x + {c}) + {d}x({e}x - {b})"

            # First part: ax^2(x^2 - bx + c)
            part1_term1 = a
            part1_term2 = -a * b
            part1_term3 = a * c

            # Second part: dx(ex - b)
            part2_term1 = d * e
            part2_term2 = -d * b

            # Combine
            final_x4 = part1_term1
            final_x3 = part1_term2
            final_x2 = part1_term3 + part2_term1
            final_x = part2_term2

            solution = f"{final_x4}x^4 {'+' if final_x3 >= 0 else ''}{final_x3}x^3 {'+' if final_x2 >= 0 else ''}{final_x2}x^2 {'+' if final_x >= 0 else ''}{final_x}x"
            steps = [
                f"First: {a}x² · x² - {a}x² · {b}x + {a}x² · {c} = {part1_term1}x⁴ {'+' if part1_term2 >= 0 else ''}{part1_term2}x³ {'+' if part1_term3 >= 0 else ''}{part1_term3}x²",
                f"Second: {d}x · {e}x - {d}x · {b} = {part2_term1}x² {'+' if part2_term2 >= 0 else ''}{part2_term2}x",
                f"Combine: {final_x4}x⁴ {'+' if final_x3 >= 0 else ''}{final_x3}x³ + ({part1_term3}x² + {part2_term1}x²) {'+' if final_x >= 0 else ''}{final_x}x",
                solution
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 3)
        c = random.randint(2, 5)
        d = random.randint(1, 4)
        e = random.randint(1, 3)
        sign1 = random.choice(['+', '-'])
        sign2 = random.choice(['+', '-'])

        latex = f"{a}x^2({b}x^3 {sign1} {c}x {sign2} {d}) - {e}x^2({b}x^2 - {c})"

        # First part
        p1_t1 = a * b
        p1_t2 = a * c if sign1 == '+' else -a * c
        p1_t3 = a * d if sign2 == '+' else -a * d

        # Second part (with negative sign in front)
        p2_t1 = -e * b
        p2_t2 = e * c

        # Combine like terms
        final_x5 = p1_t1
        final_x4 = p2_t1
        final_x3 = p1_t2 + p2_t2
        final_x2 = p1_t3

        solution = f"{final_x5}x^5 {'+' if final_x4 >= 0 else ''}{final_x4}x^4 {'+' if final_x3 >= 0 else ''}{final_x3}x^3 {'+' if final_x2 >= 0 else ''}{final_x2}x^2"
        steps = [
            f"First part: {a}x² · {b}x³ {sign1} {a}x² · {c}x {sign2} {a}x² · {d}",
            f"= {p1_t1}x⁵ {'+' if p1_t2 >= 0 else ''}{p1_t2}x³ {'+' if p1_t3 >= 0 else ''}{p1_t3}x²",
            f"Second part: -{e}x² · {b}x² - (-{e}x² · {c})",
            f"= {p2_t1}x⁴ {'+' if p2_t2 >= 0 else ''}{p2_t2}x²",
            f"Combine all terms:",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = MultiplyingMonomialsPolynomialsQuadraticsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
