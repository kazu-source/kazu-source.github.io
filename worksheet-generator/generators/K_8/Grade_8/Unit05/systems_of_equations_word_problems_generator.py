"""
Systems of Equations Word Problems Generator - Grade 8 Unit 5
Generates word problems requiring systems of equations
Example: Tickets cost $5 for adults, $3 for children. 100 tickets sold for $380. How many of each?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SystemsOfEquationsWordProblemsGenerator:
    """Generates systems of equations word problems."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        x, y = random.randint(5, 15), random.randint(10, 20)
        total = x + y

        latex = f"\\text{{Two numbers sum to }} {total}. \\text{{ One is }} {x}. \\text{{ Find the other.}}"
        solution = f"{y}"
        steps = [f"x + y = {total}", f"{x} + y = {total}", f"y = {y}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        adults = random.randint(10, 30)
        children = random.randint(20, 40)
        adult_price = random.randint(8, 12)
        child_price = random.randint(3, 6)

        total_people = adults + children
        total_revenue = adults * adult_price + children * child_price

        latex = f"\\text{{Tickets: adults $${adult_price}, children $${child_price}. }} {total_people} \\text{{ sold for $${total_revenue}. How many adults?}}"
        solution = f"{adults} \\text{{ adults}}"
        steps = [
            f"a + c = {total_people}",
            f"{adult_price}a + {child_price}c = {total_revenue}",
            f"a = {adults}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        nickels = random.randint(10, 25)
        dimes = random.randint(15, 30)
        total_coins = nickels + dimes
        total_value = nickels * 5 + dimes * 10

        latex = f"\\text{{A piggy bank has }} {total_coins} \\text{{ coins (nickels & dimes) worth }} {total_value}¢. \\text{{ How many nickels?}}"
        solution = f"{nickels} \\text{{ nickels}}"
        steps = [
            f"n + d = {total_coins}",
            f"5n + 10d = {total_value}",
            f"n = {nickels}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        length = random.randint(15, 30)
        width = random.randint(8, 15)
        perimeter = 2 * (length + width)

        latex = f"\\text{{A rectangle's length is }} {length - width} \\text{{ more than width. Perimeter is }} {perimeter}. \\text{{ Find dimensions.}}"
        solution = f"\\text{{Length: }} {length}, \\text{{ Width: }} {width}"
        steps = [
            f"l = w + {length - width}",
            f"2(l + w) = {perimeter}",
            f"w = {width}, l = {length}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = SystemsOfEquationsWordProblemsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
