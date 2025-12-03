"""
Constructing Arithmetic Sequences Generator
Creates problems about building and writing arithmetic sequences
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class ConstructingArithmeticSequencesGenerator:
    """Generates problems about constructing arithmetic sequences."""

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
        """Generate easy: Write first n terms given a1 and d"""
        a1 = random.randint(2, 10)
        d = random.randint(2, 5)
        n = random.randint(5, 6)

        latex = f"\\text{{Write the first }} {n} \\text{{ terms: }} a_1 = {a1}, d = {d}"

        terms = [a1 + d * i for i in range(n)]
        solution_str = ", ".join(map(str, terms))

        steps = [
            f"a_1 = {a1}",
            f"a_2 = {a1} + {d} = {terms[1]}",
            f"a_3 = {terms[1]} + {d} = {terms[2]}",
            f"\\text{{Continue adding }} d = {d}",
            f"\\text{{Sequence: }} {solution_str}"
        ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Construct from various given information"""
        problem_type = random.choice(['from_two_terms', 'from_formula', 'word_problem'])

        if problem_type == 'from_two_terms':
            # Given first term and another term
            a1 = random.randint(3, 8)
            d = random.randint(2, 4)
            n = random.randint(5, 8)
            an = a1 + (n - 1) * d

            latex = f"\\text{{Construct sequence with }} a_1 = {a1} \\text{{ and }} a_{{{n}}} = {an}. "
            latex += f"\\text{{Write first }} {n} \\text{{ terms.}}"

            terms = [a1 + d * i for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"a_{{{n}}} = a_1 + (n-1)d",
                f"{an} = {a1} + ({n}-1)d",
                f"d = \\frac{{{an} - {a1}}}{{{n - 1}}} = {d}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        elif problem_type == 'from_formula':
            # Given explicit formula
            a1 = random.randint(2, 6)
            d = random.randint(2, 5)
            n = 6

            # a_n = a_1 + (n-1)d = a1 + nd - d = (a1 - d) + nd
            # So a_n = d*n + (a1 - d)
            constant = a1 - d

            if constant >= 0:
                latex = f"\\text{{Write first }} {n} \\text{{ terms of }} a_n = {d}n + {constant}"
            else:
                latex = f"\\text{{Write first }} {n} \\text{{ terms of }} a_n = {d}n - {abs(constant)}"

            terms = [d * (i + 1) + constant for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"a_1 = {d}(1) + ({constant}) = {terms[0]}",
                f"a_2 = {d}(2) + ({constant}) = {terms[1]}",
                f"\\text{{Continue for each n}}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        else:  # word_problem
            initial = random.choice([20, 30, 50])
            d = random.choice([5, 10, 15])
            n = 6

            contexts = [
                (f"A theater has {initial} seats in row 1, and each row has {d} more seats than the previous", "seats"),
                (f"A staircase starts with {initial} steps, adding {d} steps each level", "steps"),
                (f"Week 1 savings: ${initial}, increasing by ${d} each week", "dollars")
            ]

            context, unit = random.choice(contexts)
            latex = f"\\text{{{context}. Write the first }} {n} \\text{{ terms.}}"

            terms = [initial + d * i for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"a_1 = {initial}",
                f"d = {d}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Complex construction with constraints"""
        problem_type = random.choice(['negative_d', 'given_sum', 'multiple_constraints'])

        if problem_type == 'negative_d':
            # Decreasing sequence
            a1 = random.randint(50, 80)
            d = random.randint(-8, -3)
            n = 7

            latex = f"\\text{{Write first }} {n} \\text{{ terms: }} a_1 = {a1}, d = {d}"

            terms = [a1 + d * i for i in range(n)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"\\text{{Negative d means decreasing sequence}}",
                f"a_1 = {a1}",
                f"a_2 = {a1} + ({d}) = {terms[1]}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        elif problem_type == 'given_sum':
            # Given sum of certain terms
            a1 = random.randint(2, 5)
            d = random.randint(2, 4)
            n = 5

            terms = [a1 + d * i for i in range(n)]
            sum_n = sum(terms)

            latex = f"\\text{{Sum of first }} {n} \\text{{ terms is }} {sum_n}, a_1 = {a1}. "
            latex += f"\\text{{Find d and write the sequence.}}"

            solution_str = ", ".join(map(str, terms))

            steps = [
                f"S_{{{n}}} = \\frac{{n}}{{2}}(2a_1 + (n-1)d)",
                f"{sum_n} = \\frac{{{n}}}{{2}}(2({a1}) + ({n}-1)d)",
                f"\\text{{Solve for d: }} d = {d}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        else:  # multiple_constraints
            # Given two different terms
            a1 = random.randint(2, 6)
            d = random.randint(2, 4)
            n1, n2 = 2, 6
            term1 = a1 + (n1 - 1) * d
            term2 = a1 + (n2 - 1) * d

            latex = f"\\text{{If }} a_{{{n1}}} = {term1} \\text{{ and }} a_{{{n2}}} = {term2}, "
            latex += f"\\text{{construct the sequence (first 8 terms).}}"

            terms = [a1 + d * i for i in range(8)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"d = \\frac{{a_{{{n2}}} - a_{{{n1}}}}}{{{n2} - {n1}}} = \\frac{{{term2} - {term1}}}{{{n2 - n1}}} = {d}",
                f"a_1 = a_{{{n1}}} - ({n1}-1)d = {term1} - {(n1-1)*d} = {a1}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Advanced construction problems"""
        problem_type = random.choice(['arithmetic_means', 'recursive_to_explicit', 'real_world'])

        if problem_type == 'arithmetic_means':
            # Insert multiple arithmetic means
            a = random.randint(5, 10)
            k = random.randint(3, 5)  # number of means
            d = random.randint(3, 6)
            b = a + (k + 1) * d

            latex = f"\\text{{Insert }} {k} \\text{{ arithmetic means between }} {a} \\text{{ and }} {b}, "
            latex += f"\\text{{then write the complete sequence.}}"

            terms = [a + d * i for i in range(k + 2)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"\\text{{Total terms: }} {k + 2}",
                f"\\text{{Total gaps: }} {k + 1}",
                f"d = \\frac{{{b} - {a}}}{{{k + 1}}} = {d}",
                f"\\text{{Complete sequence: }} {solution_str}"
            ]

        elif problem_type == 'recursive_to_explicit':
            # Convert recursive to explicit form and generate
            a1 = random.randint(3, 8)
            d = random.randint(2, 5)
            n = 6

            latex = f"\\text{{Given }} a_1 = {a1}, a_n = a_{{n-1}} + {d}, "
            latex += f"\\text{{write explicit formula and first }} {n} \\text{{ terms.}}"

            terms = [a1 + d * i for i in range(n)]
            solution_str = ", ".join(map(str, terms))
            formula = f"a_n = {a1} + (n-1) \\times {d}"

            steps = [
                f"\\text{{Recursive: }} a_n = a_{{n-1}} + {d}",
                f"\\text{{This means d = }} {d}",
                f"\\text{{Explicit: }} {formula}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        else:  # real_world
            # Complex real-world scenario
            start_year = 2020
            initial = random.choice([1000, 2000, 5000])
            d = random.choice([150, 200, 250, 500])
            years = 6

            latex = f"\\text{{In }} {start_year}, \\text{{ a company had }} {initial} \\text{{ employees. }}"
            latex += f"\\text{{They hire }} {d} \\text{{ more each year. }}"
            latex += f"\\text{{Construct the sequence for }} {start_year}-{start_year + years - 1}."

            terms = [initial + d * i for i in range(years)]
            solution_str = ", ".join(map(str, terms))

            steps = [
                f"a_1 = {initial} \\text{{ (year {start_year})}}",
                f"d = {d} \\text{{ (annual increase)}}",
                f"\\text{{Sequence: }} {solution_str}"
            ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ConstructingArithmeticSequencesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
