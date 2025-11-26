"""
Parts of a Term with Exponents Review Generator (Unit 9)
Reviews parts of a term, now including exponents
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class PartsOfTermExponentsReviewGenerator:
    """Generates review problems about parts of a term with exponents."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Easy: Identify coefficient, variable, and exponent"""
        coef = random.randint(2, 9)
        exp = random.randint(2, 4)
        
        question_type = random.choice(['coefficient', 'variable', 'exponent'])
        
        if question_type == 'coefficient':
            latex = f"\\text{{In the term }} {coef}x^{{{exp}}}\\text{{, what is the coefficient?}}"
            solution = coef
        elif question_type == 'variable':
            latex = f"\\text{{In the term }} {coef}x^{{{exp}}}\\text{{, what is the variable?}}"
            solution = "x"
        else:  # exponent
            latex = f"\\text{{In the term }} {coef}x^{{{exp}}}\\text{{, what is the exponent?}}"
            solution = exp

        steps = [
            f"\\text{{Term: coefficient}} \\times \\text{{variable}}^{{\\text{{exponent}}}}",
            f"{coef}x^{{{exp}}} = {coef} \\times x^{{{exp}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Medium: Identify all parts of more complex terms"""
        coef = random.randint(2, 12)
        var1_exp = random.randint(2, 4)
        var2_exp = random.randint(1, 3)
        
        latex = f"\\text{{In the term }} {coef}x^{{{var1_exp}}}y^{{{var2_exp}}}\\text{{, identify: coefficient, variables, and exponents.}}"
        solution = f"Coef: {coef}, Vars: x,y, Exp: {var1_exp},{var2_exp}"

        steps = [
            f"\\text{{Coefficient: }} {coef}",
            f"\\text{{Variables: }} x \\text{{ and }} y",
            f"\\text{{Exponents: }} {var1_exp} \\text{{ on }} x\\text{{, }} {var2_exp} \\text{{ on }} y"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Hard: Write term given parts"""
        coef = random.randint(2, 15)
        var = random.choice(['x', 'a', 'n'])
        exp = random.randint(2, 5)
        
        latex = f"\\text{{Write a term with coefficient }} {coef}\\text{{, variable }} {var}\\text{{, and exponent }} {exp}"
        solution = f"{coef}{var}^{{{exp}}}"

        steps = [
            f"\\text{{Format: coefficient}} \\times \\text{{variable}}^{{\\text{{exponent}}}}",
            f"\\text{{Answer: }} {coef}{var}^{{{exp}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Challenge: Complex terms with negative exponents or fractions"""
        problem_type = random.choice(['negative_exp', 'fraction_coef', 'multiple_vars'])
        
        if problem_type == 'negative_exp':
            coef = random.randint(2, 8)
            exp = random.randint(-3, -1)
            
            latex = f"\\text{{In }} {coef}x^{{{exp}}}\\text{{, what does the negative exponent mean?}}"
            solution = f"1/{coef}x^{{{abs(exp)}}}" if coef == 1 else f"{coef}/x^{{{abs(exp)}}}"
            
            steps = [
                f"\\text{{Negative exponent means reciprocal}}",
                f"{coef}x^{{{exp}}} = \\frac{{{coef}}}{{x^{{{abs(exp)}}}}}"
            ]
            
        elif problem_type == 'fraction_coef':
            num = random.randint(1, 5)
            denom = random.randint(2, 6)
            exp = random.randint(2, 4)
            
            latex = f"\\text{{In }} \\frac{{{num}}}{{{denom}}}x^{{{exp}}}\\text{{, what is the coefficient?}}"
            solution = f"{num}/{denom}"
            
            steps = [
                f"\\text{{Coefficient is the number multiplying the variable}}",
                f"\\text{{Coefficient: }} \\frac{{{num}}}{{{denom}}}"
            ]
            
        else:  # multiple_vars
            coef = random.randint(2, 10)
            exp1 = random.randint(2, 4)
            exp2 = random.randint(2, 3)
            exp3 = random.randint(1, 2)
            
            latex = f"\\text{{Find the degree (sum of exponents) of }} {coef}x^{{{exp1}}}y^{{{exp2}}}z^{{{exp3}}}"
            solution = exp1 + exp2 + exp3
            
            steps = [
                f"\\text{{Degree = sum of all exponents}}",
                f"\\text{{Degree}} = {exp1} + {exp2} + {exp3} = {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

