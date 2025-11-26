"""
Linear Models Generator - Grade 8 Unit 3
Generates problems about creating linear models from real-world situations
Example: A phone plan costs $30/month plus $0.10 per text. Write a function for total cost.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class LinearModelsGenerator:
    """Generates linear models problems."""

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
        rate = random.randint(5, 15)
        initial = random.randint(10, 40)

        latex = f"\\text{{A savings account starts with $${initial} and grows by $${rate}/week. Write a function for the balance.}}"
        solution = f"B(w) = {rate}w + {initial}"
        steps = [
            f"\\text{{Initial amount: }} {initial}",
            f"\\text{{Rate: }} {rate}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        base = random.randint(20, 50)
        rate = random.randint(2, 8)

        latex = f"\\text{{A gym charges $${base} to join plus $${rate}/month. Write a function for total cost after }} m \\text{{ months.}}"
        solution = f"C(m) = {rate}m + {base}"
        steps = [
            f"\\text{{Initial fee: }} {base}",
            f"\\text{{Monthly rate: }} {rate}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        start_temp = random.randint(60, 80)
        decrease = random.randint(2, 5)
        hours = random.randint(3, 6)
        final_temp = start_temp - decrease * hours

        latex = f"\\text{{Temperature is {start_temp}°F and drops {decrease}°F/hour. What is the temperature after {hours} hours?}}"
        solution = f"{final_temp}°F"
        steps = [
            f"T(h) = {start_temp} - {decrease}h",
            f"T({hours}) = {start_temp} - {decrease}({hours})",
            f"T({hours}) = {final_temp}°F"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        rate = random.randint(40, 70)
        initial_dist = random.randint(100, 300)

        latex = f"\\text{{A car is {initial_dist} miles away and travels toward you at {rate} mph. Write a function for distance from you.}}"
        solution = f"D(t) = {initial_dist} - {rate}t"
        steps = [
            f"\\text{{Initial distance: }} {initial_dist}",
            f"\\text{{Approaching at: }} {rate} \\text{{ mph}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = LinearModelsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
