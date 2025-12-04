"""
Polynomial Patterns Factorization Generator (difference of squares, perfect square trinomials, etc.)
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PolynomialPatternsFactorizationGenerator:
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
        # Difference of squares: a^2 - b^2
        a = random.randint(2, 8)
        b = random.randint(2, 8)

        latex = f"{a*a}x^2 - {b*b}"
        solution = f"({a}x + {b})({a}x - {b})"
        steps = [
            f"Recognize difference of squares: a^2 - b^2 = (a+b)(a-b)",
            f"a = {a}x, b = {b}",
            f"({a}x + {b})({a}x - {b})",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Perfect square trinomial
        problem_type = random.choice(['plus', 'minus'])
        a = random.randint(2, 6)
        b = random.randint(2, 6)

        if problem_type == 'plus':
            latex = f"{a*a}x^2 + {2*a*b}x + {b*b}"
            solution = f"({a}x + {b})^2"
            steps = [
                f"Check if perfect square: a^2 + 2ab + b^2",
                f"a = {a}x, b = {b}",
                f"Verify: 2ab = 2({a}x)({b}) = {2*a*b}x ",
                f"Solution: ({a}x + {b})^2"
            ]
        else:
            latex = f"{a*a}x^2 - {2*a*b}x + {b*b}"
            solution = f"({a}x - {b})^2"
            steps = [
                f"Check if perfect square: a^2 - 2ab + b^2",
                f"a = {a}x, b = {b}",
                f"Verify: 2ab = 2({a}x)({b}) = {2*a*b}x ",
                f"Solution: ({a}x - {b})^2"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['sum_cubes', 'diff_cubes'])

        if problem_type == 'sum_cubes':
            # a^3 + b^3 = (a+b)(a^2-ab+b^2)
            a = random.randint(2, 4)
            b = random.randint(2, 4)

            latex = f"{a**3}x^3 + {b**3}"
            solution = f"({a}x + {b})({a*a}x^2 - {a*b}x + {b*b})"
            steps = [
                f"Sum of cubes: a^3 + b^3 = (a+b)(a^2-ab+b^2)",
                f"a = {a}x, b = {b}",
                f"a + b = {a}x + {b}",
                f"a^2 - ab + b^2 = {a*a}x^2 - {a*b}x + {b*b}",
                f"Solution: {solution}"
            ]
        else:
            # a^3 - b^3 = (a-b)(a^2+ab+b^2)
            a = random.randint(2, 4)
            b = random.randint(2, 4)

            latex = f"{a**3}x^3 - {b**3}"
            solution = f"({a}x - {b})({a*a}x^2 + {a*b}x + {b*b})"
            steps = [
                f"Difference of cubes: a^3 - b^3 = (a-b)(a^2+ab+b^2)",
                f"a = {a}x, b = {b}",
                f"a - b = {a}x - {b}",
                f"a^2 + ab + b^2 = {a*a}x^2 + {a*b}x + {b*b}",
                f"Solution: {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex pattern - nested patterns
        a = random.randint(2, 4)
        b = random.randint(2, 4)

        # x^4 - b^4 = (x^2 + b^2)(x^2 - b^2) = (x^2 + b^2)(x+b)(x-b)
        b_sq = b * b
        b_4th = b_sq * b_sq

        latex = f"x^4 - {b_4th}"
        solution = f"(x^2 + {b_sq})(x + {b})(x - {b})"
        steps = [
            f"Difference of squares: (x^2)^2 - ({b_sq})^2",
            f"= (x^2 + {b_sq})(x^2 - {b_sq})",
            f"x^2 - {b_sq} is also difference of squares",
            f"= (x^2 + {b_sq})(x + {b})(x - {b})",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PolynomialPatternsFactorizationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
