"""
Basic Probability Generator - Kindergarten Unit 8
Generates basic probability problems (likely, unlikely, certain, impossible)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class BasicProbabilityGenerator:
    """Generates basic probability problems."""

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
        event = random.choice([
            ('the sun rising tomorrow', 'certain'),
            ('a cat flying', 'impossible')
        ])
        latex = f"\\text{{Is {event[0]} certain or impossible?}}"
        solution = event[1]
        return Equation(latex=latex, solution=solution, steps=[event[1]], difficulty='easy')

    def _generate_medium(self) -> Equation:
        events = [
            ('rolling a 1 on a dice', 'possible'),
            ('picking red from a bag of all red balls', 'certain'),
            ('seeing a dinosaur today', 'impossible')
        ]
        event, answer = random.choice(events)
        latex = f"\\text{{Is {event} certain, possible, or impossible?}}"
        solution = answer
        return Equation(latex=latex, solution=solution, steps=[answer], difficulty='medium')

    def _generate_hard(self) -> Equation:
        red = random.randint(4, 6)
        blue = random.randint(1, 2)
        latex = f"\\text{{A bag has {red} red balls and {blue} blue ball(s). Which color is more likely?}}"
        solution = "red"
        return Equation(latex=latex, solution=solution, steps=["more red balls"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        total = random.randint(4, 6)
        latex = f"\\text{{All {total} marbles in a jar are green. What color will you pick?}}"
        solution = "green"
        return Equation(latex=latex, solution=solution, steps=["certain to be green"], difficulty='challenge')


def main():
    generator = BasicProbabilityGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
