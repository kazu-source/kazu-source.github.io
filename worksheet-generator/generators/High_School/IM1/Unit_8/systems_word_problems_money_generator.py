"""
Systems Word Problems Money Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SystemsWordProblemsMoneyGenerator:
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
        price_a = random.randint(3, 8)
        price_b = random.randint(2, 6)
        qty_a = random.randint(3, 8)
        qty_b = random.randint(4, 10)
        total_cost = price_a * qty_a + price_b * qty_b
        total_items = qty_a + qty_b

        latex = f"\\text{{Bought {total_items} items for \\${total_cost}. Apples \\${price_a}, bananas \\${price_b}. How many each?}}"
        solution = f"{qty_a} apples, {qty_b} bananas"
        steps = [f"a + b = {total_items}", f"{price_a}a + {price_b}b = {total_cost}", f"Solve: a = {qty_a}, b = {qty_b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        price_adult = random.randint(10, 20)
        price_child = random.randint(5, 10)
        adults = random.randint(3, 8)
        children = random.randint(5, 12)
        total_people = adults + children
        total_cost = price_adult * adults + price_child * children

        latex = f"\\text{{{total_people} tickets for \\${total_cost}. Adults \\${price_adult}, children \\${price_child}. How many each?}}"
        solution = f"{adults} adults, {children} children"
        steps = [f"a + c = {total_people}", f"{price_adult}a + {price_child}c = {total_cost}", f"a = {adults}, c = {children}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        price_x = random.randint(8, 15)
        price_y = random.randint(4, 10)
        qty_x = random.randint(4, 10)
        qty_y = random.randint(6, 14)
        total = qty_x + qty_y
        cost = price_x * qty_x + price_y * qty_y

        latex = f"\\text{{Store sold {total} items for \\${cost}. Item X: \\${price_x}, Item Y: \\${price_y}. Find quantities.}}"
        solution = f"X: {qty_x}, Y: {qty_y}"
        steps = [f"x + y = {total}", f"{price_x}x + {price_y}y = {cost}", f"Solve system", f"x = {qty_x}, y = {qty_y}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        nickels = random.randint(8, 20)
        dimes = random.randint(6, 15)
        total_coins = nickels + dimes
        total_cents = 5 * nickels + 10 * dimes
        total_dollars = total_cents / 100

        latex = f"\\text{{{total_coins} coins worth \\${total_dollars:.2f}. Only nickels and dimes. How many each?}}"
        solution = f"{nickels} nickels, {dimes} dimes"
        steps = [f"n + d = {total_coins}", f"5n + 10d = {total_cents}", f"Solve: n = {nickels}, d = {dimes}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SystemsWordProblemsMoneyGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
