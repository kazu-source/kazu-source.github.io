"""
Equivalent Fractions Generator - Grade 3 Unit 6
Generates problems for identifying and creating equivalent fractions
Example: 1/2 = 2/4, finding equivalent fractions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EquivalentFractionsGenerator:
    """Generates equivalent fractions problems."""

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
        """Generate easy problems: simple equivalent fractions with halves, thirds, fourths."""
        # Start with simple fractions
        base_pairs = [
            (1, 2, 2, 4),  # 1/2 = 2/4
            (1, 2, 3, 6),  # 1/2 = 3/6
            (1, 3, 2, 6),  # 1/3 = 2/6
            (1, 4, 2, 8),  # 1/4 = 2/8
            (2, 4, 1, 2),  # 2/4 = 1/2
        ]

        num1, den1, num2, den2 = random.choice(base_pairs)

        problem_type = random.choice(['find_equivalent', 'are_equivalent'])

        if problem_type == 'find_equivalent':
            latex = f"\\frac{{{num1}}}{{{den1}}} = \\frac{{?}}{{{den2}}}"
            solution = str(num2)
            steps = [f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{num2}}}{{{den2}}}"]
        else:
            latex = f"\\text{{Are these equivalent? }} \\frac{{{num1}}}{{{den1}}} \\text{{ and }} \\frac{{{num2}}}{{{den2}}}"
            solution = "Yes"
            steps = [f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{num2}}}{{{den2}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: more complex equivalent fractions."""
        # Generate equivalent fractions with multiplier
        base_fractions = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5)]
        num1, den1 = random.choice(base_fractions)

        multiplier = random.choice([2, 3, 4])
        num2 = num1 * multiplier
        den2 = den1 * multiplier

        problem_type = random.choice(['find_numerator', 'find_denominator', 'verify'])

        if problem_type == 'find_numerator':
            latex = f"\\frac{{{num1}}}{{{den1}}} = \\frac{{?}}{{{den2}}}"
            solution = str(num2)
            steps = [f"\\text{{Multiply by {multiplier}: }} {num1} \\times {multiplier} = {num2}"]
        elif problem_type == 'find_denominator':
            latex = f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{num2}}}{{?}}"
            solution = str(den2)
            steps = [f"\\text{{Multiply by {multiplier}: }} {den1} \\times {multiplier} = {den2}"]
        else:
            latex = f"\\text{{Are }} \\frac{{{num1}}}{{{den1}}} \\text{{ and }} \\frac{{{num2}}}{{{den2}}} \\text{{ equivalent?}}"
            solution = "Yes"
            steps = [f"\\text{{Both equal when multiplied by {multiplier}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with equivalent fractions."""
        base_fractions = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5)]
        num1, den1 = random.choice(base_fractions)

        multiplier = random.choice([2, 3, 4])
        num2 = num1 * multiplier
        den2 = den1 * multiplier

        contexts = [
            f"A recipe calls for \\frac{{{num1}}}{{{den1}}} cup of sugar. If you double all ingredients by {multiplier}, what equivalent fraction represents the sugar needed?",
            f"Sarah completed \\frac{{{num1}}}{{{den1}}} of her homework. If the homework had {den2} problems instead of {den1}, how many would she complete to do the same fraction?",
            f"A pizza is cut into {den1} slices and you eat {num1}. Your friend's pizza is cut into {den2} slices. How many should your friend eat to match your fraction?",
            f"In a class, \\frac{{{num1}}}{{{den1}}} of students have pets. If this represents {num2} students with pets, how many students are in the class?"
        ]

        context = random.choice(contexts)

        if "how many students are in the class" in context:
            solution = str(den2)
            steps = [f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{num2}}}{{{den2}}} \\text{{, so {den2} students}}"]
        elif "how many would she complete" in context or "How many should your friend eat" in context:
            solution = str(num2)
            steps = [f"\\frac{{{num1}}}{{{den1}}} = \\frac{{{num2}}}{{{den2}}}"]
        else:
            solution = f"\\frac{{{num2}}}{{{den2}}}"
            steps = [f"\\frac{{{num1}}}{{{den1}}} \\times {multiplier} = \\frac{{{num2}}}{{{den2}}}"]

        latex = f"\\text{{{context}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: finding multiple equivalents or simplifying."""
        problem_type = random.choice(['find_multiple', 'simplify', 'identify_all'])

        if problem_type == 'find_multiple':
            base_fractions = [(1, 2), (1, 3), (1, 4), (2, 3)]
            num1, den1 = random.choice(base_fractions)

            latex = f"\\text{{Give two equivalent fractions for }} \\frac{{{num1}}}{{{den1}}}"

            equiv1_num = num1 * 2
            equiv1_den = den1 * 2
            equiv2_num = num1 * 3
            equiv2_den = den1 * 3

            solution = f"\\frac{{{equiv1_num}}}{{{equiv1_den}}} \\text{{ and }} \\frac{{{equiv2_num}}}{{{equiv2_den}}}"
            steps = [f"\\text{{Multiply by 2: }} \\frac{{{equiv1_num}}}{{{equiv1_den}}}, \\text{{ by 3: }} \\frac{{{equiv2_num}}}{{{equiv2_den}}}"]

        elif problem_type == 'simplify':
            # Create a fraction that can be simplified
            base_fractions = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4)]
            num_simple, den_simple = random.choice(base_fractions)

            multiplier = random.choice([2, 3, 4])
            num_complex = num_simple * multiplier
            den_complex = den_simple * multiplier

            latex = f"\\text{{Simplify: }} \\frac{{{num_complex}}}{{{den_complex}}}"
            solution = f"\\frac{{{num_simple}}}{{{den_simple}}}"
            steps = [f"\\text{{Divide by {multiplier}: }} \\frac{{{num_complex} \\div {multiplier}}}{{{den_complex} \\div {multiplier}}} = \\frac{{{num_simple}}}{{{den_simple}}}"]

        else:  # identify_all
            base_fractions = [(1, 2), (1, 3), (2, 4)]
            num1, den1 = random.choice(base_fractions)

            # Generate some equivalent and non-equivalent fractions
            equiv_num = num1 * 2
            equiv_den = den1 * 2

            # Create a non-equivalent
            non_equiv_num = num1 + 1 if num1 < den1 - 1 else num1
            non_equiv_den = den1

            latex = f"\\text{{Which is equivalent to }} \\frac{{{num1}}}{{{den1}}}\\text{{: }} \\frac{{{equiv_num}}}{{{equiv_den}}} \\text{{ or }} \\frac{{{non_equiv_num}}}{{{non_equiv_den}}}?"
            solution = f"\\frac{{{equiv_num}}}{{{equiv_den}}}"
            steps = [f"\\frac{{{num1}}}{{{den1}}} \\times 2 = \\frac{{{equiv_num}}}{{{equiv_den}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EquivalentFractionsGenerator()

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
