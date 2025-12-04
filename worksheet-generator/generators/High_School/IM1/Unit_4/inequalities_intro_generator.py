"""
Inequalities Intro Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class InequalitiesIntroGenerator:
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
        a = random.randint(1, 15)
        b = random.randint(a + 1, 25)

        latex = f"\\text{{Is }} {a} < {b} \\text{{ true or false?}}"
        solution = "True"
        steps = [f"{a} is less than {b}", "Answer: True"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(5, 20)
        ops = ['<', '>', '\\leq', '\\geq']
        op = random.choice(ops)

        if op == '<':
            b = a - random.randint(1, 5)
            latex = f"\\text{{Is }} {a} < {b} \\text{{ true or false?}}"
            solution = "False"
            steps = [f"{a} is not less than {b}", "Answer: False"]
        elif op == '>':
            b = a - random.randint(1, 5)
            latex = f"\\text{{Is }} {a} > {b} \\text{{ true or false?}}"
            solution = "True"
            steps = [f"{a} is greater than {b}", "Answer: True"]
        elif op == '\\leq':
            b = a
            latex = f"\\text{{Is }} {a} \\leq {b} \\text{{ true or false?}}"
            solution = "True"
            steps = [f"{a} equals {b}", f"{a} \\leq {b} is true", "Answer: True"]
        else:  # >=
            b = a
            latex = f"\\text{{Is }} {a} \\geq {b} \\text{{ true or false?}}"
            solution = "True"
            steps = [f"{a} equals {b}", f"{a} \\geq {b} is true", "Answer: True"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(3, 10)
        b = random.randint(1, 8)
        c = random.randint(5, 15)

        test_val = random.randint(1, 5)
        result = a * test_val + b

        if result < c:
            answer = "Yes"
            latex = f"\\text{{Is }} x = {test_val} \\text{{ a solution to }} {a}x + {b} < {c}?"
            steps = [f"Substitute x = {test_val}", f"{a}({test_val}) + {b} = {result}", f"{result} < {c}", "Answer: Yes"]
        else:
            answer = "No"
            latex = f"\\text{{Is }} x = {test_val} \\text{{ a solution to }} {a}x + {b} < {c}?"
            steps = [f"Substitute x = {test_val}", f"{a}({test_val}) + {b} = {result}", f"{result} \\not< {c}", "Answer: No"]

        solution = answer
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(10, 25)

        latex = f"\\text{{Graph }} x < {a} \\text{{ on a number line}}"
        solution = f"Open circle at {a}, shade left"
        steps = [f"Use open circle at {a}", "Shade all numbers less than {a} (to the left)", "Answer: Open circle at {a}, arrow pointing left"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = InequalitiesIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
