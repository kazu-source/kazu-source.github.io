"""
Special Right Triangles Generator
Creates problems about 30-60-90 and 45-45-90 triangles
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SpecialRightTrianglesGenerator:
    """Generates problems about special right triangles."""

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
        """Identify ratios of special triangles"""
        triangle_type = random.choice(['45-45-90', '30-60-90'])

        if triangle_type == '45-45-90':
            latex = f"\\text{{In a 45-45-90 triangle, if a leg is }} 1, \\text{{ what is the hypotenuse?}}"
            solution = "\\sqrt{2}"

            steps = [
                f"\\text{{45-45-90 ratio: }} 1 : 1 : \\sqrt{{2}}",
                f"\\text{{Leg : Leg : Hypotenuse}}",
                f"\\text{{If leg = 1, hypotenuse = }} \\sqrt{{2}}"
            ]
        else:
            part = random.choice(['short', 'long', 'hyp'])
            if part == 'short':
                latex = f"\\text{{In a 30-60-90 triangle, if the short leg is }} 1, \\text{{ what is the hypotenuse?}}"
                solution = "2"
                steps = [
                    f"\\text{{30-60-90 ratio: }} 1 : \\sqrt{{3}} : 2",
                    f"\\text{{Short leg : Long leg : Hypotenuse}}",
                    f"\\text{{If short leg = 1, hypotenuse = 2}}"
                ]
            elif part == 'long':
                latex = f"\\text{{In a 30-60-90 triangle, if the short leg is }} 1, \\text{{ what is the long leg?}}"
                solution = "\\sqrt{3}"
                steps = [
                    f"\\text{{30-60-90 ratio: }} 1 : \\sqrt{{3}} : 2",
                    f"\\text{{If short leg = 1, long leg = }} \\sqrt{{3}}"
                ]
            else:
                latex = f"\\text{{In a 30-60-90 triangle, the short leg is opposite which angle?}}"
                solution = "30°"
                steps = [
                    f"\\text{{The shortest side is opposite the smallest angle.}}",
                    f"\\text{{In a 30-60-90 triangle, the short leg is opposite 30°.}}"
                ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Find sides using integer multipliers"""
        triangle_type = random.choice(['45-45-90', '30-60-90'])

        if triangle_type == '45-45-90':
            leg = random.randint(2, 10)

            problem_type = random.choice(['find_hyp', 'find_leg'])

            if problem_type == 'find_hyp':
                latex = f"\\text{{In a 45-45-90 triangle, each leg is }} {leg}. \\text{{ Find the hypotenuse.}}"
                solution = f"{leg}\\sqrt{{2}}"

                steps = [
                    f"\\text{{45-45-90 ratio: leg : leg : leg}}\\sqrt{{2}}",
                    f"\\text{{Hypotenuse = leg}} \\times \\sqrt{{2}}",
                    f"\\text{{Hypotenuse = }} {leg}\\sqrt{{2}}"
                ]
            else:
                hyp_coef = leg
                latex = f"\\text{{In a 45-45-90 triangle, the hypotenuse is }} {hyp_coef}\\sqrt{{2}}. \\text{{ Find each leg.}}"
                solution = str(hyp_coef)

                steps = [
                    f"\\text{{Hypotenuse = leg}} \\times \\sqrt{{2}}",
                    f"{hyp_coef}\\sqrt{{2}} = \\text{{leg}} \\times \\sqrt{{2}}",
                    f"\\text{{leg = }} {hyp_coef}"
                ]
        else:
            short_leg = random.randint(2, 8)

            problem_type = random.choice(['find_long', 'find_hyp', 'find_short'])

            if problem_type == 'find_long':
                latex = f"\\text{{In a 30-60-90 triangle, the short leg is }} {short_leg}. \\text{{ Find the long leg.}}"
                solution = f"{short_leg}\\sqrt{{3}}"

                steps = [
                    f"\\text{{30-60-90 ratio: }} 1 : \\sqrt{{3}} : 2",
                    f"\\text{{Long leg = short leg}} \\times \\sqrt{{3}}",
                    f"\\text{{Long leg = }} {short_leg} \\times \\sqrt{{3}} = {short_leg}\\sqrt{{3}}"
                ]
            elif problem_type == 'find_hyp':
                latex = f"\\text{{In a 30-60-90 triangle, the short leg is }} {short_leg}. \\text{{ Find the hypotenuse.}}"
                solution = str(2 * short_leg)

                steps = [
                    f"\\text{{30-60-90 ratio: }} 1 : \\sqrt{{3}} : 2",
                    f"\\text{{Hypotenuse = 2}} \\times \\text{{short leg}}",
                    f"\\text{{Hypotenuse = 2}} \\times {short_leg} = {2 * short_leg}"
                ]
            else:
                hyp = 2 * short_leg
                latex = f"\\text{{In a 30-60-90 triangle, the hypotenuse is }} {hyp}. \\text{{ Find the short leg.}}"
                solution = str(short_leg)

                steps = [
                    f"\\text{{Hypotenuse = 2}} \\times \\text{{short leg}}",
                    f"{hyp} = 2 \\times \\text{{short leg}}",
                    f"\\text{{Short leg = }} \\frac{{{hyp}}}{{2}} = {short_leg}"
                ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Work with radical values or find from non-standard given"""
        triangle_type = random.choice(['45-45-90', '30-60-90'])

        if triangle_type == '45-45-90':
            # Given hypotenuse as integer, find leg
            hyp = random.randint(4, 12)

            latex = f"\\text{{In a 45-45-90 triangle, the hypotenuse is }} {hyp}. \\text{{ Find each leg.}}"
            solution = f"\\frac{{{hyp}\\sqrt{{2}}}}{{2}}"

            steps = [
                f"\\text{{Hypotenuse = leg}} \\times \\sqrt{{2}}",
                f"{hyp} = \\text{{leg}} \\times \\sqrt{{2}}",
                f"\\text{{leg}} = \\frac{{{hyp}}}{{\\sqrt{{2}}}} = \\frac{{{hyp}\\sqrt{{2}}}}{{2}}"
            ]
        else:
            # Given long leg, find others
            short = random.randint(2, 6)
            long_coef = short

            latex = f"\\text{{In a 30-60-90 triangle, the long leg is }} {long_coef}\\sqrt{{3}}. \\text{{ Find the short leg and hypotenuse.}}"
            solution = f"\\text{{Short leg = }} {short}, \\text{{ Hypotenuse = }} {2 * short}"

            steps = [
                f"\\text{{Long leg = short leg}} \\times \\sqrt{{3}}",
                f"{long_coef}\\sqrt{{3}} = \\text{{short leg}} \\times \\sqrt{{3}}",
                f"\\text{{Short leg = }} {short}",
                f"\\text{{Hypotenuse = 2}} \\times {short} = {2 * short}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Word problems and combined applications"""
        problem_type = random.choice(['diagonal', 'altitude', 'combined'])

        if problem_type == 'diagonal':
            # Diagonal of a square
            side = random.randint(4, 10)

            latex = f"\\text{{Find the diagonal of a square with side length }} {side}."
            solution = f"{side}\\sqrt{{2}}"

            steps = [
                f"\\text{{A square's diagonal creates two 45-45-90 triangles.}}",
                f"\\text{{Diagonal = side}} \\times \\sqrt{{2}}",
                f"\\text{{Diagonal = }} {side}\\sqrt{{2}}"
            ]

        elif problem_type == 'altitude':
            # Altitude of an equilateral triangle
            side = random.randint(4, 12) * 2  # Even for clean division

            latex = f"\\text{{Find the altitude of an equilateral triangle with side length }} {side}."
            solution = f"\\frac{{{side}\\sqrt{{3}}}}{{2}}"

            steps = [
                f"\\text{{The altitude creates two 30-60-90 triangles.}}",
                f"\\text{{Short leg (half the base) = }} \\frac{{{side}}}{{2}} = {side // 2}",
                f"\\text{{Altitude = short leg}} \\times \\sqrt{{3}} = {side // 2}\\sqrt{{3}} = \\frac{{{side}\\sqrt{{3}}}}{{2}}"
            ]

        else:
            # Find perimeter or area using special triangles
            short = random.randint(3, 6)
            long_leg = f"{short}\\sqrt{{3}}"
            hyp = 2 * short

            latex = f"\\text{{A 30-60-90 triangle has a short leg of }} {short}. \\text{{ Find its perimeter.}}"
            solution = f"{short + 2 * short} + {short}\\sqrt{{3}} = {3 * short} + {short}\\sqrt{{3}}"

            steps = [
                f"\\text{{Short leg = }} {short}",
                f"\\text{{Long leg = }} {short}\\sqrt{{3}}",
                f"\\text{{Hypotenuse = }} {hyp}",
                f"\\text{{Perimeter = }} {short} + {short}\\sqrt{{3}} + {hyp}",
                f"\\text{{Perimeter = }} {3 * short} + {short}\\sqrt{{3}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SpecialRightTrianglesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
