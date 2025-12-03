"""
Functions Review Generator
Creates problems reviewing function notation and evaluation
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class FunctionsReviewGenerator:
    """Generates problems reviewing function concepts."""

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
        """Evaluate f(x) for simple linear functions"""
        a = random.randint(1, 5)
        b = random.randint(-10, 10)
        x_val = random.randint(-5, 5)
        result = a * x_val + b

        if b >= 0:
            func = f"f(x) = {a}x + {b}"
        else:
            func = f"f(x) = {a}x - {abs(b)}"

        latex = f"\\text{{If }} {func}, \\text{{ find }} f({x_val})."
        solution = str(result)

        steps = [
            f"f({x_val}) = {a}({x_val}) + {b}",
            f"f({x_val}) = {a * x_val} + {b}",
            f"f({x_val}) = {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Evaluate quadratic functions or find input from output"""
        problem_type = random.choice(['evaluate', 'find_input'])

        if problem_type == 'evaluate':
            a = random.randint(1, 3)
            b = random.randint(-5, 5)
            c = random.randint(-10, 10)
            x_val = random.randint(-3, 3)
            result = a * x_val**2 + b * x_val + c

            latex = f"\\text{{If }} f(x) = {a}x^2 + {b}x + {c}, \\text{{ find }} f({x_val})."
            solution = str(result)

            steps = [
                f"f({x_val}) = {a}({x_val})^2 + {b}({x_val}) + {c}",
                f"f({x_val}) = {a}({x_val**2}) + {b * x_val} + {c}",
                f"f({x_val}) = {a * x_val**2} + {b * x_val} + {c}",
                f"f({x_val}) = {result}"
            ]
        else:
            # f(x) = ax + b, given f(?) = c, find ?
            a = random.randint(2, 5)
            x_val = random.randint(-5, 5)
            b = random.randint(-10, 10)
            c = a * x_val + b

            if b >= 0:
                func = f"f(x) = {a}x + {b}"
            else:
                func = f"f(x) = {a}x - {abs(b)}"

            latex = f"\\text{{If }} {func}, \\text{{ find }} x \\text{{ when }} f(x) = {c}."
            solution = str(x_val)

            steps = [
                f"{a}x + {b} = {c}",
                f"{a}x = {c - b}",
                f"x = {x_val}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Function composition or piecewise evaluation"""
        problem_type = random.choice(['composition', 'piecewise'])

        if problem_type == 'composition':
            a = random.randint(1, 3)
            b = random.randint(1, 5)
            c = random.randint(1, 3)
            d = random.randint(-5, 5)
            x_val = random.randint(-2, 3)

            # f(x) = ax + b, g(x) = cx + d
            # f(g(x)) = a(cx + d) + b
            g_of_x = c * x_val + d
            f_of_g = a * g_of_x + b

            latex = f"\\text{{If }} f(x) = {a}x + {b} \\text{{ and }} g(x) = {c}x + {d}, \\text{{ find }} f(g({x_val}))."
            solution = str(f_of_g)

            steps = [
                f"\\text{{First find }} g({x_val}) = {c}({x_val}) + {d} = {g_of_x}",
                f"\\text{{Then find }} f({g_of_x}) = {a}({g_of_x}) + {b}",
                f"f(g({x_val})) = {a * g_of_x} + {b} = {f_of_g}"
            ]
        else:
            # Piecewise function
            a = random.randint(1, 3)
            b = random.randint(-5, 5)
            c = random.randint(1, 4)
            threshold = random.randint(0, 2)

            if random.choice([True, False]):
                x_val = random.randint(threshold, threshold + 4)
                result = a * x_val + b
                piece_used = f"{a}x + {b} \\text{{ (since }} x \\geq {threshold})"
            else:
                x_val = random.randint(threshold - 5, threshold - 1)
                result = c * x_val
                piece_used = f"{c}x \\text{{ (since }} x < {threshold})"

            latex = f"\\text{{If }} f(x) = \\begin{{cases}} {c}x & x < {threshold} \\\\ {a}x + {b} & x \\geq {threshold} \\end{{cases}}, \\text{{ find }} f({x_val})."
            solution = str(result)

            steps = [
                f"\\text{{Since }} x = {x_val}, \\text{{ use }} {piece_used}",
                f"f({x_val}) = {result}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Find composite function formula or domain restrictions"""
        problem_type = random.choice(['composite_formula', 'domain'])

        if problem_type == 'composite_formula':
            a = random.randint(1, 3)
            b = random.randint(1, 4)
            c = random.randint(1, 3)

            # f(x) = ax + b, g(x) = x^2 + c
            # g(f(x)) = (ax + b)^2 + c

            latex = f"\\text{{If }} f(x) = {a}x + {b} \\text{{ and }} g(x) = x^2 + {c}, \\text{{ find }} g(f(x))."
            solution = f"({a}x + {b})^2 + {c} = {a**2}x^2 + {2*a*b}x + {b**2 + c}"

            steps = [
                f"g(f(x)) = g({a}x + {b})",
                f"= ({a}x + {b})^2 + {c}",
                f"= {a**2}x^2 + {2*a*b}x + {b**2} + {c}",
                f"= {a**2}x^2 + {2*a*b}x + {b**2 + c}"
            ]
        else:
            # Domain of a function with radical or fraction
            func_type = random.choice(['radical', 'fraction'])

            if func_type == 'radical':
                a = random.randint(1, 3)
                b = random.randint(-10, 10)
                # f(x) = sqrt(ax + b), need ax + b >= 0
                boundary = -b / a

                latex = f"\\text{{Find the domain of }} f(x) = \\sqrt{{{a}x + {b}}}."
                solution = f"x \\geq {-b / a}" if a > 0 else f"x \\leq {-b / a}"

                steps = [
                    f"\\text{{For a square root, the radicand must be }} \\geq 0",
                    f"{a}x + {b} \\geq 0",
                    f"{a}x \\geq {-b}",
                    f"x \\geq {-b / a}"
                ]
            else:
                a = random.randint(1, 3)
                b = random.randint(-5, 5)
                # f(x) = 1/(ax + b), need ax + b ≠ 0
                excluded = -b / a

                latex = f"\\text{{Find the domain of }} f(x) = \\frac{{1}}{{{a}x + {b}}}."
                solution = f"x \\neq {-b / a}"

                steps = [
                    f"\\text{{The denominator cannot equal 0}}",
                    f"{a}x + {b} \\neq 0",
                    f"x \\neq {-b / a}"
                ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = FunctionsReviewGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
