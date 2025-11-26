"""
Scientific Notation Word Problems Generator - Grade 8 Unit 2
Generates word problems involving scientific notation
Example: The distance from Earth to the Sun is 93,000,000 miles. Express this in scientific notation.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ScientificNotationWordProblemsGenerator:
    """Generates scientific notation word problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
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
        """Generate easy problems: simple scientific notation conversions."""
        contexts = [
            ("The population of a city is {num}. Express in scientific notation.", "people"),
            ("A computer can perform {num} calculations per second. Express in scientific notation.", "calculations"),
            ("The distance between two cities is {num} meters. Express in scientific notation.", "meters"),
            ("A factory produces {num} items per day. Express in scientific notation.", "items")
        ]

        context, unit = random.choice(contexts)
        coefficient = random.randint(2, 9)
        exponent = random.randint(3, 5)
        number = coefficient * (10 ** exponent)

        latex = f"\\text{{{context.format(num=number)}}}"
        solution = f"{coefficient} \\times 10^{{{exponent}}}"
        steps = [
            f"\\text{{Convert {number} to scientific notation}}",
            f"{number} = {coefficient} \\times 10^{{{exponent}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: operations with scientific notation."""
        problem_types = ['multiply', 'divide', 'add_subtract']
        problem_type = random.choice(problem_types)

        if problem_type == 'multiply':
            coef1 = random.randint(2, 5)
            coef2 = random.randint(2, 5)
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 4)

            result_coef = coef1 * coef2
            result_exp = exp1 + exp2

            # Adjust if coefficient >= 10
            if result_coef >= 10:
                result_exp += 1
                result_coef = result_coef / 10

            latex = f"\\text{{A bacteria colony has }} {coef1} \\times 10^{{{exp1}}} \\text{{ cells. After doubling }} {coef2} \\text{{ times, how many cells are there?}}"
            solution = f"{result_coef} \\times 10^{{{result_exp}}}"
            steps = [
                f"({coef1} \\times 10^{{{exp1}}}) \\times {coef2} = {coef1 * coef2} \\times 10^{{{exp1}}}",
                f"= {result_coef} \\times 10^{{{result_exp}}}"
            ]

        elif problem_type == 'divide':
            coef1 = random.randint(4, 9)
            coef2 = random.randint(2, 3)
            exp1 = random.randint(4, 6)
            exp2 = random.randint(2, 3)

            result_coef = coef1 / coef2
            result_exp = exp1 - exp2

            latex = f"\\text{{The mass of Earth is }} {coef1} \\times 10^{{{exp1}}} \\text{{ kg. The mass of the Moon is }} {coef2} \\times 10^{{{exp2}}} \\text{{ kg. How many times more massive is Earth?}}"
            solution = f"{result_coef} \\times 10^{{{result_exp}}}"
            steps = [
                f"\\frac{{{coef1} \\times 10^{{{exp1}}}}}{{{coef2} \\times 10^{{{exp2}}}}} = \\frac{{{coef1}}}{{{coef2}}} \\times 10^{{{exp1 - exp2}}}",
                f"= {result_coef} \\times 10^{{{result_exp}}}"
            ]
        else:  # add_subtract
            coef1 = random.randint(3, 7)
            coef2 = random.randint(1, 4)
            exp = random.randint(3, 5)

            result_coef = coef1 + coef2

            latex = f"\\text{{City A has }} {coef1} \\times 10^{{{exp}}} \\text{{ residents. City B has }} {coef2} \\times 10^{{{exp}}} \\text{{ residents. What is the total population?}}"
            solution = f"{result_coef} \\times 10^{{{exp}}}"
            steps = [
                f"{coef1} \\times 10^{{{exp}}} + {coef2} \\times 10^{{{exp}}} = ({coef1} + {coef2}) \\times 10^{{{exp}}}",
                f"= {result_coef} \\times 10^{{{exp}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: complex scientific notation word problems."""
        problems = [
            {
                "question": "\\text{Light travels at } 3 \\times 10^8 \\text{ meters per second. How far does light travel in } 5 \\times 10^2 \\text{ seconds?}",
                "solution": "1.5 \\times 10^{11} \\text{ meters}",
                "steps": [
                    "\\text{Distance = Speed × Time}",
                    "(3 \\times 10^8) \\times (5 \\times 10^2) = (3 \\times 5) \\times (10^8 \\times 10^2)",
                    "= 15 \\times 10^{10}",
                    "= 1.5 \\times 10^{11} \\text{ meters}"
                ]
            },
            {
                "question": "\\text{A grain of sand weighs } 7 \\times 10^{-5} \\text{ grams. How much do } 2 \\times 10^6 \\text{ grains weigh?}",
                "solution": "1.4 \\times 10^{2} \\text{ grams}",
                "steps": [
                    "(7 \\times 10^{-5}) \\times (2 \\times 10^6) = (7 \\times 2) \\times (10^{-5} \\times 10^6)",
                    "= 14 \\times 10^{1}",
                    "= 1.4 \\times 10^{2} \\text{ grams}"
                ]
            },
            {
                "question": "\\text{The national debt is } 2.8 \\times 10^{13} \\text{ dollars for } 3.5 \\times 10^8 \\text{ people. What is the debt per person?}",
                "solution": "8 \\times 10^{4} \\text{ dollars}",
                "steps": [
                    "\\frac{2.8 \\times 10^{13}}{3.5 \\times 10^8} = \\frac{2.8}{3.5} \\times 10^{13-8}",
                    "= 0.8 \\times 10^{5}",
                    "= 8 \\times 10^{4} \\text{ dollars}"
                ]
            }
        ]

        problem = random.choice(problems)

        return Equation(
            latex=problem["question"],
            solution=problem["solution"],
            steps=problem["steps"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step scientific notation problems."""
        problems = [
            {
                "question": "\\text{A computer processes } 4 \\times 10^9 \\text{ operations per second. If a program requires } 1.2 \\times 10^{15} \\text{ operations, how many hours will it take?}",
                "solution": "83.\\overline{3} \\text{ hours}",
                "steps": [
                    "\\text{Time in seconds} = \\frac{1.2 \\times 10^{15}}{4 \\times 10^9} = 0.3 \\times 10^{6} = 3 \\times 10^{5} \\text{ seconds}",
                    "\\text{Time in hours} = \\frac{3 \\times 10^{5}}{3600} = \\frac{3 \\times 10^{5}}{3.6 \\times 10^{3}}",
                    "= \\frac{3}{3.6} \\times 10^{2} = 0.8\\overline{3} \\times 10^{2}",
                    "= 83.\\overline{3} \\text{ hours}"
                ]
            },
            {
                "question": "\\text{The Sun's mass is } 2 \\times 10^{30} \\text{ kg. Jupiter's mass is } 1.9 \\times 10^{27} \\text{ kg. How many Jupiters equal the Sun's mass?}",
                "solution": "1052.6 \\text{ or about } 1.05 \\times 10^{3}",
                "steps": [
                    "\\frac{2 \\times 10^{30}}{1.9 \\times 10^{27}} = \\frac{2}{1.9} \\times 10^{30-27}",
                    "= 1.052... \\times 10^{3}",
                    "\\approx 1.05 \\times 10^{3} \\text{ or } 1052.6"
                ]
            },
            {
                "question": "\\text{A byte is } 8 \\text{ bits. A terabyte is } 10^{12} \\text{ bytes. How many bits are in } 2.5 \\text{ terabytes?}",
                "solution": "2 \\times 10^{13} \\text{ bits}",
                "steps": [
                    "\\text{Bits in 1 terabyte} = 8 \\times 10^{12} \\text{ bits}",
                    "\\text{Bits in 2.5 terabytes} = 2.5 \\times (8 \\times 10^{12})",
                    "= 20 \\times 10^{12}",
                    "= 2 \\times 10^{13} \\text{ bits}"
                ]
            }
        ]

        problem = random.choice(problems)

        return Equation(
            latex=problem["question"],
            solution=problem["solution"],
            steps=problem["steps"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ScientificNotationWordProblemsGenerator()

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
