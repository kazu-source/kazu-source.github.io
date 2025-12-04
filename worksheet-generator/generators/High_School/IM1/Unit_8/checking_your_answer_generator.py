"""
Checking Your Answer Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CheckingYourAnswerGenerator:
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
        x_val = random.randint(2, 6)
        y_val = random.randint(1, 5)
        c = x_val + y_val

        latex = f"\\text{{Check if }} ({x_val}, {y_val}) \\text{{ solves }} x + y = {c}"
        solution = "Yes"
        steps = [f"Substitute: {x_val} + {y_val} = {c}", f"{x_val + y_val} = {c}", "Answer: Yes"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(2, 6)
        y_val = random.randint(1, 5)
        a = random.randint(2, 5)
        b = random.randint(1, 3)

        c1 = x_val + y_val
        c2 = a * x_val + b * y_val

        latex = f"\\text{{Check if }} ({x_val}, {y_val}) \\text{{ solves }} x + y = {c1}, {a}x + {b}y = {c2}"
        solution = "Yes"
        steps = [f"First: {x_val} + {y_val} = {c1} ✓", f"Second: {a}({x_val}) + {b}({y_val}) = {c2} ✓", "Answer: Yes, both check"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(2, 5)
        y_val = random.randint(3, 7)
        wrong_y = y_val + random.randint(1, 3)

        c1 = x_val + y_val
        c2 = 2 * x_val + wrong_y

        latex = f"\\text{{Check if }} ({x_val}, {wrong_y}) \\text{{ solves }} x + y = {c1}, 2x + y = {c2}"
        solution = "No"
        steps = [f"First: {x_val} + {wrong_y} = {x_val + wrong_y} ≠ {c1}", "First equation fails", "Answer: No"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{Why must you check solutions in BOTH equations?}}"
        solution = "A point might satisfy one but not the other"
        steps = ["System solution must work for ALL equations", "Checking only one equation is insufficient", "Answer: Must satisfy both equations"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CheckingYourAnswerGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
