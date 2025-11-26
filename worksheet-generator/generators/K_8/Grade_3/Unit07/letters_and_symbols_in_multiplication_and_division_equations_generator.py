"""
Letters and Symbols in Multiplication and Division Equations Generator - Grade 3 Unit 7
Generates problems with variables/symbols in simple equations
Example: n × 4 = 20, ☐ ÷ 3 = 5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class LettersAndSymbolsGenerator:
    """Generates problems with variables in multiplication and division equations."""

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
        """Generate easy problems: simple multiplication with small numbers."""
        symbols = ['n', 'x', '\\square']
        symbol = random.choice(symbols)

        # Simple multiplication: n × a = b where a is 2-5 and n is 1-10
        multiplier = random.randint(2, 5)
        answer = random.randint(1, 10)
        product = answer * multiplier

        if random.choice([True, False]):
            # n × multiplier = product
            latex = f"{symbol} \\times {multiplier} = {product}"
            steps = [
                f"{symbol} \\times {multiplier} = {product}",
                f"{symbol} = {product} \\div {multiplier}",
                f"{symbol} = {answer}"
            ]
        else:
            # multiplier × n = product
            latex = f"{multiplier} \\times {symbol} = {product}"
            steps = [
                f"{multiplier} \\times {symbol} = {product}",
                f"{symbol} = {product} \\div {multiplier}",
                f"{symbol} = {answer}"
            ]

        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: multiplication and division with larger numbers."""
        symbols = ['n', 'x', '\\square']
        symbol = random.choice(symbols)

        if random.choice([True, False]):
            # Multiplication: n × a = b
            multiplier = random.randint(2, 10)
            answer = random.randint(2, 12)
            product = answer * multiplier

            if random.choice([True, False]):
                latex = f"{symbol} \\times {multiplier} = {product}"
            else:
                latex = f"{multiplier} \\times {symbol} = {product}"

            steps = [
                f"{symbol} = {product} \\div {multiplier}",
                f"{symbol} = {answer}"
            ]
        else:
            # Division: n ÷ a = b
            divisor = random.randint(2, 10)
            quotient = random.randint(2, 10)
            answer = divisor * quotient

            latex = f"{symbol} \\div {divisor} = {quotient}"
            steps = [
                f"{symbol} \\div {divisor} = {quotient}",
                f"{symbol} = {quotient} \\times {divisor}",
                f"{symbol} = {answer}"
            ]

        solution = str(answer)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: division and word contexts."""
        symbols = ['n', 'x', '\\square']
        symbol = random.choice(symbols)

        if random.choice([True, False]):
            # Division with variable in dividend
            divisor = random.randint(3, 10)
            quotient = random.randint(3, 12)
            answer = divisor * quotient

            contexts = [
                f"If {answer} apples are divided equally into {divisor} bags, how many are in each bag?",
                f"{answer} students sit in {divisor} equal rows. How many in each row?",
                f"A baker makes {answer} cookies and puts {divisor} cookies in each box. How many boxes?",
                f"{answer} pencils are shared equally among {divisor} students. How many each?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(quotient)
            steps = [
                f"{answer} \\div {divisor} = {symbol}",
                f"{symbol} = {quotient}"
            ]
        else:
            # Multiplication with word context
            multiplier = random.randint(3, 10)
            answer = random.randint(3, 12)
            product = answer * multiplier

            contexts = [
                f"Each box has {multiplier} crayons. If there are {product} crayons total, how many boxes?",
                f"Books cost ${multiplier} each. If you spend ${product}, how many books did you buy?",
                f"Each row has {multiplier} chairs. If there are {product} chairs total, how many rows?",
                f"If {multiplier} students sit at each table and there are {product} students, how many tables?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(answer)
            steps = [
                f"{symbol} \\times {multiplier} = {product}",
                f"{symbol} = {product} \\div {multiplier}",
                f"{symbol} = {answer}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex word problems with larger numbers."""
        symbols = ['n', 'x', '\\square']
        symbol = random.choice(symbols)

        problem_type = random.choice(['division_context', 'multiplication_context', 'missing_factor'])

        if problem_type == 'division_context':
            divisor = random.randint(5, 12)
            quotient = random.randint(5, 15)
            answer = divisor * quotient

            contexts = [
                f"A school has {answer} students who need to be divided into {divisor} equal classes. How many students per class?",
                f"A farmer has {answer} eggs to pack into cartons. Each carton holds {divisor} eggs. How many cartons needed?",
                f"There are {answer} pages in a book. If you read {divisor} pages each day, how many days to finish?",
                f"A recipe needs {answer} cups of flour. If each batch uses {divisor} cups, how many batches can you make?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(quotient)
            steps = [
                f"{answer} \\div {divisor} = {symbol}",
                f"{symbol} = {quotient}"
            ]

        elif problem_type == 'multiplication_context':
            multiplier = random.randint(6, 12)
            answer = random.randint(4, 15)
            product = answer * multiplier

            contexts = [
                f"Tickets cost ${multiplier} each. If the total cost is ${product}, how many tickets were bought?",
                f"Each box contains {multiplier} markers. If there are {product} markers total, how many boxes?",
                f"A garden has rows with {multiplier} plants each. If there are {product} plants, how many rows?",
                f"Each student needs {multiplier} pencils. If {product} pencils are needed total, how many students?"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}}}"
            solution = str(answer)
            steps = [
                f"{symbol} \\times {multiplier} = {product}",
                f"{symbol} = {product} \\div {multiplier}",
                f"{symbol} = {answer}"
            ]

        else:  # missing_factor
            # More complex: a × n = b where both a and b are larger
            multiplier = random.randint(7, 12)
            answer = random.randint(6, 12)
            product = answer * multiplier

            latex = f"{multiplier} \\times {symbol} = {product}"
            solution = str(answer)
            steps = [
                f"{multiplier} \\times {symbol} = {product}",
                f"{symbol} = {product} \\div {multiplier}",
                f"{symbol} = {answer}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = LettersAndSymbolsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")


if __name__ == '__main__':
    main()
