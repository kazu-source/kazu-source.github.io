"""
Inverse Operations Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class InverseOperationsGenerator:
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
        operations = [
            ("addition", "subtraction"),
            ("subtraction", "addition"),
            ("multiplication", "division"),
            ("division", "multiplication")
        ]
        op, inverse = random.choice(operations)

        latex = f"\\text{{What is the inverse of {op}?}}"
        solution = inverse
        steps = [f"The inverse of {op} is {inverse}", f"Answer: {inverse}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(5, 15)

        latex = f"\\text{{What operation undoes adding {a}?}}"
        solution = f"Subtract {a}"
        steps = [f"Inverse of addition is subtraction", f"Answer: Subtract {a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 9)
        b = random.randint(10, 25)

        latex = f"\\text{{To solve }} {a}x = {b}\\text{{, what operation do you use?}}"
        solution = f"Divide both sides by {a}"
        steps = ["Inverse of multiplication is division", f"Answer: Divide both sides by {a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(5, 15)
        c = random.randint(20, 40)

        latex = f"\\text{{List the inverse operations needed to solve }} {a}x + {b} = {c}"
        solution = f"1) Subtract {b}, 2) Divide by {a}"
        steps = [f"First undo addition: subtract {b}", f"Then undo multiplication: divide by {a}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = InverseOperationsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
