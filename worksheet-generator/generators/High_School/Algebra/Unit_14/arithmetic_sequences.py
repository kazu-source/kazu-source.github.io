"""
Generator for Arithmetic Sequences problems.
"""

import random
from generators.base import Problem, BaseGenerator
from typing import List


class ArithmeticSequencesGenerator(BaseGenerator):
    """Generator for arithmetic sequences problems."""

    def __init__(self):
        """Initialize the generator."""
        super().__init__()

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Problem]:
        """
        Generate a worksheet of arithmetic sequences problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Problem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            if problem:
                problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> Problem:
        """
        Generate a single arithmetic sequences problem.

        Args:
            difficulty: Problem difficulty level

        Returns:
            Problem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        elif difficulty == 'challenge':
            return self._generate_challenge()
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def _generate_easy(self) -> Problem:
        """
        Generate an easy arithmetic sequences problem.
        Find the next term or identify common difference.
        """
        problem_type = random.choice(['next_term', 'common_difference', 'is_arithmetic'])

        if problem_type == 'next_term':
            # Generate a simple sequence
            a1 = random.randint(-10, 10)
            d = random.randint(-5, 5)
            while d == 0:
                d = random.randint(-5, 5)

            # Generate first few terms
            terms = []
            for i in range(4):
                terms.append(a1 + i * d)

            sequence_str = ", ".join(map(str, terms))
            next_term = a1 + 4 * d

            question = f"Find the next term in the sequence: {sequence_str}, ..."
            answer = str(next_term)

        elif problem_type == 'common_difference':
            # Generate a sequence and ask for common difference
            a1 = random.randint(-20, 20)
            d = random.randint(-8, 8)
            while d == 0:
                d = random.randint(-8, 8)

            terms = []
            for i in range(4):
                terms.append(a1 + i * d)

            sequence_str = ", ".join(map(str, terms))

            question = f"Find the common difference of: {sequence_str}, ..."
            answer = f"d = {d}"

        else:  # is_arithmetic
            # Generate either arithmetic or non-arithmetic sequence
            is_arith = random.choice([True, False])

            if is_arith:
                a1 = random.randint(-10, 10)
                d = random.randint(-5, 5)
                while d == 0:
                    d = random.randint(-5, 5)
                terms = [a1 + i * d for i in range(5)]
            else:
                # Generate a geometric or random sequence
                terms = [random.randint(-20, 20) for _ in range(5)]
                # Make sure it's not accidentally arithmetic
                while len(set([terms[i+1] - terms[i] for i in range(4)])) == 1:
                    terms = [random.randint(-20, 20) for _ in range(5)]

            sequence_str = ", ".join(map(str, terms))
            question = f"Is this an arithmetic sequence? {sequence_str}"
            answer = "Yes" if is_arith else "No"

        return Problem(
            problem_type="arithmetic_sequences",
            question=question,
            answer=answer,
            difficulty=1
        )

    def _generate_medium(self) -> Problem:
        """
        Generate a medium arithmetic sequences problem.
        Find specific terms or use the formula.
        """
        problem_type = random.choice(['nth_term', 'find_n', 'sum'])

        if problem_type == 'nth_term':
            # Find the nth term using formula a_n = a_1 + (n-1)d
            a1 = random.randint(-20, 20)
            d = random.randint(-10, 10)
            while d == 0:
                d = random.randint(-10, 10)
            n = random.randint(10, 30)

            # Give first few terms
            terms = [a1 + i * d for i in range(3)]
            sequence_str = ", ".join(map(str, terms))

            an = a1 + (n - 1) * d

            question = f"In the sequence {sequence_str}, ..., find the {n}th term"
            answer = f"a_{n} = {an}"

        elif problem_type == 'find_n':
            # Given a term, find its position
            a1 = random.randint(-10, 10)
            d = random.randint(1, 5)  # Positive for simplicity
            n = random.randint(10, 25)
            an = a1 + (n - 1) * d

            # Give first few terms
            terms = [a1 + i * d for i in range(3)]
            sequence_str = ", ".join(map(str, terms))

            question = f"In the sequence {sequence_str}, ..., which term equals {an}?"
            answer = f"n = {n}"

        else:  # sum
            # Find sum of first n terms
            a1 = random.randint(-10, 10)
            d = random.randint(-5, 5)
            while d == 0:
                d = random.randint(-5, 5)
            n = random.randint(5, 15)

            # Give the sequence
            terms = [a1 + i * d for i in range(3)]
            sequence_str = ", ".join(map(str, terms))

            # Calculate sum using S_n = n/2 * (2a_1 + (n-1)d)
            sum_n = n * (2 * a1 + (n - 1) * d) // 2

            question = f"Find the sum of the first {n} terms of: {sequence_str}, ..."
            answer = f"S_{n} = {sum_n}"

        return Problem(
            problem_type="arithmetic_sequences",
            question=question,
            answer=answer,
            difficulty=2
        )

    def _generate_hard(self) -> Problem:
        """
        Generate a hard arithmetic sequences problem.
        Write explicit formulas or solve for unknowns.
        """
        problem_type = random.choice(['write_formula', 'find_missing', 'word_problem'])

        if problem_type == 'write_formula':
            # Given two terms, write the explicit formula
            a1 = random.randint(-20, 20)
            d = random.randint(-10, 10)
            while d == 0:
                d = random.randint(-10, 10)

            # Pick two random positions
            n1 = random.randint(1, 5)
            n2 = random.randint(10, 20)
            term1 = a1 + (n1 - 1) * d
            term2 = a1 + (n2 - 1) * d

            question = f"An arithmetic sequence has a_{n1} = {term1} and a_{n2} = {term2}. Write the explicit formula."

            if d > 0:
                answer = f"a_n = {a1} + {d}(n - 1)" if a1 >= 0 else f"a_n = {a1} + {d}(n - 1)"
            else:
                answer = f"a_n = {a1} - {abs(d)}(n - 1)" if a1 >= 0 else f"a_n = {a1} - {abs(d)}(n - 1)"

        elif problem_type == 'find_missing':
            # Given partial sequence with missing terms
            a1 = random.randint(-20, 20)
            d = random.randint(-8, 8)
            while d == 0:
                d = random.randint(-8, 8)

            # Create sequence with a gap
            term1 = a1
            term2 = a1 + d
            term4 = a1 + 3 * d
            term5 = a1 + 4 * d
            missing = a1 + 2 * d

            question = f"Find the missing term: {term1}, {term2}, ___, {term4}, {term5}"
            answer = str(missing)

        else:  # word_problem
            # Real-world context
            initial = random.randint(1000, 5000)
            increase = random.randint(50, 200)
            months = random.randint(12, 24)

            question = f"A savings account starts with ${initial} and increases by ${increase} each month. "
            question += f"How much will be in the account after {months} months?"

            total = initial + increase * months

            answer = f"${total}"

        return Problem(
            problem_type="arithmetic_sequences",
            question=question,
            answer=answer,
            difficulty=3
        )

    def _generate_challenge(self) -> Problem:
        """
        Generate a challenge arithmetic sequences problem.
        Complex formulas, systems, or recursive definitions.
        """
        problem_type = random.choice(['system', 'recursive', 'complex_sum'])

        if problem_type == 'system':
            # System of equations with arithmetic sequences
            a1 = random.randint(-10, 10)
            d = random.randint(1, 8)

            # Create conditions
            n1 = random.randint(3, 7)
            n2 = random.randint(10, 15)
            term_n1 = a1 + (n1 - 1) * d
            term_n2 = a1 + (n2 - 1) * d
            sum_first_5 = 5 * (2 * a1 + 4 * d) // 2

            question = f"An arithmetic sequence has a_{n1} = {term_n1} and the sum of the first 5 terms is {sum_first_5}. "
            question += f"Find a_1 and d."

            answer = f"a_1 = {a1}, d = {d}"

        elif problem_type == 'recursive':
            # Convert between recursive and explicit
            a1 = random.randint(-15, 15)
            d = random.randint(-10, 10)
            while d == 0:
                d = random.randint(-10, 10)

            question = f"A sequence is defined recursively as a_1 = {a1}, a_n = a_{{n-1}} + {d} for n > 1. "
            question += "Write the explicit formula and find a_20."

            a20 = a1 + 19 * d

            if d > 0:
                answer = f"a_n = {a1} + {d}(n - 1), a_20 = {a20}"
            else:
                answer = f"a_n = {a1} - {abs(d)}(n - 1), a_20 = {a20}"

        else:  # complex_sum
            # Sum of arithmetic sequence with conditions
            a1 = random.randint(1, 10)
            d = random.randint(2, 6)

            # Find sum of terms from position m to n
            m = random.randint(5, 10)
            n = random.randint(m + 10, m + 20)

            # Sum from m to n = S_n - S_{m-1}
            sum_n = n * (2 * a1 + (n - 1) * d) // 2
            sum_m_minus_1 = (m - 1) * (2 * a1 + (m - 2) * d) // 2
            result = sum_n - sum_m_minus_1

            question = f"For the arithmetic sequence with a_1 = {a1} and d = {d}, "
            question += f"find the sum of terms from position {m} to {n}."

            answer = str(result)

        return Problem(
            problem_type="arithmetic_sequences",
            question=question,
            answer=answer,
            difficulty=4
        )