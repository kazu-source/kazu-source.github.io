"""
Solving Similar Triangles Generator
Creates problems about finding missing sides using triangle similarity
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SolvingSimilarTrianglesGenerator:
    """Generates problems about solving similar triangles."""

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
        """Set up and solve simple proportion"""
        # Small triangle sides
        a = random.randint(3, 8)
        b = random.randint(3, 8)

        # Scale factor
        k = random.randint(2, 4)

        # Large triangle sides
        a_prime = a * k
        b_prime = b * k

        # Ask for missing side
        problem_type = random.choice(['find_large', 'find_small'])

        if problem_type == 'find_large':
            latex = f"\\triangle ABC \\sim \\triangle DEF. \\text{{ If }} AB = {a}, DE = {a_prime}, \\text{{ and }} BC = {b}, \\text{{ find }} EF."
            solution = str(b_prime)

            steps = [
                f"\\text{{Set up proportion: }} \\frac{{AB}}{{DE}} = \\frac{{BC}}{{EF}}",
                f"\\frac{{{a}}}{{{a_prime}}} = \\frac{{{b}}}{{EF}}",
                f"EF = \\frac{{{b} \\times {a_prime}}}{{{a}}} = \\frac{{{b * a_prime}}}{{{a}}} = {b_prime}"
            ]
        else:
            latex = f"\\triangle ABC \\sim \\triangle DEF. \\text{{ If }} AB = {a}, DE = {a_prime}, \\text{{ and }} EF = {b_prime}, \\text{{ find }} BC."
            solution = str(b)

            steps = [
                f"\\text{{Set up proportion: }} \\frac{{AB}}{{DE}} = \\frac{{BC}}{{EF}}",
                f"\\frac{{{a}}}{{{a_prime}}} = \\frac{{BC}}{{{b_prime}}}",
                f"BC = \\frac{{{a} \\times {b_prime}}}{{{a_prime}}} = \\frac{{{a * b_prime}}}{{{a_prime}}} = {b}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Proportions with fractional or decimal answers"""
        a = random.randint(4, 10)
        b = random.randint(4, 10)
        c = random.randint(4, 10)

        # Scale factor as fraction
        k_num = random.randint(3, 5)
        k_den = 2

        a_prime = a * k_num // k_den
        b_prime = b * k_num // k_den

        # Make sure c_prime is clean
        c_prime = c * k_num // k_den

        latex = f"\\triangle PQR \\sim \\triangle XYZ. \\text{{ Given }} PQ = {a}, XY = {a_prime}, QR = {b}, YZ = {b_prime}. \\text{{ If }} PR = {c}, \\text{{ find }} XZ."
        solution = str(c_prime)

        steps = [
            f"\\text{{Find scale factor: }} \\frac{{XY}}{{PQ}} = \\frac{{{a_prime}}}{{{a}}} = {k_num / k_den}",
            f"XZ = PR \\times \\frac{{{k_num}}}{{{k_den}}} = {c} \\times {k_num / k_den} = {c_prime}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Algebraic: solve for x in similar triangles"""
        x = random.randint(2, 8)
        a = random.randint(2, 4)
        b = random.randint(1, 10)

        # Side in small triangle: ax + b
        side1 = a * x + b

        # Set up scale factor
        k = random.randint(2, 3)

        # Corresponding sides
        side2 = k * random.randint(3, 6)
        side1_large = k * side1 // 1  # Make it integer

        # Actually, let's set it up more carefully
        # Small: side_a = (ax + b), side_b = c
        # Large: side_a' = k(ax + b), side_b' = kc
        c = random.randint(4, 8)
        c_large = k * c

        latex = f"\\triangle ABC \\sim \\triangle DEF. \\text{{ If }} AB = {a}x + {b}, DE = {side1 * k}, BC = {c}, EF = {c_large}. \\text{{ Find }} x."
        solution = str(x)

        steps = [
            f"\\text{{Scale factor: }} \\frac{{EF}}{{BC}} = \\frac{{{c_large}}}{{{c}}} = {k}",
            f"\\text{{So: }} DE = {k} \\times AB",
            f"{side1 * k} = {k}({a}x + {b})",
            f"{side1 * k} = {k * a}x + {k * b}",
            f"{k * a}x = {side1 * k - k * b}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Word problems or nested similar triangles"""
        problem_type = random.choice(['shadow', 'nested', 'find_height'])

        if problem_type == 'shadow':
            # Shadow problem
            height1 = random.randint(5, 8)  # Person height in feet
            shadow1 = random.randint(3, 6)  # Person shadow
            shadow2 = random.randint(15, 30)  # Tree shadow

            height2 = height1 * shadow2 // shadow1

            latex = f"\\text{{A {height1}-foot person casts a {shadow1}-foot shadow. At the same time, a tree casts a {shadow2}-foot shadow. How tall is the tree?}}"
            solution = f"{height2} \\text{{ feet}}"

            steps = [
                f"\\text{{Similar triangles: }} \\frac{{\\text{{person height}}}}{{\\text{{person shadow}}}} = \\frac{{\\text{{tree height}}}}{{\\text{{tree shadow}}}}",
                f"\\frac{{{height1}}}{{{shadow1}}} = \\frac{{h}}{{{shadow2}}}",
                f"h = \\frac{{{height1} \\times {shadow2}}}{{{shadow1}}} = {height2} \\text{{ feet}}"
            ]

        elif problem_type == 'nested':
            # Triangle with parallel line creating similar triangles
            a = random.randint(3, 6)
            b = random.randint(4, 8)
            k = random.randint(2, 3)

            small_base = a
            large_base = a * k
            small_side = b
            large_side = b * k

            latex = f"\\text{{In }} \\triangle ABC, DE \\parallel BC. \\text{{ If }} AD = {a}, DB = {a * (k-1)}, AE = {b}, \\text{{ find }} EC."
            solution = str(b * (k - 1))

            steps = [
                f"\\text{{When }} DE \\parallel BC, \\triangle ADE \\sim \\triangle ABC",
                f"\\frac{{AD}}{{AB}} = \\frac{{AE}}{{AC}}",
                f"\\frac{{{a}}}{{{a + a*(k-1)}}} = \\frac{{{b}}}{{{b} + EC}}",
                f"\\frac{{{a}}}{{{a * k}}} = \\frac{{{b}}}{{{b} + EC}}",
                f"EC = {b * (k - 1)}"
            ]

        else:
            # Find building height using mirror
            eye_height = random.randint(5, 6)
            dist_to_mirror = random.randint(3, 5)
            dist_mirror_to_building = random.randint(20, 40)

            building_height = eye_height * dist_mirror_to_building // dist_to_mirror

            latex = f"\\text{{You stand {dist_to_mirror} ft from a mirror on the ground. The building is {dist_mirror_to_building} ft from the mirror. Your eye level is {eye_height} ft. How tall is the building?}}"
            solution = f"{building_height} \\text{{ ft}}"

            steps = [
                f"\\text{{Mirror creates similar triangles (angle of incidence = angle of reflection)}}",
                f"\\frac{{\\text{{your height}}}}{{\\text{{your distance}}}} = \\frac{{\\text{{building height}}}}{{\\text{{building distance}}}}",
                f"\\frac{{{eye_height}}}{{{dist_to_mirror}}} = \\frac{{h}}{{{dist_mirror_to_building}}}",
                f"h = \\frac{{{eye_height} \\times {dist_mirror_to_building}}}{{{dist_to_mirror}}} = {building_height} \\text{{ ft}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SolvingSimilarTrianglesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
