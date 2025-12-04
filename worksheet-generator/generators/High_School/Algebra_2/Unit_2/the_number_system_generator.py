"""
The Number System Generator (rational, irrational, real numbers)
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class TheNumberSystemGenerator:
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
        problem_type = random.choice(['classify_rational', 'classify_irrational'])

        if problem_type == 'classify_rational':
            num = random.randint(1, 20)
            denom = random.randint(2, 10)
            latex = f"\\text{{Classify: }} \\frac{{{num}}}{{{denom}}}"
            solution = "\\text{Rational}"
            steps = [
                f"This is a fraction of two integers",
                f"All fractions are rational numbers",
                "Answer: Rational"
            ]
        else:
            num = random.choice([2, 3, 5, 7, 11])
            latex = f"\\text{{Classify: }} \\sqrt{{{num}}}"
            solution = "\\text{Irrational}"
            steps = [
                f"\\sqrt{{{num}}} cannot be expressed as a fraction",
                f"\\sqrt{{{num}}} has non-repeating, non-terminating decimals",
                "Answer: Irrational"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['evaluate_expression', 'compare_numbers'])

        if problem_type == 'evaluate_expression':
            a = random.randint(2, 6)
            b = random.randint(1, 5)
            c = random.randint(1, 8)
            latex = f"\\text{{Is }} {a}\\sqrt{{{b}}} + {c} \\text{{ rational or irrational?}}"
            solution = "\\text{Irrational}"
            steps = [
                f"\\sqrt{{{b}}} is irrational",
                f"{a}\\sqrt{{{b}}} is irrational (irrational \\times rational)",
                f"Irrational + rational = irrational",
                "Answer: Irrational"
            ]
        else:
            num1 = random.choice([2, 3, 5])
            num2 = random.choice([7, 11, 13])
            latex = f"\\text{{Order: }} \\sqrt{{{num1}}}, \\sqrt{{{num2}}}, {random.randint(2, 4)}"
            solution = f"\\sqrt{{{num1}}} < {random.randint(2, 4)} < \\sqrt{{{num2}}}"
            steps = [
                f"\\sqrt{{{num1}}} \\approx {round(num1**0.5, 2)}",
                f"\\sqrt{{{num2}}} \\approx {round(num2**0.5, 2)}",
                f"Order from least to greatest: {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['simplify_radicals', 'operations'])

        if problem_type == 'simplify_radicals':
            perfect_square = random.choice([4, 9, 16, 25])
            non_perfect = random.choice([2, 3, 5, 7])
            num = perfect_square * non_perfect

            latex = f"\\text{{Simplify: }} \\sqrt{{{num}}}"
            solution = f"{int(perfect_square**0.5)}\\sqrt{{{non_perfect}}}"
            steps = [
                f"\\sqrt{{{num}}} = \\sqrt{{{perfect_square} \\cdot {non_perfect}}}",
                f"= \\sqrt{{{perfect_square}}} \\cdot \\sqrt{{{non_perfect}}}",
                f"= {int(perfect_square**0.5)}\\sqrt{{{non_perfect}}}",
                f"Answer: {solution}"
            ]
        else:
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            num = random.choice([2, 3, 5])
            latex = f"\\text{{Rationalize: }} \\frac{{{a}}}{{\\sqrt{{{num}}}}}"
            solution = f"\\frac{{{a}\\sqrt{{{num}}}}}{{{num}}}"
            steps = [
                f"Multiply by \\frac{{\\sqrt{{{num}}}}}{{\\sqrt{{{num}}}}}",
                f"= \\frac{{{a} \\cdot \\sqrt{{{num}}}}}{{\\sqrt{{{num}}} \\cdot \\sqrt{{{num}}}}}",
                f"= \\frac{{{a}\\sqrt{{{num}}}}}{{{num}}}",
                f"Answer: {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        problem_type = random.choice(['complex_rationalize', 'nested_radicals'])

        if problem_type == 'complex_rationalize':
            a = random.randint(1, 4)
            b = random.randint(1, 4)
            c = random.choice([2, 3, 5])
            latex = f"\\text{{Rationalize: }} \\frac{{{a}}}{{{b} + \\sqrt{{{c}}}}}"
            numerator = f"{a*b} - {a}\\sqrt{{{c}}}"
            denominator = b*b - c
            solution = f"\\frac{{{numerator}}}{{{denominator}}}"
            steps = [
                f"Multiply by conjugate: \\frac{{{b} - \\sqrt{{{c}}}}}{{{b} - \\sqrt{{{c}}}}}",
                f"Numerator: {a}({b} - \\sqrt{{{c}}}) = {numerator}",
                f"Denominator: ({b})^2 - (\\sqrt{{{c}}})^2 = {b*b} - {c} = {denominator}",
                f"Answer: {solution}"
            ]
        else:
            inner = random.choice([4, 9, 16])
            outer_mult = random.randint(2, 4)
            latex = f"\\text{{Simplify: }} \\sqrt{{{outer_mult} + \\sqrt{{{inner}}}}}"
            solution = f"\\sqrt{{{outer_mult} + {int(inner**0.5)}}}"
            steps = [
                f"Simplify inner radical: \\sqrt{{{inner}}} = {int(inner**0.5)}",
                f"Substitute: \\sqrt{{{outer_mult} + {int(inner**0.5)}}}",
                f"Answer: {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = TheNumberSystemGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
