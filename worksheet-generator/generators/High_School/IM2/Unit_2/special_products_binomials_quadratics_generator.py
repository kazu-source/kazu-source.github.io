"""
Special Products of Binomials (Quadratics) Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SpecialProductsBinomialsQuadraticsGenerator:
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
        problem_type = random.choice(['perfect_square', 'difference_squares'])

        if problem_type == 'perfect_square':
            a = random.randint(1, 8)
            sign = random.choice(['+', '-'])

            latex = f"(x {sign} {a})^2"

            if sign == '+':
                solution = f"x^2 + {2*a}x + {a**2}"
                steps = [
                    f"(x + {a})² = (x + {a})(x + {a})",
                    f"Use pattern (a + b)² = a² + 2ab + b²",
                    f"= x² + 2·x·{a} + {a}²",
                    f"= x² + {2*a}x + {a**2}"
                ]
            else:
                solution = f"x^2 - {2*a}x + {a**2}"
                steps = [
                    f"(x - {a})² = (x - {a})(x - {a})",
                    f"Use pattern (a - b)² = a² - 2ab + b²",
                    f"= x² - 2·x·{a} + {a}²",
                    f"= x² - {2*a}x + {a**2}"
                ]
        else:  # difference_squares
            a = random.randint(2, 8)

            latex = f"(x + {a})(x - {a})"
            solution = f"x^2 - {a**2}"
            steps = [
                f"(x + {a})(x - {a})",
                "Use pattern (a + b)(a - b) = a² - b²",
                f"= x² - {a}²",
                f"= x² - {a**2}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['perfect_square_coefficient', 'difference_squares_coefficient'])

        if problem_type == 'perfect_square_coefficient':
            a = random.randint(2, 5)
            b = random.randint(1, 6)
            sign = random.choice(['+', '-'])

            latex = f"({a}x {sign} {b})^2"

            if sign == '+':
                solution = f"{a**2}x^2 + {2*a*b}x + {b**2}"
                steps = [
                    f"({a}x + {b})² = ({a}x + {b})({a}x + {b})",
                    f"Use pattern (a + b)² = a² + 2ab + b²",
                    f"= ({a}x)² + 2·{a}x·{b} + {b}²",
                    f"= {a**2}x² + {2*a*b}x + {b**2}"
                ]
            else:
                solution = f"{a**2}x^2 - {2*a*b}x + {b**2}"
                steps = [
                    f"({a}x - {b})² = ({a}x - {b})({a}x - {b})",
                    f"Use pattern (a - b)² = a² - 2ab + b²",
                    f"= ({a}x)² - 2·{a}x·{b} + {b}²",
                    f"= {a**2}x² - {2*a*b}x + {b**2}"
                ]
        else:  # difference_squares_coefficient
            a = random.randint(2, 6)
            b = random.randint(2, 7)

            latex = f"({a}x + {b})({a}x - {b})"
            solution = f"{a**2}x^2 - {b**2}"
            steps = [
                f"({a}x + {b})({a}x - {b})",
                "Use pattern (a + b)(a - b) = a² - b²",
                f"= ({a}x)² - {b}²",
                f"= {a**2}x² - {b**2}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['cube_pattern', 'complex_special'])

        if problem_type == 'cube_pattern':
            a = random.randint(1, 5)
            sign = random.choice(['+', '-'])

            latex = f"(x {sign} {a})^3"

            if sign == '+':
                # (a+b)³ = a³ + 3a²b + 3ab² + b³
                solution = f"x^3 + {3*a}x^2 + {3*a**2}x + {a**3}"
                steps = [
                    f"(x + {a})³ = (x + {a})(x + {a})²",
                    f"First find (x + {a})² = x² + {2*a}x + {a**2}",
                    f"Then (x + {a})(x² + {2*a}x + {a**2})",
                    f"= x³ + {2*a}x² + {a**2}x + {a}x² + {2*a**2}x + {a**3}",
                    f"= x³ + {3*a}x² + {3*a**2}x + {a**3}"
                ]
            else:
                # (a-b)³ = a³ - 3a²b + 3ab² - b³
                solution = f"x^3 - {3*a}x^2 + {3*a**2}x - {a**3}"
                steps = [
                    f"(x - {a})³ = (x - {a})(x - {a})²",
                    f"First find (x - {a})² = x² - {2*a}x + {a**2}",
                    f"Then (x - {a})(x² - {2*a}x + {a**2})",
                    f"= x³ - {2*a}x² + {a**2}x - {a}x² + {2*a**2}x - {a**3}",
                    f"= x³ - {3*a}x² + {3*a**2}x - {a**3}"
                ]
        else:  # complex_special
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(2, 4)

            latex = f"({a}x + {b})^2 - ({c}x)^2"

            # First expand (ax+b)²
            term1 = a**2
            term2 = 2*a*b
            term3 = b**2
            # Then subtract (cx)²
            final_x2 = term1 - c**2

            solution = f"{final_x2}x^2 + {term2}x + {term3}"
            steps = [
                f"First expand ({a}x + {b})²:",
                f"= {a**2}x² + {2*a*b}x + {b**2}",
                f"Then subtract ({c}x)² = {c**2}x²:",
                f"= {a**2}x² - {c**2}x² + {term2}x + {term3}",
                f"= {final_x2}x² + {term2}x + {term3}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 4)
        c = random.randint(2, 4)
        d = random.randint(1, 4)

        latex = f"({a}x + {b})^2 + ({c}x - {d})^2"

        # First square
        s1_x2 = a**2
        s1_x = 2*a*b
        s1_const = b**2

        # Second square
        s2_x2 = c**2
        s2_x = -2*c*d
        s2_const = d**2

        # Combine
        final_x2 = s1_x2 + s2_x2
        final_x = s1_x + s2_x
        final_const = s1_const + s2_const

        solution = f"{final_x2}x^2 {'+' if final_x >= 0 else ''}{final_x}x + {final_const}"
        steps = [
            f"Expand ({a}x + {b})²:",
            f"= {s1_x2}x² + {s1_x}x + {s1_const}",
            f"Expand ({c}x - {d})²:",
            f"= {s2_x2}x² - {2*c*d}x + {s2_const}",
            "Combine like terms:",
            f"x² terms: {s1_x2}x² + {s2_x2}x² = {final_x2}x²",
            f"x terms: {s1_x}x + ({s2_x}x) = {final_x}x",
            f"Constants: {s1_const} + {s2_const} = {final_const}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SpecialProductsBinomialsQuadraticsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
