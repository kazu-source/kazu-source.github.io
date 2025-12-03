"""
Geometric Sequences Generator
Creates problems about understanding and working with geometric sequences
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class GeometricSequencesGenerator:
    """Generates problems about geometric sequences."""

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
        """Generate easy: Identify geometric sequences, find common ratio"""
        problem_type = random.choice(['identify', 'find_r', 'next_term'])

        if problem_type == 'identify':
            # Is this geometric?
            is_geometric = random.choice([True, False])
            if is_geometric:
                a1 = random.randint(2, 5)
                r = random.choice([2, 3])
                terms = [a1 * (r ** i) for i in range(5)]
            else:
                # Arithmetic sequence
                a1 = random.randint(2, 10)
                d = random.randint(2, 5)
                terms = [a1 + d * i for i in range(5)]

            sequence_str = ", ".join(map(str, terms))
            latex = f"\\text{{Is this a geometric sequence? }} {sequence_str}"
            solution = "Yes" if is_geometric else "No"

            if is_geometric:
                steps = [f"\\text{{Common ratio: }} r = \\frac{{{terms[1]}}}{{{terms[0]}}} = {r}", "\\text{{Yes, geometric}}"]
            else:
                steps = [f"\\text{{Ratios are not constant}}", "\\text{{No, not geometric}}"]

        elif problem_type == 'find_r':
            # Find common ratio
            a1 = random.randint(2, 5)
            r = random.choice([2, 3, 4])
            terms = [a1 * (r ** i) for i in range(4)]
            sequence_str = ", ".join(map(str, terms))

            latex = f"\\text{{Find the common ratio: }} {sequence_str}"
            solution = str(r)

            steps = [
                f"r = \\frac{{a_2}}{{a_1}} = \\frac{{{terms[1]}}}{{{terms[0]}}} = {r}",
                f"\\text{{Verify: }} \\frac{{{terms[2]}}}{{{terms[1]}}} = {r}"
            ]

        else:  # next_term
            a1 = random.randint(2, 4)
            r = random.choice([2, 3])
            terms = [a1 * (r ** i) for i in range(4)]
            next_term = a1 * (r ** 4)
            sequence_str = ", ".join(map(str, terms))

            latex = f"\\text{{Find the next term: }} {sequence_str}, ..."
            solution = str(next_term)

            steps = [
                f"r = \\frac{{{terms[1]}}}{{{terms[0]}}} = {r}",
                f"\\text{{Next term: }} {terms[3]} \\times {r} = {next_term}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Find nth term, use formula a_n = a_1 * r^(n-1)"""
        problem_type = random.choice(['find_nth', 'find_formula', 'word_problem'])

        if problem_type == 'find_nth':
            a1 = random.randint(2, 5)
            r = random.choice([2, 3])
            n = random.randint(5, 7)

            latex = f"\\text{{Find }} a_{{{n}}} \\text{{ if }} a_1 = {a1} \\text{{ and }} r = {r}"

            an = a1 * (r ** (n - 1))
            solution = str(an)

            steps = [
                f"a_n = a_1 \\times r^{{n-1}}",
                f"a_{{{n}}} = {a1} \\times {r}^{{{n}-1}}",
                f"a_{{{n}}} = {a1} \\times {r ** (n-1)}",
                f"a_{{{n}}} = {an}"
            ]

        elif problem_type == 'find_formula':
            a1 = random.randint(2, 4)
            r = random.choice([2, 3])
            terms = [a1 * (r ** i) for i in range(4)]
            sequence_str = ", ".join(map(str, terms))

            latex = f"\\text{{Write the explicit formula for: }} {sequence_str}, ..."
            solution = f"a_n = {a1} \\times {r}^{{n-1}}"

            steps = [
                f"a_1 = {a1}",
                f"r = \\frac{{{terms[1]}}}{{{terms[0]}}} = {r}",
                f"a_n = a_1 \\times r^{{n-1}}",
                f"a_n = {a1} \\times {r}^{{n-1}}"
            ]

        else:  # word_problem
            initial = random.choice([100, 200, 500])
            r = random.choice([2, 3])
            n = random.randint(4, 6)

            contexts = [
                (f"Bacteria start at {initial} and triple each hour", 3),
                (f"An investment of ${initial} doubles each year", 2),
            ]

            context, r_val = random.choice(contexts)
            r = r_val

            latex = f"\\text{{{context}. How many after }} {n} \\text{{ periods?}}"

            an = initial * (r ** (n - 1))
            solution = str(an)

            steps = [
                f"a_1 = {initial}, r = {r}",
                f"a_{{{n}}} = {initial} \\times {r}^{{{n}-1}}",
                f"a_{{{n}}} = {an}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Find a1 or r given other info, negative/fractional ratios"""
        problem_type = random.choice(['find_a1', 'find_position', 'fractional_r'])

        if problem_type == 'find_a1':
            # Given a_n and r, find a_1
            r = random.choice([2, 3])
            a1 = random.randint(2, 5)
            n = random.randint(4, 6)
            an = a1 * (r ** (n - 1))

            latex = f"\\text{{If }} a_{{{n}}} = {an} \\text{{ and }} r = {r}, \\text{{ find }} a_1"
            solution = str(a1)

            steps = [
                f"a_n = a_1 \\times r^{{n-1}}",
                f"{an} = a_1 \\times {r}^{{{n}-1}}",
                f"a_1 = \\frac{{{an}}}{{{r ** (n-1)}}}",
                f"a_1 = {a1}"
            ]

        elif problem_type == 'find_position':
            # Which term equals a certain value?
            a1 = random.choice([2, 3])
            r = random.choice([2, 3])
            n = random.randint(5, 7)
            an = a1 * (r ** (n - 1))

            latex = f"\\text{{In the sequence }} a_1 = {a1}, r = {r}, \\text{{ which term equals }} {an}?"
            solution = str(n)

            steps = [
                f"a_n = a_1 \\times r^{{n-1}}",
                f"{an} = {a1} \\times {r}^{{n-1}}",
                f"{r}^{{n-1}} = {an // a1}",
                f"n - 1 = {n - 1}",
                f"n = {n}"
            ]

        else:  # fractional_r
            # Decreasing sequence with r < 1
            a1 = random.choice([64, 128, 256])
            r = 0.5
            n = 5

            terms = [a1 * (r ** i) for i in range(n)]
            terms_str = ", ".join([str(int(t)) for t in terms])

            latex = f"\\text{{Identify the common ratio: }} {terms_str}"
            solution = "0.5 or 1/2"

            steps = [
                f"r = \\frac{{a_2}}{{a_1}} = \\frac{{{int(terms[1])}}}{{{int(terms[0])}}} = 0.5",
                f"\\text{{This is a decreasing geometric sequence}}",
                f"r = \\frac{{1}}{{2}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Sum formulas, negative ratios, complex applications"""
        problem_type = random.choice(['sum_finite', 'negative_ratio', 'geometric_mean'])

        if problem_type == 'sum_finite':
            a1 = random.choice([2, 3])
            r = 2
            n = random.randint(5, 7)

            # Sum formula: S_n = a1(r^n - 1)/(r - 1)
            sum_n = a1 * ((r ** n) - 1) // (r - 1)

            latex = f"\\text{{Find sum of first }} {n} \\text{{ terms: }} a_1 = {a1}, r = {r}"
            solution = str(sum_n)

            steps = [
                f"S_n = \\frac{{a_1(r^n - 1)}}{{r - 1}}",
                f"S_{{{n}}} = \\frac{{{a1}({r}^{{{n}}} - 1)}}{{{r} - 1}}",
                f"S_{{{n}}} = \\frac{{{a1}({r ** n} - 1)}}{{{r - 1}}}",
                f"S_{{{n}}} = {sum_n}"
            ]

        elif problem_type == 'negative_ratio':
            # Alternating sequence
            a1 = random.choice([3, 4, 5])
            r = -2
            n = 6

            terms = [a1 * (r ** i) for i in range(n)]
            terms_str = ", ".join(map(str, terms))

            latex = f"\\text{{Write first }} {n} \\text{{ terms: }} a_1 = {a1}, r = {r}"
            solution = terms_str

            steps = [
                f"\\text{{Negative ratio creates alternating signs}}",
                f"a_1 = {terms[0]}",
                f"a_2 = {terms[0]} \\times ({r}) = {terms[1]}",
                f"a_3 = {terms[1]} \\times ({r}) = {terms[2]}",
                f"\\text{{Sequence: }} {terms_str}"
            ]

        else:  # geometric_mean
            # Find geometric mean
            a = random.choice([4, 9, 16, 25])
            b = random.choice([16, 36, 64, 100])

            # Ensure clean geometric mean
            import math
            gm = int(math.sqrt(a * b))
            b = (gm * gm) // a  # Adjust b for clean answer

            latex = f"\\text{{Find the geometric mean of }} {a} \\text{{ and }} {b}"
            solution = str(gm)

            steps = [
                f"\\text{{Geometric mean}} = \\sqrt{{a \\times b}}",
                f"= \\sqrt{{{a} \\times {b}}}",
                f"= \\sqrt{{{a * b}}}",
                f"= {gm}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = GeometricSequencesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
