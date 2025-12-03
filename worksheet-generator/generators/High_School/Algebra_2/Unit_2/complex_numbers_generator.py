"""
Complex Numbers Generator
Creates problems about complex numbers in a + bi form
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ComplexNumbersGenerator:
    """Generates problems about complex numbers."""

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

    def _format_complex(self, a, b):
        """Format a + bi nicely"""
        if b == 0:
            return str(a)
        elif a == 0:
            if b == 1:
                return "i"
            elif b == -1:
                return "-i"
            else:
                return f"{b}i"
        else:
            if b == 1:
                return f"{a} + i"
            elif b == -1:
                return f"{a} - i"
            elif b > 0:
                return f"{a} + {b}i"
            else:
                return f"{a} - {abs(b)}i"

    def _generate_easy(self) -> Equation:
        """Identify real and imaginary parts"""
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        while b == 0:
            b = random.randint(-10, 10)

        complex_num = self._format_complex(a, b)

        part = random.choice(['real', 'imaginary'])

        if part == 'real':
            latex = f"\\text{{What is the real part of }} {complex_num}?"
            solution = str(a)
            steps = [
                f"\\text{{In }} a + bi, \\text{{ the real part is }} a",
                f"\\text{{Real part of }} {complex_num} \\text{{ is }} {a}"
            ]
        else:
            latex = f"\\text{{What is the imaginary part of }} {complex_num}?"
            solution = str(b)
            steps = [
                f"\\text{{In }} a + bi, \\text{{ the imaginary part is }} b",
                f"\\text{{Imaginary part of }} {complex_num} \\text{{ is }} {b}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Add or subtract complex numbers"""
        a1 = random.randint(-8, 8)
        b1 = random.randint(-8, 8)
        a2 = random.randint(-8, 8)
        b2 = random.randint(-8, 8)

        operation = random.choice(['+', '-'])

        z1 = self._format_complex(a1, b1)
        z2 = self._format_complex(a2, b2)

        if operation == '+':
            result_a = a1 + a2
            result_b = b1 + b2
            latex = f"\\text{{Simplify: }} ({z1}) + ({z2})"
            op_word = "add"
        else:
            result_a = a1 - a2
            result_b = b1 - b2
            latex = f"\\text{{Simplify: }} ({z1}) - ({z2})"
            op_word = "subtract"

        solution = self._format_complex(result_a, result_b)

        steps = [
            f"\\text{{{op_word.capitalize()} real parts: }} {a1} {operation} {a2} = {result_a}",
            f"\\text{{{op_word.capitalize()} imaginary parts: }} {b1} {operation} {b2} = {result_b}",
            f"\\text{{Result: }} {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Multiply complex numbers"""
        a1 = random.randint(-5, 5)
        b1 = random.randint(-5, 5)
        a2 = random.randint(-5, 5)
        b2 = random.randint(-5, 5)

        while b1 == 0 or b2 == 0:
            b1 = random.randint(-5, 5)
            b2 = random.randint(-5, 5)

        z1 = self._format_complex(a1, b1)
        z2 = self._format_complex(a2, b2)

        # (a1 + b1i)(a2 + b2i) = a1*a2 + a1*b2*i + b1*a2*i + b1*b2*i^2
        # = a1*a2 - b1*b2 + (a1*b2 + b1*a2)i
        result_a = a1 * a2 - b1 * b2
        result_b = a1 * b2 + b1 * a2

        latex = f"\\text{{Simplify: }} ({z1})({z2})"
        solution = self._format_complex(result_a, result_b)

        steps = [
            f"\\text{{Use FOIL: }} ({a1} + {b1}i)({a2} + {b2}i)",
            f"= {a1}({a2}) + {a1}({b2}i) + {b1}i({a2}) + {b1}i({b2}i)",
            f"= {a1*a2} + {a1*b2}i + {b1*a2}i + {b1*b2}i^2",
            f"= {a1*a2} + {a1*b2 + b1*a2}i + {b1*b2}(-1)",
            f"= {a1*a2} - {b1*b2} + {a1*b2 + b1*a2}i",
            f"= {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex conjugates or division"""
        problem_type = random.choice(['conjugate', 'divide', 'power_of_i'])

        if problem_type == 'conjugate':
            a = random.randint(-8, 8)
            b = random.randint(1, 8) * random.choice([1, -1])
            z = self._format_complex(a, b)

            # z * z_bar = |z|^2 = a^2 + b^2
            result = a**2 + b**2

            latex = f"\\text{{Find }} z \\cdot \\bar{{z}} \\text{{ where }} z = {z}."
            solution = str(result)

            steps = [
                f"\\text{{Conjugate: }} \\bar{{z}} = {self._format_complex(a, -b)}",
                f"z \\cdot \\bar{{z}} = ({z})({self._format_complex(a, -b)})",
                f"= {a}^2 - ({b}i)^2",
                f"= {a**2} - ({b**2})(i^2)",
                f"= {a**2} + {b**2} = {result}"
            ]

        elif problem_type == 'divide':
            # (a + bi) / (c + di) - use conjugate
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            c = random.randint(1, 4)
            d = random.randint(1, 4)

            # Multiply by conjugate
            # (a + bi)(c - di) / (c^2 + d^2)
            num_real = a * c + b * d
            num_imag = b * c - a * d
            denom = c**2 + d**2

            z1 = self._format_complex(a, b)
            z2 = self._format_complex(c, d)

            latex = f"\\text{{Simplify: }} \\frac{{{z1}}}{{{z2}}}"
            solution = f"\\frac{{{num_real}}}{{{denom}}} + \\frac{{{num_imag}}}{{{denom}}}i"

            steps = [
                f"\\text{{Multiply by conjugate: }} \\frac{{{z1}}}{{{z2}}} \\cdot \\frac{{{self._format_complex(c, -d)}}}{{{self._format_complex(c, -d)}}}",
                f"= \\frac{{({a} + {b}i)({c} - {d}i)}}{{({c})^2 + ({d})^2}}",
                f"= \\frac{{{num_real} + {num_imag}i}}{{{denom}}}",
                f"= \\frac{{{num_real}}}{{{denom}}} + \\frac{{{num_imag}}}{{{denom}}}i"
            ]

        else:
            # Power of i
            n = random.randint(5, 50)
            remainder = n % 4
            powers = {0: "1", 1: "i", 2: "-1", 3: "-i"}
            result = powers[remainder]

            latex = f"\\text{{Simplify: }} i^{{{n}}}"
            solution = result

            steps = [
                f"\\text{{Powers of i cycle every 4: }} i^1 = i, i^2 = -1, i^3 = -i, i^4 = 1",
                f"\\text{{Find remainder: }} {n} \\div 4 = {n // 4} \\text{{ R }} {remainder}",
                f"i^{{{n}}} = i^{{{remainder}}} = {result}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = ComplexNumbersGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
