"""
Constructing Geometric Sequences Generator
Creates problems about building and writing geometric sequences
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class ConstructingGeometricSequencesGenerator:
    """Generates problems about constructing geometric sequences."""

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
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy: Write first n terms given a1 and r"""
        a1 = random.choice([2, 3, 4, 5])
        r = random.choice([2, 3, 0.5])
        n = random.randint(4, 5)

        latex = f"\\text{{Write the first }} {n} \\text{{ terms of geometric sequence with }} a_1 = {a1}, r = {r}"

        # Generate terms
        terms = []
        for i in range(n):
            term = a1 * (r ** i)
            if term == int(term):
                terms.append(str(int(term)))
            else:
                terms.append(str(term))

        solution_str = ", ".join(terms)
        
        steps = [
            f"a_1 = {a1}",
            f"a_2 = {a1} \\times {r} = {terms[1]}",
            f"a_3 = {terms[1]} \\times {r} = {terms[2]}",
            f"\\text{{Continue pattern...}}",
            f"\\text{{Sequence: }} {solution_str}"
        ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Find a1 and r, then write sequence"""
        problem_type = random.choice(['two_terms', 'explicit_formula', 'word_problem'])

        if problem_type == 'two_terms':
            # Given two terms, find a1 and r
            a1 = random.choice([2, 3, 4])
            r = random.choice([2, 3])
            
            # Give 1st and 3rd term
            term1 = a1
            term3 = a1 * (r ** 2)

            latex = f"\\text{{A geometric sequence has }} a_1 = {term1} \\text{{ and }} a_3 = {term3}. "
            latex += f"\\text{{Find }} r \\text{{ and write first 5 terms.}}"

            # Generate terms
            terms = [a1 * (r ** i) for i in range(5)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"a_3 = a_1 \\times r^2",
                f"{term3} = {term1} \\times r^2",
                f"r^2 = {term3 // term1}",
                f"r = {r}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        elif problem_type == 'explicit_formula':
            # Given explicit formula, write terms
            a1 = random.choice([2, 3, 5])
            r = random.choice([2, 3, -2])
            
            latex = f"\\text{{Write first 5 terms of }} a_n = {a1} \\cdot {r}^{{n-1}}"

            terms = [a1 * (r ** i) for i in range(5)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"a_1 = {a1} \\cdot {r}^0 = {terms[0]}",
                f"a_2 = {a1} \\cdot {r}^1 = {terms[1]}",
                f"a_3 = {a1} \\cdot {r}^2 = {terms[2]}",
                f"\\text{{Continue...}}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        else:  # word_problem
            # Growth/decay scenario
            initial = random.choice([100, 200, 500, 1000])
            r = random.choice([2, 0.5, 0.75])
            periods = 4

            if r > 1:
                context = "doubles"
                r_val = 2
            elif r == 0.5:
                context = "halves"
                r_val = 0.5
            else:
                context = "becomes 75%"
                r_val = 0.75

            latex = f"\\text{{A population starts at }} {initial} \\text{{ and }} {context} \\text{{ each period. "
            latex += f"\\text{{Write population for first }} {periods} \\text{{ periods.}}"

            terms = [initial * (r_val ** i) for i in range(periods)]
            solution_str = ", ".join([str(int(t)) if t == int(t) else str(t) for t in terms])

            steps = [
                f"\\text{{Initial: }} {initial}",
                f"\\text{{Ratio: }} {r_val}",
                f"\\text{{Values: }} {solution_str}"
            ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Complex construction with negative ratios or fractions"""
        problem_type = random.choice(['negative_ratio', 'fraction_ratio', 'reverse_engineer'])

        if problem_type == 'negative_ratio':
            # Alternating sequence
            a1 = random.choice([3, 4, 5])
            r = random.choice([-2, -3])
            n = 6

            latex = f"\\text{{Write first }} {n} \\text{{ terms: }} a_1 = {a1}, r = {r}"

            terms = [a1 * (r ** i) for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"\\text{{Negative ratio creates alternating signs}}",
                f"a_1 = {terms[0]}",
                f"a_2 = {terms[0]} \\times ({r}) = {terms[1]}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        elif problem_type == 'fraction_ratio':
            # Fractional ratio
            a1 = random.choice([16, 32, 64])
            r = random.choice([0.5, 0.25])
            n = 5

            latex = f"\\text{{Write first }} {n} \\text{{ terms: }} a_1 = {a1}, r = {r}"

            terms = [a1 * (r ** i) for i in range(n)]
            solution_str = ", ".join([str(int(t)) if t == int(t) else str(t) for t in terms])

            steps = [
                f"\\text{{Ratio }} < 1 \\text{{ creates decreasing sequence}}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        else:  # reverse_engineer
            # Given nth term, find sequence
            a1 = random.choice([2, 3])
            r = random.choice([2, 3])
            n = random.randint(4, 5)
            an = a1 * (r ** (n - 1))

            latex = f"\\text{{A geometric sequence has }} a_1 = {a1} \\text{{ and }} a_{n} = {an}. "
            latex += f"\\text{{Find }} r \\text{{ and write all terms.}}"

            # Calculate r
            # a_n = a1 * r^(n-1)
            # r^(n-1) = a_n / a1
            r_power = an // a1
            # For now, assume we can find r easily
            
            terms = [a1 * (r ** i) for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"a_{n} = a_1 \\times r^{{{n-1}}}",
                f"{an} = {a1} \\times r^{{{n-1}}}",
                f"r^{{{n-1}}} = {r_power}",
                f"r = {r}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex scenarios with multiple constraints"""
        problem_type = random.choice(['sum_constraint', 'product_constraint', 'mixed_sequence'])

        if problem_type == 'sum_constraint':
            # Given sum of first few terms
            a1 = random.choice([2, 3, 4])
            r = 2
            n = 4
            
            # Sum formula: S_n = a1(r^n - 1)/(r - 1)
            sum_n = a1 * ((r ** n) - 1) // (r - 1)

            latex = f"\\text{{Sum of first }} {n} \\text{{ terms is }} {sum_n}, a_1 = {a1}, r = {r}. "
            latex += f"\\text{{Write the sequence.}}"

            terms = [a1 * (r ** i) for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"\\text{{Verify: }} S_{n} = \\frac{{a_1(r^{n} - 1)}}{{r - 1}} = {sum_n}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        elif problem_type == 'product_constraint':
            # Given product of certain terms
            a1 = random.choice([2, 3])
            r = random.choice([2, 3])
            n = 5

            latex = f"\\text{{Construct geometric sequence with }} a_1 = {a1}, r = {r}, {n} \\text{{ terms}}"

            terms = [a1 * (r ** i) for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            product_first_3 = terms[0] * terms[1] * terms[2]
            
            steps = [
                f"\\text{{Generate terms using }} a_n = a_1 \\times r^{{n-1}}",
                f"\\text{{Sequence: }} {solution_str}",
                f"\\text{{Product of first 3: }} {product_first_3}"
            ]

        else:  # mixed_sequence
            # Geometric sequence embedded in larger pattern
            a1 = random.choice([1, 2])
            r = 3
            n = 5

            latex = f"\\text{{Write geometric sequence: }} a_1 = {a1}, r = {r}, \\text{{ first }} {n} \\text{{ terms}}"
            latex += f"\\text{{ Then find }} a_{{10}}"

            terms = [a1 * (r ** i) for i in range(n)]
            solution_str = ", ".join(map(str, terms))
            a10 = a1 * (r ** 9)

            steps = [
                f"\\text{{First }} {n} \\text{{ terms: }} {solution_str}",
                f"a_{{10}} = {a1} \\times {r}^9 = {a10}"
            ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='challenge'
        )

