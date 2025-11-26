"""
Polynomial Operations Generator - Unit 9
Generates problems for adding, subtracting, and multiplying polynomials
"""

import random
from dataclasses import dataclass
from typing import List, Tuple, Dict


@dataclass
class PolynomialProblem:
    """Represents a polynomial operation problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The simplified answer
    difficulty: str
    operation: str  # 'add', 'subtract', 'multiply'
    problem_type: str  # Specific type of problem


class PolynomialOperationsGenerator:
    """Generates problems for polynomial operations."""

    def __init__(self, seed=None):
        """Initialize the polynomial operations generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[PolynomialProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of PolynomialProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> PolynomialProblem:
        """Generate a single polynomial problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _format_polynomial(self, terms: Dict[int, int]) -> str:
        """
        Format a polynomial from a dictionary of {degree: coefficient}.
        """
        if not terms or all(coeff == 0 for coeff in terms.values()):
            return "0"

        result = []
        for degree in sorted(terms.keys(), reverse=True):
            coeff = terms[degree]
            if coeff == 0:
                continue

            if degree == 0:
                # Constant term
                if result:
                    result.append(f"{coeff:+d}")
                else:
                    result.append(str(coeff))
            elif degree == 1:
                # Linear term
                if coeff == 1:
                    term = "x" if not result else "+x"
                elif coeff == -1:
                    term = "-x"
                else:
                    term = f"{coeff:+d}x" if result else f"{coeff}x"
                result.append(term)
            else:
                # Higher degree terms
                if coeff == 1:
                    term = f"x^{{{degree}}}" if not result else f"+x^{{{degree}}}"
                elif coeff == -1:
                    term = f"-x^{{{degree}}}"
                else:
                    term = f"{coeff:+d}x^{{{degree}}}" if result else f"{coeff}x^{{{degree}}}"
                result.append(term)

        return "".join(result).replace("+-", "-")

    def _add_polynomials(self, poly1: Dict, poly2: Dict) -> Dict:
        """Add two polynomials."""
        result = poly1.copy()
        for degree, coeff in poly2.items():
            result[degree] = result.get(degree, 0) + coeff
        return {d: c for d, c in result.items() if c != 0}

    def _subtract_polynomials(self, poly1: Dict, poly2: Dict) -> Dict:
        """Subtract poly2 from poly1."""
        result = poly1.copy()
        for degree, coeff in poly2.items():
            result[degree] = result.get(degree, 0) - coeff
        return {d: c for d, c in result.items() if c != 0}

    def _multiply_polynomials(self, poly1: Dict, poly2: Dict) -> Dict:
        """Multiply two polynomials."""
        result = {}
        for d1, c1 in poly1.items():
            for d2, c2 in poly2.items():
                degree = d1 + d2
                result[degree] = result.get(degree, 0) + c1 * c2
        return {d: c for d, c in result.items() if c != 0}

    def _generate_easy(self) -> PolynomialProblem:
        """Generate easy polynomial problems (add/subtract simple polynomials)."""
        problem_type = random.choice(['add_binomials', 'subtract_binomials', 'multiply_monomials'])

        if problem_type == 'add_binomials':
            # Add two binomials
            a1 = random.randint(-5, 5)
            b1 = random.randint(-5, 5)
            a2 = random.randint(-5, 5)
            b2 = random.randint(-5, 5)

            poly1 = {1: a1, 0: b1} if a1 != 0 else {0: b1}
            poly2 = {1: a2, 0: b2} if a2 != 0 else {0: b2}

            latex = f"({self._format_polynomial(poly1)}) + ({self._format_polynomial(poly2)})"
            result = self._add_polynomials(poly1, poly2)
            solution = self._format_polynomial(result)
            operation = 'add'

        elif problem_type == 'subtract_binomials':
            # Subtract two binomials
            a1 = random.randint(-5, 5)
            b1 = random.randint(-5, 5)
            a2 = random.randint(-5, 5)
            b2 = random.randint(-5, 5)

            poly1 = {1: a1, 0: b1} if a1 != 0 else {0: b1}
            poly2 = {1: a2, 0: b2} if a2 != 0 else {0: b2}

            latex = f"({self._format_polynomial(poly1)}) - ({self._format_polynomial(poly2)})"
            result = self._subtract_polynomials(poly1, poly2)
            solution = self._format_polynomial(result)
            operation = 'subtract'

        else:  # multiply_monomials
            # Multiply two monomials
            coeff1 = random.randint(1, 5)
            exp1 = random.randint(1, 3)
            coeff2 = random.randint(1, 5)
            exp2 = random.randint(1, 3)

            latex = f"{coeff1}x^{{{exp1}}} \\cdot {coeff2}x^{{{exp2}}}"
            solution = f"{coeff1 * coeff2}x^{{{exp1 + exp2}}}"
            operation = 'multiply'

        return PolynomialProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            operation=operation,
            problem_type=problem_type
        )

    def _generate_medium(self) -> PolynomialProblem:
        """Generate medium polynomial problems (trinomials, monomial-binomial multiplication)."""
        problem_type = random.choice(['add_trinomials', 'multiply_monomial_binomial', 'subtract_mixed'])

        if problem_type == 'add_trinomials':
            # Add two trinomials
            poly1 = {
                2: random.randint(-3, 3),
                1: random.randint(-5, 5),
                0: random.randint(-5, 5)
            }
            poly2 = {
                2: random.randint(-3, 3),
                1: random.randint(-5, 5),
                0: random.randint(-5, 5)
            }

            # Remove zero coefficients
            poly1 = {d: c for d, c in poly1.items() if c != 0}
            poly2 = {d: c for d, c in poly2.items() if c != 0}

            latex = f"({self._format_polynomial(poly1)}) + ({self._format_polynomial(poly2)})"
            result = self._add_polynomials(poly1, poly2)
            solution = self._format_polynomial(result)
            operation = 'add'

        elif problem_type == 'multiply_monomial_binomial':
            # Multiply monomial by binomial
            mono_coeff = random.randint(2, 5)
            mono_exp = random.randint(1, 2)
            mono = {mono_exp: mono_coeff}

            bi_a = random.randint(-4, 4)
            bi_b = random.randint(-5, 5)
            binomial = {1: bi_a, 0: bi_b} if bi_a != 0 else {0: bi_b}

            latex = f"{self._format_polynomial(mono)} \\cdot ({self._format_polynomial(binomial)})"
            result = self._multiply_polynomials(mono, binomial)
            solution = self._format_polynomial(result)
            operation = 'multiply'

        else:  # subtract_mixed
            # Subtract polynomial from polynomial
            poly1 = {
                3: random.randint(-2, 2),
                2: random.randint(-3, 3),
                1: random.randint(-5, 5),
                0: random.randint(-5, 5)
            }
            poly2 = {
                2: random.randint(-3, 3),
                1: random.randint(-5, 5),
                0: random.randint(-5, 5)
            }

            # Remove zero coefficients
            poly1 = {d: c for d, c in poly1.items() if c != 0}
            poly2 = {d: c for d, c in poly2.items() if c != 0}

            latex = f"({self._format_polynomial(poly1)}) - ({self._format_polynomial(poly2)})"
            result = self._subtract_polynomials(poly1, poly2)
            solution = self._format_polynomial(result)
            operation = 'subtract'

        return PolynomialProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            operation=operation,
            problem_type=problem_type
        )

    def _generate_hard(self) -> PolynomialProblem:
        """Generate hard polynomial problems (binomial multiplication, complex operations)."""
        problem_type = random.choice(['multiply_binomials', 'foil_method', 'complex_add_subtract'])

        if problem_type == 'multiply_binomials' or problem_type == 'foil_method':
            # Multiply two binomials (FOIL)
            a1 = random.randint(-4, 4)
            if a1 == 0:
                a1 = 1
            b1 = random.randint(-6, 6)
            a2 = random.randint(-4, 4)
            if a2 == 0:
                a2 = 1
            b2 = random.randint(-6, 6)

            poly1 = {1: a1, 0: b1}
            poly2 = {1: a2, 0: b2}

            latex = f"({self._format_polynomial(poly1)})({self._format_polynomial(poly2)})"
            result = self._multiply_polynomials(poly1, poly2)
            solution = self._format_polynomial(result)
            operation = 'multiply'

        else:  # complex_add_subtract
            # Complex polynomial addition/subtraction
            poly1 = {
                4: random.randint(-2, 2),
                3: random.randint(-3, 3),
                2: random.randint(-4, 4),
                1: random.randint(-5, 5),
                0: random.randint(-6, 6)
            }
            poly2 = {
                4: random.randint(-2, 2),
                2: random.randint(-4, 4),
                1: random.randint(-5, 5),
                0: random.randint(-6, 6)
            }

            # Remove zero coefficients
            poly1 = {d: c for d, c in poly1.items() if c != 0}
            poly2 = {d: c for d, c in poly2.items() if c != 0}

            if random.choice([True, False]):
                latex = f"({self._format_polynomial(poly1)}) + ({self._format_polynomial(poly2)})"
                result = self._add_polynomials(poly1, poly2)
                operation = 'add'
            else:
                latex = f"({self._format_polynomial(poly1)}) - ({self._format_polynomial(poly2)})"
                result = self._subtract_polynomials(poly1, poly2)
                operation = 'subtract'

            solution = self._format_polynomial(result)

        return PolynomialProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            operation=operation,
            problem_type=problem_type
        )

    def _generate_challenge(self) -> PolynomialProblem:
        """Generate challenge polynomial problems (trinomial multiplication, special products)."""
        problem_type = random.choice(['multiply_trinomials', 'special_product', 'triple_product'])

        if problem_type == 'multiply_trinomials':
            # Multiply binomial by trinomial
            bi_a = random.randint(-3, 3)
            if bi_a == 0:
                bi_a = 1
            bi_b = random.randint(-4, 4)
            binomial = {1: bi_a, 0: bi_b}

            tri_a = random.randint(-2, 2)
            if tri_a == 0:
                tri_a = 1
            tri_b = random.randint(-3, 3)
            tri_c = random.randint(-4, 4)
            trinomial = {2: tri_a, 1: tri_b, 0: tri_c}
            trinomial = {d: c for d, c in trinomial.items() if c != 0}

            latex = f"({self._format_polynomial(binomial)})({self._format_polynomial(trinomial)})"
            result = self._multiply_polynomials(binomial, trinomial)
            solution = self._format_polynomial(result)
            operation = 'multiply'

        elif problem_type == 'special_product':
            # Special products: (a+b)^2 or (a-b)^2 or (a+b)(a-b)
            product_type = random.choice(['square_sum', 'square_diff', 'diff_squares'])

            if product_type == 'square_sum':
                # (ax + b)^2
                a = random.randint(1, 3)
                b = random.randint(1, 5)
                latex = f"(x + {b})^2" if a == 1 else f"({a}x + {b})^2"
                # Result: a^2*x^2 + 2ab*x + b^2
                result = {2: a*a, 1: 2*a*b, 0: b*b}
                solution = self._format_polynomial(result)

            elif product_type == 'square_diff':
                # (ax - b)^2
                a = random.randint(1, 3)
                b = random.randint(1, 5)
                latex = f"(x - {b})^2" if a == 1 else f"({a}x - {b})^2"
                # Result: a^2*x^2 - 2ab*x + b^2
                result = {2: a*a, 1: -2*a*b, 0: b*b}
                solution = self._format_polynomial(result)

            else:  # diff_squares
                # (ax + b)(ax - b)
                a = random.randint(1, 3)
                b = random.randint(1, 6)
                latex = f"(x + {b})(x - {b})" if a == 1 else f"({a}x + {b})({a}x - {b})"
                # Result: a^2*x^2 - b^2
                result = {2: a*a, 0: -b*b}
                solution = self._format_polynomial(result)

            operation = 'multiply'

        else:  # triple_product
            # Multiply three simple factors
            # (x + a)(x + b)(x + c)
            a = random.randint(-3, 3)
            b = random.randint(-3, 3)
            c = random.randint(-3, 3)

            # First multiply (x + a)(x + b)
            poly1 = {1: 1, 0: a}
            poly2 = {1: 1, 0: b}
            intermediate = self._multiply_polynomials(poly1, poly2)

            # Then multiply result by (x + c)
            poly3 = {1: 1, 0: c}
            result = self._multiply_polynomials(intermediate, poly3)

            latex = f"(x {a:+d})(x {b:+d})(x {c:+d})".replace("+-", "-")
            solution = self._format_polynomial(result)
            operation = 'multiply'

        return PolynomialProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            operation=operation,
            problem_type=problem_type
        )


if __name__ == "__main__":
    # Test the generator
    gen = PolynomialOperationsGenerator()

    print("Testing Polynomial Operations Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Simplify: {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Operation: {problem.operation}")
            print(f"   Type: {problem.problem_type}")