"""
Logarithms Generator
Creates problems about evaluating logarithms and converting forms
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class LogarithmsGenerator:
    """Generates problems about logarithms."""

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
        """Evaluate simple logarithms with integer results"""
        problem_type = random.choice(['base_10', 'base_2', 'base_other'])

        if problem_type == 'base_10':
            exp = random.randint(1, 4)
            value = 10 ** exp

            latex = f"\\text{{Evaluate: }} \\log {value}"
            solution = str(exp)

            steps = [
                f"\\log {value} = x \\text{{ means }} 10^x = {value}",
                f"10^{{{exp}}} = {value}",
                f"\\text{{So }} \\log {value} = {exp}"
            ]

        elif problem_type == 'base_2':
            exp = random.randint(1, 6)
            value = 2 ** exp

            latex = f"\\text{{Evaluate: }} \\log_2 {value}"
            solution = str(exp)

            steps = [
                f"\\log_2 {value} = x \\text{{ means }} 2^x = {value}",
                f"2^{{{exp}}} = {value}",
                f"\\text{{So }} \\log_2 {value} = {exp}"
            ]

        else:
            base = random.choice([3, 4, 5])
            exp = random.randint(1, 3)
            value = base ** exp

            latex = f"\\text{{Evaluate: }} \\log_{{{base}}} {value}"
            solution = str(exp)

            steps = [
                f"\\log_{{{base}}} {value} = x \\text{{ means }} {base}^x = {value}",
                f"{base}^{{{exp}}} = {value}",
                f"\\text{{So }} \\log_{{{base}}} {value} = {exp}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Convert between exponential and logarithmic form"""
        problem_type = random.choice(['exp_to_log', 'log_to_exp'])

        base = random.choice([2, 3, 5, 10])
        exp = random.randint(1, 4)
        value = base ** exp

        if problem_type == 'exp_to_log':
            latex = f"\\text{{Write in logarithmic form: }} {base}^{{{exp}}} = {value}"
            solution = f"\\log_{{{base}}} {value} = {exp}"

            steps = [
                f"\\text{{Exponential form: }} b^x = y",
                f"\\text{{Logarithmic form: }} \\log_b y = x",
                f"{base}^{{{exp}}} = {value} \\Rightarrow \\log_{{{base}}} {value} = {exp}"
            ]
        else:
            latex = f"\\text{{Write in exponential form: }} \\log_{{{base}}} {value} = {exp}"
            solution = f"{base}^{{{exp}}} = {value}"

            steps = [
                f"\\text{{Logarithmic form: }} \\log_b y = x",
                f"\\text{{Exponential form: }} b^x = y",
                f"\\log_{{{base}}} {value} = {exp} \\Rightarrow {base}^{{{exp}}} = {value}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Evaluate logs with fractions or negative exponents"""
        problem_type = random.choice(['fraction', 'negative', 'special'])

        if problem_type == 'fraction':
            base = random.choice([2, 3, 4, 5])
            exp = random.randint(1, 3)
            value = base ** exp

            latex = f"\\text{{Evaluate: }} \\log_{{{base}}} \\frac{{1}}{{{value}}}"
            solution = str(-exp)

            steps = [
                f"\\frac{{1}}{{{value}}} = {base}^{{-{exp}}}",
                f"\\log_{{{base}}} {base}^{{-{exp}}} = -{exp}"
            ]

        elif problem_type == 'negative':
            base = random.choice([2, 3, 5])
            exp = random.randint(1, 3)

            latex = f"\\text{{Evaluate: }} \\log_{{{base}}} {base}^{{-{exp}}}"
            solution = str(-exp)

            steps = [
                f"\\text{{By definition, }} \\log_b b^x = x",
                f"\\log_{{{base}}} {base}^{{-{exp}}} = -{exp}"
            ]

        else:
            # log_b(1) or log_b(b)
            base = random.choice([2, 3, 5, 7, 10])
            special = random.choice(['one', 'base'])

            if special == 'one':
                latex = f"\\text{{Evaluate: }} \\log_{{{base}}} 1"
                solution = "0"
                steps = [
                    f"\\log_b 1 = 0 \\text{{ for any base }} b",
                    f"\\text{{Because }} {base}^0 = 1"
                ]
            else:
                latex = f"\\text{{Evaluate: }} \\log_{{{base}}} {base}"
                solution = "1"
                steps = [
                    f"\\log_b b = 1 \\text{{ for any base }} b",
                    f"\\text{{Because }} {base}^1 = {base}"
                ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Solve logarithmic equations or use properties"""
        problem_type = random.choice(['solve', 'simplify', 'equation'])

        if problem_type == 'solve':
            # log_b(x) = n, find x
            base = random.choice([2, 3, 5])
            n = random.randint(2, 4)
            x = base ** n

            latex = f"\\text{{Solve: }} \\log_{{{base}}} x = {n}"
            solution = str(x)

            steps = [
                f"\\text{{Convert to exponential form:}}",
                f"{base}^{{{n}}} = x",
                f"x = {x}"
            ]

        elif problem_type == 'simplify':
            # Use log properties: log_b(b^x) = x
            base = random.choice([2, 3, 5, 10])
            a = random.randint(2, 4)
            b_exp = random.randint(1, 3)

            latex = f"\\text{{Simplify: }} {base}^{{\\log_{{{base}}} {a}}}"
            solution = str(a)

            steps = [
                f"\\text{{Property: }} b^{{\\log_b x}} = x",
                f"{base}^{{\\log_{{{base}}} {a}}} = {a}"
            ]

        else:
            # log_b(x) + log_b(y) = log_b(xy)
            base = random.choice([2, 10])
            x = random.randint(2, 8)
            y = random.randint(2, 8)
            product = x * y

            if base == 10:
                latex = f"\\text{{Simplify: }} \\log {x} + \\log {y}"
                solution = f"\\log {product}"
            else:
                latex = f"\\text{{Simplify: }} \\log_{{{base}}} {x} + \\log_{{{base}}} {y}"
                solution = f"\\log_{{{base}}} {product}"

            steps = [
                f"\\text{{Product Rule: }} \\log_b x + \\log_b y = \\log_b(xy)",
                f"= \\log_{{{base}}}({x} \\cdot {y})",
                f"= \\log_{{{base}}} {product}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = LogarithmsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
