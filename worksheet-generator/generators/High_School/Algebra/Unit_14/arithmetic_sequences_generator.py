"""
Arithmetic Sequences Generator
Creates problems about understanding and working with arithmetic sequences
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class ArithmeticSequencesGenerator:
    """Generates problems about arithmetic sequences."""

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
        """Generate easy: Identify if sequence is arithmetic, find common difference"""
        problem_type = random.choice(['identify', 'find_d', 'next_term'])

        if problem_type == 'identify':
            # Is this arithmetic?
            is_arithmetic = random.choice([True, False])
            if is_arithmetic:
                a1 = random.randint(2, 10)
                d = random.randint(2, 5)
                terms = [a1 + d * i for i in range(5)]
            else:
                # Geometric or random
                a1 = random.randint(2, 5)
                r = random.choice([2, 3])
                terms = [a1 * (r ** i) for i in range(5)]

            sequence_str = ", ".join(map(str, terms))
            latex = f"\\text{{Is this an arithmetic sequence? }} {sequence_str}"
            solution = "Yes" if is_arithmetic else "No"

            if is_arithmetic:
                steps = [f"\\text{{Common difference: }} {d} \\text{{ (constant)}}", "\\text{{Yes, arithmetic}}"]
            else:
                steps = [f"\\text{{Differences are not constant}}", "\\text{{No, not arithmetic}}"]

        elif problem_type == 'find_d':
            # Find common difference
            a1 = random.randint(2, 10)
            d = random.randint(2, 6)
            terms = [a1 + d * i for i in range(4)]
            sequence_str = ", ".join(map(str, terms))

            latex = f"\\text{{Find the common difference: }} {sequence_str}"
            solution = str(d)

            steps = [
                f"d = a_2 - a_1 = {terms[1]} - {terms[0]} = {d}",
                f"\\text{{Verify: }} {terms[2]} - {terms[1]} = {d}"
            ]

        else:  # next_term
            a1 = random.randint(3, 10)
            d = random.randint(2, 5)
            terms = [a1 + d * i for i in range(4)]
            next_term = a1 + d * 4
            sequence_str = ", ".join(map(str, terms))

            latex = f"\\text{{Find the next term: }} {sequence_str}, ..."
            solution = str(next_term)

            steps = [
                f"d = {terms[1]} - {terms[0]} = {d}",
                f"\\text{{Next term: }} {terms[3]} + {d} = {next_term}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Find nth term, use formula a_n = a_1 + (n-1)d"""
        problem_type = random.choice(['find_nth', 'find_formula', 'word_problem'])

        if problem_type == 'find_nth':
            a1 = random.randint(2, 10)
            d = random.randint(2, 5)
            n = random.randint(8, 15)

            latex = f"\\text{{Find }} a_{{{n}}} \\text{{ if }} a_1 = {a1} \\text{{ and }} d = {d}"

            an = a1 + (n - 1) * d
            solution = str(an)

            steps = [
                f"a_n = a_1 + (n-1)d",
                f"a_{{{n}}} = {a1} + ({n}-1) \\times {d}",
                f"a_{{{n}}} = {a1} + {(n-1) * d}",
                f"a_{{{n}}} = {an}"
            ]

        elif problem_type == 'find_formula':
            a1 = random.randint(3, 8)
            d = random.randint(2, 4)
            terms = [a1 + d * i for i in range(4)]
            sequence_str = ", ".join(map(str, terms))

            latex = f"\\text{{Write the explicit formula for: }} {sequence_str}, ..."
            solution = f"a_n = {a1} + (n-1) \\times {d}"

            steps = [
                f"a_1 = {a1}",
                f"d = {terms[1]} - {terms[0]} = {d}",
                f"a_n = a_1 + (n-1)d",
                f"a_n = {a1} + (n-1) \\times {d}"
            ]

        else:  # word_problem
            initial = random.choice([50, 100, 200])
            d = random.choice([10, 15, 20, 25])
            n = random.randint(5, 10)

            latex = f"\\text{{A student saves }} ${initial} \\text{{ initially, then adds }} ${d} \\text{{ each week. }}"
            latex += f"\\text{{How much after }} {n} \\text{{ weeks?}}"

            an = initial + (n - 1) * d
            solution = f"${an}"

            steps = [
                f"a_1 = {initial}, d = {d}",
                f"a_{{{n}}} = {initial} + ({n}-1) \\times {d}",
                f"a_{{{n}}} = ${an}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Find a1 or d given other info, find term position"""
        problem_type = random.choice(['find_a1', 'find_position', 'two_terms'])

        if problem_type == 'find_a1':
            # Given a_n and d, find a_1
            d = random.randint(3, 6)
            a1 = random.randint(5, 15)
            n = random.randint(8, 12)
            an = a1 + (n - 1) * d

            latex = f"\\text{{If }} a_{{{n}}} = {an} \\text{{ and }} d = {d}, \\text{{ find }} a_1"
            solution = str(a1)

            steps = [
                f"a_n = a_1 + (n-1)d",
                f"{an} = a_1 + ({n}-1) \\times {d}",
                f"{an} = a_1 + {(n-1) * d}",
                f"a_1 = {an} - {(n-1) * d} = {a1}"
            ]

        elif problem_type == 'find_position':
            # Which term equals a certain value?
            a1 = random.randint(3, 8)
            d = random.randint(2, 5)
            n = random.randint(10, 20)
            an = a1 + (n - 1) * d

            latex = f"\\text{{In the sequence }} a_1 = {a1}, d = {d}, \\text{{ which term equals }} {an}?"
            solution = str(n)

            steps = [
                f"a_n = a_1 + (n-1)d",
                f"{an} = {a1} + (n-1) \\times {d}",
                f"{an - a1} = (n-1) \\times {d}",
                f"n - 1 = {(an - a1) // d}",
                f"n = {n}"
            ]

        else:  # two_terms
            # Given two terms, find d and a1
            a1 = random.randint(2, 8)
            d = random.randint(2, 5)
            n1, n2 = 3, 7
            term1 = a1 + (n1 - 1) * d
            term2 = a1 + (n2 - 1) * d

            latex = f"\\text{{If }} a_{{{n1}}} = {term1} \\text{{ and }} a_{{{n2}}} = {term2}, \\text{{ find }} a_1 \\text{{ and }} d"
            solution = f"a_1 = {a1}, d = {d}"

            steps = [
                f"d = \\frac{{a_{{{n2}}} - a_{{{n1}}}}}{{{n2} - {n1}}} = \\frac{{{term2} - {term1}}}{{{n2 - n1}}} = {d}",
                f"a_{{{n1}}} = a_1 + ({n1}-1)d",
                f"{term1} = a_1 + {(n1-1) * d}",
                f"a_1 = {a1}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Sum of arithmetic sequence, complex applications"""
        problem_type = random.choice(['sum', 'missing_terms', 'mean'])

        if problem_type == 'sum':
            a1 = random.randint(2, 5)
            d = random.randint(2, 4)
            n = random.randint(8, 12)
            an = a1 + (n - 1) * d

            # Sum formula: S_n = n/2 * (a1 + an)
            sum_n = n * (a1 + an) // 2

            latex = f"\\text{{Find the sum of first }} {n} \\text{{ terms: }} a_1 = {a1}, d = {d}"
            solution = str(sum_n)

            steps = [
                f"a_{{{n}}} = {a1} + ({n}-1) \\times {d} = {an}",
                f"S_{{{n}}} = \\frac{{n}}{{2}}(a_1 + a_n)",
                f"S_{{{n}}} = \\frac{{{n}}}{{2}}({a1} + {an})",
                f"S_{{{n}}} = {sum_n}"
            ]

        elif problem_type == 'missing_terms':
            # Insert arithmetic means
            a = random.randint(2, 5)
            b = random.randint(20, 30)
            n = 3  # number of means to insert

            # Total terms = n + 2
            d = (b - a) // (n + 1)
            b = a + (n + 1) * d  # Adjust b to ensure integer d

            means = [a + d * i for i in range(1, n + 1)]
            means_str = ", ".join(map(str, means))

            latex = f"\\text{{Insert }} {n} \\text{{ arithmetic means between }} {a} \\text{{ and }} {b}"
            solution = means_str

            steps = [
                f"\\text{{Total terms: }} {n + 2}",
                f"d = \\frac{{{b} - {a}}}{{{n + 1}}} = {d}",
                f"\\text{{Means: }} {means_str}"
            ]

        else:  # mean
            # Arithmetic mean of two terms
            a = random.randint(10, 30)
            b = random.randint(40, 60)
            mean = (a + b) // 2
            b = 2 * mean - a  # Adjust to ensure integer mean

            latex = f"\\text{{Find the arithmetic mean of }} {a} \\text{{ and }} {b}"
            solution = str(mean)

            steps = [
                f"\\text{{Arithmetic mean}} = \\frac{{a + b}}{{2}}",
                f"= \\frac{{{a} + {b}}}{{2}}",
                f"= {mean}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ArithmeticSequencesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
