"""
Expression vs Equation Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ExpressionVsEquationGenerator:
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
        is_equation = random.choice([True, False])

        if is_equation:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 20)
            latex = f"\\text{{Is }} {a}x + {b} = {c} \\text{{ an expression or equation?}}"
            solution = "equation"
            steps = ["Contains an equals sign", "Answer: equation"]
        else:
            a = random.randint(2, 10)
            b = random.randint(1, 15)
            latex = f"\\text{{Is }} {a}x - {b} \\text{{ an expression or equation?}}"
            solution = "expression"
            steps = ["No equals sign", "Answer: expression"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['classify_multiple', 'definition'])

        if problem_type == 'classify_multiple':
            a = random.randint(2, 8)
            b = random.randint(1, 12)
            c = random.randint(1, 15)
            item1 = f"{a}x + {b}"
            item2 = f"{a}x = {c}"
            latex = f"\\text{{Classify: (a) }} {item1} \\text{{ (b) }} {item2}"
            solution = "(a) expression, (b) equation"
            steps = ["(a) No equals sign - expression", "(b) Has equals sign - equation"]
        else:
            latex = "\\text{What makes an equation different from an expression?}"
            solution = "An equation has an equals sign"
            steps = ["Expressions are mathematical phrases", "Equations are mathematical sentences with =", "Answer: An equation has an equals sign"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(1, 10)
        c = random.randint(1, 12)
        d = random.randint(1, 15)

        item1 = f"{a}x + {b} - {c}"
        item2 = f"{a}x + {b} = {d}"
        item3 = f"{a}({b}x - {c})"

        latex = f"\\text{{Classify each: (a) }} {item1} \\text{{ (b) }} {item2} \\text{{ (c) }} {item3}"
        solution = "(a) expression, (b) equation, (c) expression"
        steps = ["(a) No equals sign - expression", "(b) Has equals sign - equation", "(c) No equals sign - expression"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 9)
        c = random.randint(1, 10)
        d = random.randint(1, 12)

        latex = f"\\text{{Write an expression and an equation using }} {a}x \\text{{ and }} {b}"
        solution = f"Expression example: {a}x + {b}, Equation example: {a}x + {b} = {c+b}"
        steps = [f"Expression (no =): {a}x + {b}", f"Equation (has =): {a}x + {b} = {c+b}", "Answers may vary"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ExpressionVsEquationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
