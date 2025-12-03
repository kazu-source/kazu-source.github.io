"""
Polynomial Multiplication and Division Generator
Creates problems about multiplying and dividing polynomials
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class PolynomialMultDivGenerator:
    """Generates problems about multiplying and dividing polynomials."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Multiply monomial by binomial"""
        a = random.randint(2, 8)
        b = random.randint(1, 6)
        c = random.randint(-10, 10)

        result_a = a * b
        result_b = a * c

        latex = f"{a}({b}x + {c})"
        solution = f"{result_a}x + {result_b}"

        steps = [
            f"\\text{{Distribute }} {a}",
            f"{a} \\cdot {b}x + {a} \\cdot {c}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Multiply two binomials using FOIL"""
        a = random.randint(1, 5)
        b = random.randint(-8, 8)
        c = random.randint(1, 5)
        d = random.randint(-8, 8)

        # (ax + b)(cx + d) = acx^2 + (ad + bc)x + bd
        first = a * c
        outer = a * d
        inner = b * c
        last = b * d
        middle = outer + inner

        latex = f"({a}x + {b})({c}x + {d})"
        solution = f"{first}x^2 + {middle}x + {last}"

        steps = [
            f"\\text{{Use FOIL method}}",
            f"\\text{{First: }} {a}x \\cdot {c}x = {first}x^2",
            f"\\text{{Outer: }} {a}x \\cdot {d} = {outer}x",
            f"\\text{{Inner: }} {b} \\cdot {c}x = {inner}x",
            f"\\text{{Last: }} {b} \\cdot {d} = {last}",
            f"{first}x^2 + {middle}x + {last}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Multiply binomial by trinomial"""
        a = random.randint(1, 4)
        b = random.randint(-5, 5)

        c = random.randint(1, 3)
        d = random.randint(-4, 4)
        e = random.randint(-6, 6)

        # (ax + b)(cx^2 + dx + e)
        term1 = a * c
        term2 = a * d + b * c
        term3 = a * e + b * d
        term4 = b * e

        latex = f"({a}x + {b})({c}x^2 + {d}x + {e})"
        solution = f"{term1}x^3 + {term2}x^2 + {term3}x + {term4}"

        steps = [
            f"\\text{{Distribute each term}}",
            f"{a}x({c}x^2 + {d}x + {e}) + {b}({c}x^2 + {d}x + {e})",
            f"{term1}x^3 + {a * d}x^2 + {a * e}x + {b * c}x^2 + {b * d}x + {term4}",
            f"\\text{{Combine like terms}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Divide polynomial by monomial or multiply complex polynomials"""
        problem_type = random.choice(['division', 'multiplication'])

        if problem_type == 'division':
            # Divide polynomial by monomial
            divisor = random.randint(2, 6)
            a = divisor * random.randint(2, 8)
            b = divisor * random.randint(-6, 6)
            c = divisor * random.randint(-8, 8)

            result_a = a // divisor
            result_b = b // divisor
            result_c = c // divisor

            latex = f"\\frac{{{a}x^2 + {b}x + {c}}}{{{divisor}}}"
            solution = f"{result_a}x^2 + {result_b}x + {result_c}"

            steps = [
                f"\\text{{Divide each term by }} {divisor}",
                f"\\frac{{{a}x^2}}{{{divisor}}} + \\frac{{{b}x}}{{{divisor}}} + \\frac{{{c}}}{{{divisor}}}",
                solution
            ]
        else:
            # Multiply two trinomials (simplified)
            a1 = random.randint(1, 3)
            b1 = random.randint(1, 3)
            c1 = random.randint(1, 3)

            # (x + a)(x + b)(x + c) = x^3 + (a+b+c)x^2 + (ab+ac+bc)x + abc
            sum_coef = a1 + b1 + c1
            pair_sum = a1*b1 + a1*c1 + b1*c1
            product = a1 * b1 * c1

            latex = f"(x + {a1})(x + {b1})(x + {c1})"
            solution = f"x^3 + {sum_coef}x^2 + {pair_sum}x + {product}"

            steps = [
                f"\\text{{First multiply }} (x + {a1})(x + {b1}) = x^2 + {a1 + b1}x + {a1 * b1}",
                f"\\text{{Then multiply by }} (x + {c1})",
                f"(x^2 + {a1 + b1}x + {a1 * b1})(x + {c1})",
                solution
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PolynomialMultDivGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
