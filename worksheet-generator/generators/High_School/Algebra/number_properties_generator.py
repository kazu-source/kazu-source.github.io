"""
Number Properties Generator - Commutative, Associative, and Distributive Properties
Generates problems about identifying and applying number properties
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class NumberPropertiesGenerator:
    """Generates problems for number properties."""

    def __init__(self, seed=None):
        """Initialize the number properties generator."""
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
        """Generate a single number properties problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple property identification"""
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        property_type = random.choice(['commutative_add', 'commutative_mult', 'identity'])

        if property_type == 'commutative_add':
            latex = f"\\text{{Which property? }} {a} + {b} = {b} + {a}"
            solution = "Commutative (Addition)"
        elif property_type == 'commutative_mult':
            latex = f"\\text{{Which property? }} {a} \\times {b} = {b} \\times {a}"
            solution = "Commutative (Multiplication)"
        else:  # identity
            if random.choice([True, False]):
                latex = f"\\text{{Which property? }} {a} + 0 = {a}"
                solution = "Identity (Addition)"
            else:
                latex = f"\\text{{Which property? }} {a} \\times 1 = {a}"
                solution = "Identity (Multiplication)"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate associative property problems"""
        a = random.randint(2, 7)
        b = random.randint(2, 7)
        c = random.randint(2, 7)

        property_type = random.choice(['associative_add', 'associative_mult', 'apply_assoc'])

        if property_type == 'associative_add':
            latex = f"\\text{{Which property? }} ({a} + {b}) + {c} = {a} + ({b} + {c})"
            solution = "Associative (Addition)"
        elif property_type == 'associative_mult':
            latex = f"\\text{{Which property? }} ({a} \\times {b}) \\times {c} = {a} \\times ({b} \\times {c})"
            solution = "Associative (Multiplication)"
        else:  # apply_assoc
            latex = f"\\text{{Use associative property: }} ({a} + {b}) + {c}"
            solution = str((a + b) + c)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate distributive property problems"""
        a = random.randint(2, 8)
        b = random.randint(2, 6)
        c = random.randint(2, 6)

        problem_type = random.choice(['identify_dist', 'apply_dist', 'factor_out'])

        if problem_type == 'identify_dist':
            latex = f"\\text{{Which property? }} {a}({b} + {c}) = {a} \\times {b} + {a} \\times {c}"
            solution = "Distributive"
        elif problem_type == 'apply_dist':
            latex = f"\\text{{Distribute: }} {a}({b} + {c})"
            solution = f"{a * b} + {a * c}"
        else:  # factor_out
            term1 = a * b
            term2 = a * c
            latex = f"\\text{{Factor: }} {term1} + {term2}"
            solution = f"{a}({b} + {c})"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate mixed property problems"""
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(2, 6)
        d = random.randint(2, 6)

        problem_type = random.choice(['multi_property', 'complex_dist', 'inverse'])

        if problem_type == 'multi_property':
            latex = f"\\text{{Name all properties: }} {a} \\times ({b} + {c}) = ({b} + {c}) \\times {a}"
            solution = "Commutative and Distributive"
        elif problem_type == 'complex_dist':
            latex = f"\\text{{Distribute: }} ({a} + {b})({c} + {d})"
            result = a*c + a*d + b*c + b*d
            solution = str(result)
        else:  # inverse
            latex = f"\\text{{Which property? }} {a} + (-{a}) = 0"
            solution = "Inverse (Addition)"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = NumberPropertiesGenerator()

    print("Testing Number Properties Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")