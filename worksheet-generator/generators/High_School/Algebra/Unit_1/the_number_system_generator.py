"""
The Number System Generator
Generates problems about classifying numbers (natural, whole, integers, rational, irrational, real)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class TheNumberSystemGenerator:
    """Generates number system classification problems."""

    NUMBER_TYPES = {
        'natural': {
            'description': 'counting numbers starting from 1',
            'examples': [1, 2, 3, 4, 5, 10, 25, 100],
            'symbol': '\\mathbb{N}'
        },
        'whole': {
            'description': 'natural numbers plus zero',
            'examples': [0, 1, 2, 3, 4, 5, 10, 25],
            'symbol': '\\mathbb{W}'
        },
        'integer': {
            'description': 'whole numbers and their negatives',
            'examples': [-5, -3, -1, 0, 1, 3, 5, 10],
            'symbol': '\\mathbb{Z}'
        },
        'rational': {
            'description': 'numbers that can be written as a fraction',
            'examples': ['1/2', '3/4', '-2/3', '0.5', '0.75', '-1.5', '2', '-3'],
            'symbol': '\\mathbb{Q}'
        },
        'irrational': {
            'description': 'numbers that cannot be written as a fraction',
            'examples': ['\\pi', '\\sqrt{2}', '\\sqrt{3}', '\\sqrt{5}', 'e'],
            'symbol': '\\mathbb{Q}^c'
        },
        'real': {
            'description': 'all rational and irrational numbers',
            'examples': ['any number on the number line'],
            'symbol': '\\mathbb{R}'
        }
    }

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
        """Generate easy: Basic classification of simple numbers."""
        problem_type = random.choice(['classify', 'identify', 'true_false'])

        if problem_type == 'classify':
            # Classify a simple number
            num_type = random.choice(['natural', 'whole', 'integer'])
            if num_type == 'natural':
                num = random.randint(1, 20)
                solution = "Natural, Whole, Integer, Rational, Real"
            elif num_type == 'whole':
                num = 0
                solution = "Whole, Integer, Rational, Real"
            else:
                num = random.randint(-10, -1)
                solution = "Integer, Rational, Real"

            latex = f"\\text{{Classify the number: }} {num}"
            steps = [f"\\text{{{num} belongs to: {solution}}}"]

        elif problem_type == 'identify':
            # Which set does this number belong to?
            num = random.randint(1, 10)
            latex = f"\\text{{Is }} {num} \\text{{ a natural number?}}"
            solution = "Yes"
            steps = [f"\\text{{{num} is a counting number, so it is natural}}"]

        else:  # true_false
            statements = [
                ("All natural numbers are whole numbers", "True"),
                ("Zero is a natural number", "False"),
                ("Negative numbers are integers", "True"),
                ("All integers are natural numbers", "False"),
            ]
            statement, answer = random.choice(statements)
            latex = f"\\text{{True or False: {statement}}}"
            solution = answer
            steps = [f"\\text{{This statement is {answer.lower()}}}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium: Rational numbers and fractions."""
        problem_type = random.choice(['classify_fraction', 'classify_decimal', 'compare_sets'])

        if problem_type == 'classify_fraction':
            num = random.randint(1, 9)
            denom = random.randint(2, 9)
            if random.choice([True, False]):
                num = -num

            latex = f"\\text{{Classify: }} \\frac{{{num}}}{{{denom}}}"
            solution = "Rational, Real"
            steps = [
                f"\\frac{{{num}}}{{{denom}}} \\text{{ can be written as a fraction}}",
                f"\\text{{Therefore it is Rational and Real}}"
            ]

        elif problem_type == 'classify_decimal':
            decimals = [
                (0.5, "Rational, Real", "0.5 = 1/2"),
                (0.333, "Rational, Real", "0.333... = 1/3"),
                (0.25, "Rational, Real", "0.25 = 1/4"),
                (-1.5, "Rational, Real", "-1.5 = -3/2"),
                (0.75, "Rational, Real", "0.75 = 3/4"),
            ]
            decimal, answer, explanation = random.choice(decimals)

            latex = f"\\text{{Classify: }} {decimal}"
            solution = answer
            steps = [f"\\text{{{explanation}}}", f"\\text{{Therefore: {answer}}}"]

        else:  # compare_sets
            comparisons = [
                ("natural numbers", "whole numbers", "Natural \\subset Whole"),
                ("whole numbers", "integers", "Whole \\subset Integer"),
                ("integers", "rational numbers", "Integer \\subset Rational"),
                ("rational numbers", "real numbers", "Rational \\subset Real"),
            ]
            set1, set2, relationship = random.choice(comparisons)

            latex = f"\\text{{What is the relationship between {set1} and {set2}?}}"
            solution = f"{set1.capitalize()} is a subset of {set2}"
            steps = [f"\\text{{Every {set1[:-1]} is also a {set2[:-1]}}}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard: Irrational numbers and edge cases."""
        problem_type = random.choice(['irrational', 'sqrt_classify', 'multiple_sets'])

        if problem_type == 'irrational':
            irrationals = [
                ("\\pi", "Irrational, Real", "Pi cannot be expressed as a fraction"),
                ("\\sqrt{2}", "Irrational, Real", "Square root of 2 is non-terminating, non-repeating"),
                ("\\sqrt{3}", "Irrational, Real", "Square root of 3 is non-terminating, non-repeating"),
                ("e", "Irrational, Real", "Euler's number is irrational"),
            ]
            num, answer, explanation = random.choice(irrationals)

            latex = f"\\text{{Classify: }} {num}"
            solution = answer
            steps = [f"\\text{{{explanation}}}"]

        elif problem_type == 'sqrt_classify':
            # Some square roots are rational, some are not
            options = [
                (4, "2", "Natural, Whole, Integer, Rational, Real"),
                (9, "3", "Natural, Whole, Integer, Rational, Real"),
                (2, "\\sqrt{2}", "Irrational, Real"),
                (5, "\\sqrt{5}", "Irrational, Real"),
                (16, "4", "Natural, Whole, Integer, Rational, Real"),
            ]
            n, simplified, classification = random.choice(options)

            latex = f"\\text{{Classify }} \\sqrt{{{n}}}"
            solution = classification
            steps = [
                f"\\sqrt{{{n}}} = {simplified}",
                f"\\text{{Classification: {classification}}}"
            ]

        else:  # multiple_sets
            # List all sets a number belongs to
            num = random.randint(1, 10)

            latex = f"\\text{{List ALL number sets that }} {num} \\text{{ belongs to.}}"
            solution = "Natural, Whole, Integer, Rational, Real"
            steps = [
                f"\\text{{{num} is a counting number (Natural)}}",
                f"\\text{{{num} is a whole number (Whole)}}",
                f"\\text{{{num} is an integer (Integer)}}",
                f"\\text{{{num} = {num}/1 (Rational)}}",
                f"\\text{{{num} is on the number line (Real)}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex classification and reasoning."""
        problem_type = random.choice(['venn_diagram', 'counterexample', 'always_sometimes'])

        if problem_type == 'venn_diagram':
            # Describe the relationship between sets
            latex = "\\text{Which set contains all other number sets: Natural, Whole, Integer, Rational, or Real?}"
            solution = "Real"
            steps = [
                "\\text{Natural} \\subset \\text{Whole} \\subset \\text{Integer} \\subset \\text{Rational} \\subset \\text{Real}",
                "\\text{Also: Irrational} \\subset \\text{Real}",
                "\\text{Real numbers contain all other sets}"
            ]

        elif problem_type == 'counterexample':
            statements = [
                ("All square roots are irrational", "False", "\\sqrt{4} = 2 \\text{ is rational}"),
                ("All fractions are less than 1", "False", "\\frac{5}{2} = 2.5 > 1"),
                ("The sum of two irrational numbers is always irrational", "False",
                 "\\sqrt{2} + (-\\sqrt{2}) = 0 \\text{ is rational}"),
            ]
            statement, answer, counterexample = random.choice(statements)

            latex = f"\\text{{True or False: {statement}. If false, give counterexample.}}"
            solution = f"{answer}. {counterexample}" if answer == "False" else answer
            steps = [f"{counterexample}"]

        else:  # always_sometimes
            statements = [
                ("A rational number is always a real number", "Always", "All rationals are real"),
                ("An integer is sometimes negative", "Sometimes", "Integers include positive, negative, and zero"),
                ("A real number is always rational", "Sometimes", "Irrational numbers are real but not rational"),
                ("A natural number is always positive", "Always", "Natural numbers start at 1"),
            ]
            statement, answer, explanation = random.choice(statements)

            latex = f"\\text{{Always, Sometimes, or Never: {statement}}}"
            solution = answer
            steps = [f"\\text{{{explanation}}}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = TheNumberSystemGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
