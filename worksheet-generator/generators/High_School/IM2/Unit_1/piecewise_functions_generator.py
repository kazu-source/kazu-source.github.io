"""
Piecewise Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PiecewiseFunctionsGenerator:
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
        problem_type = random.choice(['evaluate', 'simple_evaluate'])

        if problem_type == 'evaluate':
            a = random.randint(1, 5)
            b = random.randint(-5, 5)
            c = random.randint(1, 5)
            threshold = random.randint(-2, 2)
            x_val = random.choice([threshold - 2, threshold + 2])

            latex = f"\\text{{Evaluate }} f({x_val}) \\text{{ where }} f(x) = \\begin{{cases}} {a}x {'+' if b >= 0 else ''} {b} & x < {threshold} \\\\ {c} & x \\geq {threshold} \\end{{cases}}"

            if x_val < threshold:
                result = a * x_val + b
                steps = [
                    f"Since {x_val} < {threshold}, use f(x) = {a}x {'+' if b >= 0 else ''} {b}",
                    f"f({x_val}) = {a}({x_val}) {'+' if b >= 0 else ''} {b}",
                    f"f({x_val}) = {a * x_val} {'+' if b >= 0 else ''} {b}",
                    f"f({x_val}) = {result}"
                ]
            else:
                result = c
                steps = [
                    f"Since {x_val} ≥ {threshold}, use f(x) = {c}",
                    f"f({x_val}) = {c}"
                ]

            solution = str(result)
        else:  # simple_evaluate
            m1 = random.randint(1, 4)
            m2 = random.randint(-4, -1)
            threshold = 0
            x_val = random.choice([-3, -2, -1, 1, 2, 3])

            latex = f"\\text{{Evaluate }} f({x_val}) \\text{{ where }} f(x) = \\begin{{cases}} {m1}x & x < 0 \\\\ {m2}x & x \\geq 0 \\end{{cases}}"

            if x_val < 0:
                result = m1 * x_val
                steps = [
                    f"Since {x_val} < 0, use f(x) = {m1}x",
                    f"f({x_val}) = {m1}({x_val})",
                    f"f({x_val}) = {result}"
                ]
            else:
                result = m2 * x_val
                steps = [
                    f"Since {x_val} ≥ 0, use f(x) = {m2}x",
                    f"f({x_val}) = {m2}({x_val})",
                    f"f({x_val}) = {result}"
                ]

            solution = str(result)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['three_pieces', 'quadratic_piece'])

        if problem_type == 'three_pieces':
            a = random.randint(1, 4)
            c = random.randint(-5, 5)
            t1 = random.randint(-2, 0)
            t2 = random.randint(1, 3)
            x_val = random.choice([t1 - 2, t1, t2, t2 + 2])

            latex = f"\\text{{Evaluate }} f({x_val}) \\text{{ where }} f(x) = \\begin{{cases}} {a}x & x < {t1} \\\\ {c} & {t1} \\leq x < {t2} \\\\ -{a}x & x \\geq {t2} \\end{{cases}}"

            if x_val < t1:
                result = a * x_val
                steps = [
                    f"Since {x_val} < {t1}, use f(x) = {a}x",
                    f"f({x_val}) = {a}({x_val})",
                    f"f({x_val}) = {result}"
                ]
            elif x_val < t2:
                result = c
                steps = [
                    f"Since {t1} ≤ {x_val} < {t2}, use f(x) = {c}",
                    f"f({x_val}) = {c}"
                ]
            else:
                result = -a * x_val
                steps = [
                    f"Since {x_val} ≥ {t2}, use f(x) = -{a}x",
                    f"f({x_val}) = -{a}({x_val})",
                    f"f({x_val}) = {result}"
                ]

            solution = str(result)
        else:  # quadratic_piece
            a = random.randint(1, 3)
            b = random.randint(1, 5)
            threshold = random.randint(0, 2)
            x_val = random.choice([threshold - 2, threshold + 2])

            latex = f"\\text{{Evaluate }} f({x_val}) \\text{{ where }} f(x) = \\begin{{cases}} x^2 {'+' if a >= 0 else ''} {a} & x < {threshold} \\\\ {b}x & x \\geq {threshold} \\end{{cases}}"

            if x_val < threshold:
                result = x_val**2 + a
                steps = [
                    f"Since {x_val} < {threshold}, use f(x) = x² {'+' if a >= 0 else ''} {a}",
                    f"f({x_val}) = ({x_val})² {'+' if a >= 0 else ''} {a}",
                    f"f({x_val}) = {x_val**2} {'+' if a >= 0 else ''} {a}",
                    f"f({x_val}) = {result}"
                ]
            else:
                result = b * x_val
                steps = [
                    f"Since {x_val} ≥ {threshold}, use f(x) = {b}x",
                    f"f({x_val}) = {b}({x_val})",
                    f"f({x_val}) = {result}"
                ]

            solution = str(result)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['find_domain_range', 'absolute_value_piece'])

        if problem_type == 'find_domain_range':
            m1 = random.randint(1, 3)
            b1 = random.randint(-3, 3)
            c = random.randint(-5, 5)
            threshold = random.randint(-1, 2)

            # Calculate values at boundary
            left_val = m1 * threshold + b1

            latex = f"\\text{{Find the range of }} f(x) = \\begin{{cases}} {m1}x {'+' if b1 >= 0 else ''} {b1} & x < {threshold} \\\\ {c} & x \\geq {threshold} \\end{{cases}}"

            # For x < threshold, the function approaches m1*threshold + b1 from below
            # For x >= threshold, the function is constant c
            if m1 > 0:
                range_desc = f"(-\\infty, {left_val}) \\cup \\{{{c}\\}}"
            else:
                range_desc = f"({left_val}, \\infty) \\cup \\{{{c}\\}}"

            solution = range_desc
            steps = [
                f"For x < {threshold}: f(x) = {m1}x {'+' if b1 >= 0 else ''} {b1}",
                f"As x → -∞, f(x) → {'−∞' if m1 > 0 else '+∞'}",
                f"As x → {threshold}⁻, f(x) → {left_val}",
                f"For x ≥ {threshold}: f(x) = {c}",
                f"Range: {range_desc}"
            ]
        else:  # absolute_value_piece
            a = random.randint(2, 5)
            b = random.randint(1, 4)
            threshold = random.randint(-2, 2)
            x_val = random.choice([threshold - 2, threshold + 1])

            latex = f"\\text{{Evaluate }} f({x_val}) \\text{{ where }} f(x) = \\begin{{cases}} |x {'+' if threshold >= 0 else ''} {-threshold}| & x < {threshold} \\\\ {a}x {'+' if b >= 0 else ''} {b} & x \\geq {threshold} \\end{{cases}}"

            if x_val < threshold:
                abs_val = abs(x_val + (-threshold))
                result = abs_val
                steps = [
                    f"Since {x_val} < {threshold}, use f(x) = |x {'+' if threshold >= 0 else ''} {-threshold}|",
                    f"f({x_val}) = |{x_val} {'+' if threshold >= 0 else ''} {-threshold}|",
                    f"f({x_val}) = |{x_val - threshold}|",
                    f"f({x_val}) = {result}"
                ]
            else:
                result = a * x_val + b
                steps = [
                    f"Since {x_val} ≥ {threshold}, use f(x) = {a}x {'+' if b >= 0 else ''} {b}",
                    f"f({x_val}) = {a}({x_val}) {'+' if b >= 0 else ''} {b}",
                    f"f({x_val}) = {a * x_val} {'+' if b >= 0 else ''} {b}",
                    f"f({x_val}) = {result}"
                ]

            solution = str(result)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        problem_type = random.choice(['continuity', 'complex_evaluation'])

        if problem_type == 'continuity':
            m = random.randint(2, 5)
            threshold = random.randint(1, 4)
            # For continuity: m*threshold + b = threshold^2 + c
            # We'll find b when c is chosen
            c = random.randint(-3, 3)
            b = threshold**2 + c - m * threshold

            latex = f"\\text{{Is }} f(x) = \\begin{{cases}} {m}x {'+' if b >= 0 else ''} {b} & x < {threshold} \\\\ x^2 {'+' if c >= 0 else ''} {c} & x \\geq {threshold} \\end{{cases}} \\text{{ continuous at }} x = {threshold}?"

            left_limit = m * threshold + b
            right_limit = threshold**2 + c
            is_continuous = (left_limit == right_limit)

            solution = "Yes, continuous" if is_continuous else "No, discontinuous"
            steps = [
                f"Check if lim(x→{threshold}⁻) f(x) = lim(x→{threshold}⁺) f(x) = f({threshold})",
                f"Left limit: lim(x→{threshold}⁻) = {m}({threshold}) {'+' if b >= 0 else ''} {b} = {left_limit}",
                f"Right limit: lim(x→{threshold}⁺) = ({threshold})² {'+' if c >= 0 else ''} {c} = {right_limit}",
                f"f({threshold}) = {right_limit} (using x ≥ {threshold} piece)",
                f"Since limits {'match' if is_continuous else 'do not match'}: {solution}"
            ]
        else:  # complex_evaluation
            a = random.randint(2, 4)
            b = random.randint(1, 3)
            c = random.randint(-4, 4)
            t1 = random.randint(-2, 0)
            t2 = random.randint(2, 4)
            x_val = random.choice([t1 - 1, t1, t2 - 1, t2 + 1])

            latex = f"\\text{{Evaluate }} f({x_val}) \\text{{ where }} f(x) = \\begin{{cases}} x^2 {'-' if a >= 0 else '+'} {abs(a)} & x < {t1} \\\\ {b}x {'+' if c >= 0 else ''} {c} & {t1} \\leq x < {t2} \\\\ -x^2 {'+' if a >= 0 else ''} {a} & x \\geq {t2} \\end{{cases}}"

            if x_val < t1:
                result = x_val**2 - a
                steps = [
                    f"Since {x_val} < {t1}, use f(x) = x² - {a}",
                    f"f({x_val}) = ({x_val})² - {a}",
                    f"f({x_val}) = {x_val**2} - {a}",
                    f"f({x_val}) = {result}"
                ]
            elif x_val < t2:
                result = b * x_val + c
                steps = [
                    f"Since {t1} ≤ {x_val} < {t2}, use f(x) = {b}x {'+' if c >= 0 else ''} {c}",
                    f"f({x_val}) = {b}({x_val}) {'+' if c >= 0 else ''} {c}",
                    f"f({x_val}) = {b * x_val} {'+' if c >= 0 else ''} {c}",
                    f"f({x_val}) = {result}"
                ]
            else:
                result = -x_val**2 + a
                steps = [
                    f"Since {x_val} ≥ {t2}, use f(x) = -x² + {a}",
                    f"f({x_val}) = -({x_val})² + {a}",
                    f"f({x_val}) = -{x_val**2} + {a}",
                    f"f({x_val}) = {result}"
                ]

            solution = str(result)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PiecewiseFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
