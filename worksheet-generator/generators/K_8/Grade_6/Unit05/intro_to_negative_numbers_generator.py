"""
Intro to Negative Numbers Generator - Grade 6 Unit 5
Generates problems introducing negative numbers
Example: What is the opposite of 5?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IntroToNegativeNumbersGenerator:
    """Generates intro to negative numbers problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy problems: identifying opposites."""
        number = random.randint(1, 20)

        if random.choice([True, False]):
            latex = f"\\text{{What is the opposite of }} {number}\\text{{?}}"
            solution = f"-{number}"
        else:
            latex = f"\\text{{What is the opposite of }} -{number}\\text{{?}}"
            solution = str(number)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{The opposite is }} {solution}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: real-world contexts."""
        contexts = [
            ("temperature drops", "degrees", "below zero"),
            ("elevation", "feet", "below sea level"),
            ("money owed", "dollars", "debt"),
            ("time before event", "hours", "ago")
        ]

        context, unit, negative_term = random.choice(contexts)
        amount = random.randint(5, 50)

        latex = f"\\text{{A {context} of {amount} {unit} {negative_term}. Write this as an integer.}}"
        solution = f"-{amount}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{negative_term.capitalize()} is represented by }} -{amount}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: comparing positive and negative."""
        num1 = random.randint(5, 20)
        num2 = random.randint(5, 20)

        choices = [
            (num1, -num2, ">"),
            (-num1, num2, "<"),
            (-num1, -num2, "<" if num1 > num2 else ">")
        ]

        val1, val2, comp = random.choice(choices)

        latex = f"\\text{{Compare using }} <, >, \\text{{ or }} =: {val1} \\quad ? \\quad {val2}"
        solution = f"{val1} {comp} {val2}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{val1} {comp} {val2}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: ordering integers."""
        numbers = []
        # Add some positive and negative numbers
        for _ in range(2):
            numbers.append(random.randint(1, 15))
        for _ in range(2):
            numbers.append(-random.randint(1, 15))

        random.shuffle(numbers)
        sorted_nums = sorted(numbers)

        nums_str = ", ".join([str(n) for n in numbers])
        sorted_str = ", ".join([str(n) for n in sorted_nums])

        latex = f"\\text{{Order from least to greatest: }} {nums_str}"
        solution = sorted_str

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Ordered: }} {sorted_str}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = IntroToNegativeNumbersGenerator()

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
