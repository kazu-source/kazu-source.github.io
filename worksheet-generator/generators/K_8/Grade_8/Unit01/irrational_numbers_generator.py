"""
Irrational Numbers Generator - Grade 8 Unit 1
Generates problems identifying and understanding irrational numbers
Example: Classify √2 as rational or irrational
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class IrrationalNumbersGenerator:
    """Generates irrational numbers problems."""

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
        """Generate easy problems: identifying rational vs irrational numbers."""
        numbers = [
            ("\\sqrt{2}", "Irrational", ["\\text{√2 cannot be expressed as a fraction}"]),
            ("\\sqrt{4}", "Rational", ["\\text{√4 = 2, which is a whole number}"]),
            ("\\pi", "Irrational", ["\\text{π cannot be expressed as a fraction}"]),
            ("\\frac{1}{3}", "Rational", ["\\text{1/3 is already a fraction}"]),
            ("0.5", "Rational", ["\\text{0.5 = 1/2, a fraction}"]),
            ("\\sqrt{9}", "Rational", ["\\text{√9 = 3, which is a whole number}"]),
            ("\\sqrt{5}", "Irrational", ["\\text{√5 cannot be expressed as a fraction}"])
        ]

        number, classification, steps = random.choice(numbers)

        latex = f"\\text{{Is }} {number} \\text{{ rational or irrational?}}"
        solution = classification

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: classifying multiple numbers."""
        problems = [
            {
                "question": "\\text{Which of the following is irrational? } \\sqrt{16}, \\sqrt{20}, \\sqrt{25}",
                "solution": "\\sqrt{20}",
                "steps": ["\\sqrt{16} = 4 \\text{ (rational)}", "\\sqrt{25} = 5 \\text{ (rational)}", "\\sqrt{20} \\text{ is irrational}"]
            },
            {
                "question": "\\text{Which is rational? } \\pi, \\sqrt{3}, \\frac{22}{7}",
                "solution": "\\frac{22}{7}",
                "steps": ["\\pi \\text{ is irrational}", "\\sqrt{3} \\text{ is irrational}", "\\frac{22}{7} \\text{ is a fraction (rational)}"]
            },
            {
                "question": "\\text{True or False: All square roots are irrational}",
                "solution": "False",
                "steps": ["\\text{√4 = 2 (rational)}", "\\text{√9 = 3 (rational)}", "\\text{Only square roots of non-perfect squares are irrational}"]
            }
        ]

        problem = random.choice(problems)

        return Equation(
            latex=problem["question"],
            solution=problem["solution"],
            steps=problem["steps"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: operations with irrational numbers."""
        problems = [
            {
                "question": "\\text{Is } \\sqrt{2} + \\sqrt{2} \\text{ rational or irrational?}",
                "solution": "Irrational",
                "steps": ["\\sqrt{2} + \\sqrt{2} = 2\\sqrt{2}", "\\text{2√2 is still irrational}"]
            },
            {
                "question": "\\text{Is } \\sqrt{2} \\times \\sqrt{2} \\text{ rational or irrational?}",
                "solution": "Rational",
                "steps": ["\\sqrt{2} \\times \\sqrt{2} = 2", "\\text{2 is rational}"]
            },
            {
                "question": "\\text{Is } \\pi + 3 \\text{ rational or irrational?}",
                "solution": "Irrational",
                "steps": ["\\text{Adding a rational to an irrational gives an irrational}"]
            },
            {
                "question": "\\text{Between which two integers does } \\sqrt{15} \\text{ lie?}",
                "solution": "3 \\text{ and } 4",
                "steps": ["\\sqrt{9} = 3", "\\sqrt{16} = 4", "\\text{So } 3 < \\sqrt{15} < 4"]
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
        """Generate challenge problems: proving irrationality and complex operations."""
        problems = [
            {
                "question": "\\text{Explain why } \\sqrt{6} \\text{ is irrational}",
                "solution": "\\text{6 is not a perfect square}",
                "steps": [
                    "\\text{If √6 were rational, then √6 = a/b}",
                    "\\text{Then 6 = a²/b², so 6b² = a²}",
                    "\\text{This leads to a contradiction}",
                    "\\text{Therefore √6 is irrational}"
                ]
            },
            {
                "question": "\\text{Is } (\\sqrt{3})^2 + (\\sqrt{5})^2 \\text{ rational or irrational?}",
                "solution": "Rational",
                "steps": [
                    "(\\sqrt{3})^2 = 3",
                    "(\\sqrt{5})^2 = 5",
                    "3 + 5 = 8",
                    "\\text{8 is rational}"
                ]
            },
            {
                "question": "\\text{Can the product of two irrational numbers be rational?}",
                "solution": "Yes",
                "steps": [
                    "\\text{Example: } \\sqrt{2} \\times \\sqrt{2} = 2",
                    "\\text{Both factors are irrational}",
                    "\\text{But the product is 2 (rational)}"
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
    generator = IrrationalNumbersGenerator()

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
