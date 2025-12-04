"""
Word Problems Standard Form Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WordProblemsStandardFormGenerator:
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
        price_a = random.randint(3, 10)
        price_b = random.randint(2, 8)
        total = random.randint(30, 60)

        latex = f"\\text{{Apples cost \\${price_a}, bananas \\${price_b}. Spent \\${total}. Write equation.}}"
        solution = f"{price_a}a + {price_b}b = {total}"
        steps = [f"Cost of apples: {price_a}a", f"Cost of bananas: {price_b}b", f"Total: {price_a}a + {price_b}b = {total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        wage_adult = random.randint(12, 20)
        wage_child = random.randint(5, 10)
        total = random.randint(100, 200)

        latex = f"\\text{{Adult tickets \\${wage_adult}, child tickets \\${wage_child}, total \\${total}. Write equation.}}"
        solution = f"{wage_adult}a + {wage_child}c = {total}"
        steps = [f"Adult tickets: {wage_adult}a", f"Child tickets: {wage_child}c", f"{wage_adult}a + {wage_child}c = {total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        price_x = random.randint(4, 12)
        price_y = random.randint(3, 10)
        budget = random.randint(50, 100)

        max_x = budget // price_x
        max_y = budget // price_y

        latex = f"\\text{{Items cost \\${price_x} and \\${price_y}, budget \\${budget}. Find max of each if buying only one type.}}"
        solution = f"Max x: {max_x}, Max y: {max_y}"
        steps = [f"Equation: {price_x}x + {price_y}y = {budget}", f"If only x: {budget}/{price_x} = {max_x}", f"If only y: {budget}/{price_y} = {max_y}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        price_a = random.randint(5, 12)
        price_b = random.randint(3, 8)
        total = random.randint(60, 120)
        qty_a = random.randint(3, 8)

        qty_b = (total - price_a * qty_a) / price_b

        latex = f"\\text{{Concert: \\${price_a} VIP, \\${price_b} regular, total \\${total}. If {qty_a} VIP, how many regular?}}"
        solution = f"{qty_b:.0f} \\text{{ regular tickets}}"
        steps = [f"{price_a}({qty_a}) + {price_b}r = {total}", f"{price_a * qty_a} + {price_b}r = {total}", f"{price_b}r = {total - price_a * qty_a}", f"r = {qty_b:.0f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WordProblemsStandardFormGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
