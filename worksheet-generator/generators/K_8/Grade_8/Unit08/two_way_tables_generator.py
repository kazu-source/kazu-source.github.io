"""
Two-Way Tables Generator - Grade 8 Unit 8
Generates problems about two-way tables and relative frequency
Example: Given a two-way table, find the relative frequency.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class TwoWayTablesGenerator:
    """Generates two-way tables problems."""

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
        boys_like = random.randint(15, 25)
        boys_dislike = random.randint(10, 15)
        girls_like = random.randint(20, 30)
        girls_dislike = random.randint(8, 12)

        total_like = boys_like + girls_like
        total = boys_like + boys_dislike + girls_like + girls_dislike

        latex = f"\\text{{Survey: Boys who like pizza: }} {boys_like}, \\text{{ dislike: }} {boys_dislike}. \\text{{ Girls who like: }} {girls_like}, \\text{{ dislike: }} {girls_dislike}. \\text{{ Total who like pizza?}}"
        solution = f"{total_like}"
        steps = [
            f"{boys_like} + {girls_like} = {total_like}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b, c, d = random.randint(20, 40), random.randint(15, 30), random.randint(25, 45), random.randint(10, 25)
        total = a + b + c + d

        latex = f"\\text{{Two-way table with values: }} {a}, {b}, {c}, {d}. \\text{{ Find relative frequency of }} {a}."
        rel_freq = a / total
        solution = f"{rel_freq:.2f} \\text{{ or }} \\frac{{{a}}}{{{total}}}"
        steps = [
            f"\\text{{Total}} = {total}",
            f"\\text{{Relative frequency}} = \\frac{{{a}}}{{{total}}} = {rel_freq:.2f}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        male_yes = random.randint(30, 50)
        male_no = random.randint(20, 35)
        female_yes = random.randint(40, 60)
        female_no = random.randint(15, 30)

        total_yes = male_yes + female_yes
        total = male_yes + male_no + female_yes + female_no

        latex = f"\\text{{Survey results - Males yes: }} {male_yes}, \\text{{ no: }} {male_no}. \\text{{ Females yes: }} {female_yes}, \\text{{ no: }} {female_no}. \\text{{ What percent said yes?}}"
        percent = (total_yes / total) * 100
        solution = f"{percent:.1f}\\%"
        steps = [
            f"\\text{{Total yes}} = {male_yes} + {female_yes} = {total_yes}",
            f"\\text{{Total}} = {total}",
            f"\\frac{{{total_yes}}}{{{total}}} \\times 100 = {percent:.1f}\\%"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        cat_indoor = random.randint(25, 40)
        cat_outdoor = random.randint(15, 25)
        dog_indoor = random.randint(30, 50)
        dog_outdoor = random.randint(20, 35)

        total_cats = cat_indoor + cat_outdoor
        total = cat_indoor + cat_outdoor + dog_indoor + dog_outdoor

        latex = f"\\text{{Pet survey: Cats indoor }} {cat_indoor}, \\text{{ outdoor }} {cat_outdoor}. \\text{{ Dogs indoor }} {dog_indoor}, \\text{{ outdoor }} {dog_outdoor}. \\text{{ Find conditional probability: P(indoor|cat)?}}"
        cond_prob = cat_indoor / total_cats
        solution = f"{cond_prob:.2f} \\text{{ or }} \\frac{{{cat_indoor}}}{{{total_cats}}}"
        steps = [
            f"\\text{{Total cats}} = {total_cats}",
            f"P(\\text{{indoor}}|\\text{{cat}}) = \\frac{{{cat_indoor}}}{{{total_cats}}} = {cond_prob:.2f}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = TwoWayTablesGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
