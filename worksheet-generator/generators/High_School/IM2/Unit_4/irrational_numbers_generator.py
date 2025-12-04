"""
Irrational Numbers Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class IrrationalNumbersGenerator:
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
        nums = [2, 3, 5, 6, 7, 8]
        num = random.choice(nums)
        latex = f"\\text{{Is }} \\sqrt{{{num}}} \\text{{ rational or irrational?}}"
        solution = "Irrational"
        steps = [
            f"√{num} is not a perfect square",
            f"√{num} cannot be expressed as a fraction p/q",
            f"Therefore √{num} is irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['identify', 'between'])
        if problem_type == 'identify':
            options = ["π", "√2", "√3", "e"]
            num = random.choice(options)
            latex = f"\\text{{Explain why }} {num} \\text{{ is irrational}}"
            if num == "π":
                solution = "π cannot be expressed as a ratio of integers"
                steps = ["π = 3.14159...", "Decimal never terminates or repeats", "Therefore π is irrational"]
            elif num == "e":
                solution = "e cannot be expressed as a ratio of integers"
                steps = ["e = 2.71828...", "Decimal never terminates or repeats", "Therefore e is irrational"]
            else:
                solution = f"{num} cannot be expressed as a fraction"
                steps = [f"{num} is not a perfect square", "Cannot be written as p/q", f"Therefore {num} is irrational"]
        else:
            n = random.choice([2, 3, 5, 6, 7])
            import math
            lower = int(math.sqrt(n))
            upper = lower + 1
            latex = f"\\text{{Between which two integers is }} \\sqrt{{{n}}}?"
            solution = f"Between {lower} and {upper}"
            steps = [
                f"{lower}² = {lower**2}",
                f"{upper}² = {upper**2}",
                f"Since {lower**2} < {n} < {upper**2}",
                f"√{n} is between {lower} and {upper}"
            ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.choice([2, 3, 5, 7])
        latex = f"\\text{{Is }} {a}\\sqrt{{{b}}} \\text{{ rational or irrational?}}"
        solution = "Irrational"
        steps = [
            f"√{b} is irrational (not a perfect square)",
            f"Product of rational ({a}) and irrational (√{b}) is irrational",
            f"Therefore {a}√{b} is irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        problem_type = random.choice(['sum', 'product'])
        if problem_type == 'sum':
            a = random.randint(1, 5)
            b = random.choice([2, 3, 5])
            latex = f"\\text{{Is }} {a} + \\sqrt{{{b}}} \\text{{ rational or irrational?}}"
            solution = "Irrational"
            steps = [
                f"Assume {a} + √{b} = p/q (rational)",
                f"Then √{b} = p/q - {a} (rational)",
                "But √{b} is irrational - contradiction!",
                f"Therefore {a} + √{b} is irrational"
            ]
        else:
            a = random.choice([2, 3, 5])
            b = random.choice([2, 3, 5])
            latex = f"\\text{{Is }} \\sqrt{{{a}}} \\cdot \\sqrt{{{b}}} \\text{{ rational or irrational?}}"
            product = a * b
            import math
            if math.sqrt(product) == int(math.sqrt(product)):
                solution = f"Rational (equals {int(math.sqrt(product))})"
                steps = [
                    f"√{a} · √{b} = √({a}·{b}) = √{product}",
                    f"√{product} = {int(math.sqrt(product))}",
                    "This is rational"
                ]
            else:
                solution = "Irrational"
                steps = [
                    f"√{a} · √{b} = √({a}·{b}) = √{product}",
                    f"√{product} is irrational",
                    "Product of irrationals can be irrational"
                ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = IrrationalNumbersGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
