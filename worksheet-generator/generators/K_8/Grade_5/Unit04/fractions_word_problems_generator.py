"""
Fractions Word Problems Generator - Grade 5 Unit 4
Generates word problems for adding and subtracting fractions with unlike denominators
Example: Sarah ran 1/2 mile and then ran 1/3 mile more. How far did she run?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class FractionsWordProblemsGenerator:
    """Generates fractions word problems."""

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

    def _gcd(self, a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    def _lcm(self, a, b):
        """Calculate least common multiple."""
        return abs(a * b) // self._gcd(a, b)

    def _simplify(self, num, den):
        """Simplify a fraction."""
        gcd = self._gcd(abs(num), abs(den))
        return num // gcd, den // gcd

    def _generate_easy(self) -> Equation:
        """Generate easy problems: simple addition word problems."""
        contexts = [
            ("pizza", "ate"),
            ("pie", "ate"),
            ("cake", "ate"),
            ("mile", "ran"),
            ("hour", "studied"),
            ("gallon", "used")
        ]

        unit, verb = random.choice(contexts)
        name = random.choice(["Sarah", "John", "Maria", "Alex", "Emma", "David"])

        den1 = random.choice([2, 4])
        den2 = den1 * 2 if den1 == 2 else den1

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = den2
        new_num1 = num1 * (lcm // den1)
        result_num = new_num1 + num2
        result_num, result_den = self._simplify(result_num, lcm)

        latex = f"\\text{{{{{name} {verb} }}}} \\frac{{{num1}}}{{{den1}}} \\text{{{{ {unit} and then }}}} \\frac{{{num2}}}{{{den2}}} \\text{{{{ {unit} more. How much in total?}}}}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}} \\text{{{{ {unit}}}}}"
        steps = [
            f"\\frac{{{num1}}}{{{den1}}} + \\frac{{{num2}}}{{{den2}}}",
            f"\\frac{{{new_num1}}}{{{lcm}}} + \\frac{{{num2}}}{{{lcm}}} = \\frac{{{new_num1 + num2}}}{{{lcm}}}",
            f"\\frac{{{result_num}}}{{{result_den}}} \\text{{{{ {unit}}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: subtraction word problems."""
        contexts = [
            ("cup", "had", "used"),
            ("yard", "had", "cut"),
            ("pound", "bought", "used"),
            ("liter", "had", "drank")
        ]

        unit, verb1, verb2 = random.choice(contexts)
        name = random.choice(["Sarah", "John", "Maria", "Alex", "Emma", "David"])

        pairs = [(3, 2), (4, 3), (5, 2), (6, 4)]
        den1, den2 = random.choice(pairs)

        num1 = random.randint(2, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        # Make sure subtraction is positive
        if new_num1 < new_num2:
            num1, num2 = num2, num1
            den1, den2 = den2, den1
            new_num1, new_num2 = new_num2, new_num1

        result_num = new_num1 - new_num2
        result_num, result_den = self._simplify(result_num, lcm)

        latex = f"\\text{{{{{name} {verb1} }}}} \\frac{{{num1}}}{{{den1}}} \\text{{{{ {unit} of flour and {verb2} }}}} \\frac{{{num2}}}{{{den2}}} \\text{{{{ {unit}. How much is left?}}}}"
        solution = f"\\frac{{{result_num}}}{{{result_den}}} \\text{{{{ {unit}}}}}"
        steps = [
            f"\\frac{{{num1}}}{{{den1}}} - \\frac{{{num2}}}{{{den2}}}",
            f"\\frac{{{new_num1}}}{{{lcm}}} - \\frac{{{new_num2}}}{{{lcm}}} = \\frac{{{result_num}}}{{{result_den}}}",
            f"\\frac{{{result_num}}}{{{result_den}}} \\text{{{{ {unit}}}}}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: mixed numbers in word problems."""
        name1 = random.choice(["Sarah", "John", "Maria"])
        name2 = random.choice(["Alex", "Emma", "David"])
        unit = random.choice(["mile", "hour", "pound"])

        whole1 = random.randint(1, 3)
        whole2 = random.randint(1, 3)

        den1 = random.choice([2, 3, 4])
        den2 = random.choice([2, 3, 4])
        while den2 == den1:
            den2 = random.choice([2, 3, 4])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)

        lcm = self._lcm(den1, den2)
        new_num1 = num1 * (lcm // den1)
        new_num2 = num2 * (lcm // den2)

        result_frac = new_num1 + new_num2
        extra_whole = result_frac // lcm
        result_frac = result_frac % lcm
        result_whole = whole1 + whole2 + extra_whole

        result_num, result_den = self._simplify(result_frac, lcm)

        if result_frac == 0:
            solution = f"{result_whole} \\text{{{{ {unit}s}}}}"
        else:
            solution = f"{result_whole}\\frac{{{result_num}}}{{{result_den}}} \\text{{{{ {unit}s}}}}"

        latex = f"\\text{{{{{name1} ran }}}} {whole1}\\frac{{{num1}}}{{{den1}}} \\text{{{{ {unit}s and {name2} ran }}}} {whole2}\\frac{{{num2}}}{{{den2}}} \\text{{{{ {unit}s. How far did they run together?}}}}"
        steps = [
            f"{whole1}\\frac{{{num1}}}{{{den1}}} + {whole2}\\frac{{{num2}}}{{{den2}}}",
            solution
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step word problems."""
        name = random.choice(["Sarah", "John", "Maria", "Alex"])
        unit = random.choice(["pound", "gallon", "meter"])

        whole1 = random.randint(3, 6)
        whole2 = random.randint(1, 3)
        whole3 = random.randint(1, 2)

        den1 = random.choice([2, 4])
        den2 = random.choice([3, 6])
        den3 = random.choice([2, 3])

        num1 = random.randint(1, den1 - 1)
        num2 = random.randint(1, den2 - 1)
        num3 = random.randint(1, den3 - 1)

        lcm_12 = self._lcm(den1, den2)
        lcm_all = self._lcm(lcm_12, den3)

        new_num1 = num1 * (lcm_all // den1)
        new_num2 = num2 * (lcm_all // den2)
        new_num3 = num3 * (lcm_all // den3)

        # Convert to improper fractions
        improper1 = whole1 * lcm_all + new_num1
        improper2 = whole2 * lcm_all + new_num2
        improper3 = whole3 * lcm_all + new_num3

        result = improper1 - improper2 - improper3
        result_whole = result // lcm_all
        result_frac = result % lcm_all

        result_num, result_den = self._simplify(result_frac, lcm_all)

        if result_frac == 0:
            solution = f"{result_whole} \\text{{{{ {unit}s}}}}"
        else:
            solution = f"{result_whole}\\frac{{{result_num}}}{{{result_den}}} \\text{{{{ {unit}s}}}}"

        latex = f"\\text{{{{{name} had }}}} {whole1}\\frac{{{num1}}}{{{den1}}} \\text{{{{ {unit}s. Used }}}} {whole2}\\frac{{{num2}}}{{{den2}}} \\text{{{{ {unit}s for project A and }}}} {whole3}\\frac{{{num3}}}{{{den3}}} \\text{{{{ {unit}s for project B. How much is left?}}}}"
        steps = [
            f"{whole1}\\frac{{{num1}}}{{{den1}}} - {whole2}\\frac{{{num2}}}{{{den2}}} - {whole3}\\frac{{{num3}}}{{{den3}}}",
            solution
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = FractionsWordProblemsGenerator()

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
