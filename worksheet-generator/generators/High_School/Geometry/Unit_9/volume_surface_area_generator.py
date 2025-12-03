"""
Volume and Surface Area Generator
Creates problems about volume and surface area of 3D shapes
"""

import random
import math
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class VolumeSurfaceAreaGenerator:
    """Generates problems about volume and surface area of 3D shapes."""

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
        """Volume of rectangular prism or cube"""
        shape = random.choice(['cube', 'rectangular_prism'])

        if shape == 'cube':
            s = random.randint(2, 8)
            volume = s ** 3

            latex = f"\\text{{Find the volume of a cube with side length }} {s}."
            solution = f"{volume} \\text{{ cubic units}}"

            steps = [
                f"V = s^3",
                f"V = {s}^3 = {volume}"
            ]
        else:
            l = random.randint(2, 8)
            w = random.randint(2, 8)
            h = random.randint(2, 8)
            volume = l * w * h

            latex = f"\\text{{Find the volume of a rectangular prism with length }} {l}, \\text{{ width }} {w}, \\text{{ height }} {h}."
            solution = f"{volume} \\text{{ cubic units}}"

            steps = [
                f"V = l \\times w \\times h",
                f"V = {l} \\times {w} \\times {h} = {volume}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Volume or SA of cylinder, cone, or prism"""
        shape = random.choice(['cylinder_volume', 'cylinder_sa', 'triangular_prism'])

        if shape == 'cylinder_volume':
            r = random.randint(2, 6)
            h = random.randint(3, 10)
            # V = πr²h

            latex = f"\\text{{Find the volume of a cylinder with radius }} {r} \\text{{ and height }} {h}. \\text{{ (Leave answer in terms of }} \\pi.)"
            solution = f"{r**2 * h}\\pi \\text{{ cubic units}}"

            steps = [
                f"V = \\pi r^2 h",
                f"V = \\pi ({r})^2 ({h})",
                f"V = \\pi \\cdot {r**2} \\cdot {h} = {r**2 * h}\\pi"
            ]

        elif shape == 'cylinder_sa':
            r = random.randint(2, 5)
            h = random.randint(3, 8)
            # SA = 2πr² + 2πrh = 2πr(r + h)

            latex = f"\\text{{Find the surface area of a cylinder with radius }} {r} \\text{{ and height }} {h}. \\text{{ (In terms of }} \\pi.)"
            solution = f"{2 * r * (r + h)}\\pi \\text{{ square units}}"

            steps = [
                f"SA = 2\\pi r^2 + 2\\pi rh = 2\\pi r(r + h)",
                f"SA = 2\\pi ({r})({r} + {h})",
                f"SA = 2\\pi ({r})({r + h}) = {2 * r * (r + h)}\\pi"
            ]

        else:
            # Triangular prism
            b = random.randint(3, 8)
            h_tri = random.randint(3, 8)
            length = random.randint(4, 10)
            # V = (1/2)bh × length

            volume = (b * h_tri * length) // 2

            latex = f"\\text{{Find the volume of a triangular prism with base }} {b}, \\text{{ triangle height }} {h_tri}, \\text{{ and length }} {length}."
            solution = f"{volume} \\text{{ cubic units}}"

            steps = [
                f"V = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\times \\text{{length}}",
                f"V = \\frac{{1}}{{2}} \\times {b} \\times {h_tri} \\times {length}",
                f"V = {volume}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Cone, sphere, or finding missing dimension"""
        shape = random.choice(['cone', 'sphere', 'find_dimension'])

        if shape == 'cone':
            r = random.randint(2, 6)
            h = random.randint(3, 9)
            # V = (1/3)πr²h

            latex = f"\\text{{Find the volume of a cone with radius }} {r} \\text{{ and height }} {h}. \\text{{ (In terms of }} \\pi.)"
            volume_coef = r**2 * h
            if volume_coef % 3 == 0:
                solution = f"{volume_coef // 3}\\pi \\text{{ cubic units}}"
            else:
                solution = f"\\frac{{{volume_coef}\\pi}}{{3}} \\text{{ cubic units}}"

            steps = [
                f"V = \\frac{{1}}{{3}}\\pi r^2 h",
                f"V = \\frac{{1}}{{3}}\\pi ({r})^2 ({h})",
                f"V = \\frac{{{volume_coef}\\pi}}{{3}}"
            ]

        elif shape == 'sphere':
            r = random.randint(2, 5)
            # V = (4/3)πr³

            vol_coef = 4 * r**3
            if vol_coef % 3 == 0:
                solution = f"{vol_coef // 3}\\pi \\text{{ cubic units}}"
            else:
                solution = f"\\frac{{{vol_coef}\\pi}}{{3}} \\text{{ cubic units}}"

            latex = f"\\text{{Find the volume of a sphere with radius }} {r}. \\text{{ (In terms of }} \\pi.)"

            steps = [
                f"V = \\frac{{4}}{{3}}\\pi r^3",
                f"V = \\frac{{4}}{{3}}\\pi ({r})^3",
                f"V = \\frac{{4}}{{3}}\\pi ({r**3}) = \\frac{{{vol_coef}\\pi}}{{3}}"
            ]

        else:
            # Find missing dimension given volume
            l = random.randint(3, 8)
            w = random.randint(3, 8)
            h = random.randint(2, 6)
            volume = l * w * h

            latex = f"\\text{{A rectangular prism has volume }} {volume} \\text{{ cubic units, length }} {l}, \\text{{ and width }} {w}. \\text{{ Find the height.}}"
            solution = str(h)

            steps = [
                f"V = l \\times w \\times h",
                f"{volume} = {l} \\times {w} \\times h",
                f"{volume} = {l * w} \\times h",
                f"h = \\frac{{{volume}}}{{{l * w}}} = {h}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Composite shapes or real-world applications"""
        problem_type = random.choice(['composite', 'word_problem', 'hemisphere'])

        if problem_type == 'composite':
            # Cylinder with hemisphere on top
            r = random.randint(2, 4)
            h = random.randint(4, 8)

            # V = πr²h + (2/3)πr³
            cyl_vol = r**2 * h
            hemi_vol = (2 * r**3)  # coefficient for (2/3)πr³

            latex = f"\\text{{Find the volume of a cylinder (r={r}, h={h}) with a hemisphere on top. (In terms of }} \\pi.)"

            if hemi_vol % 3 == 0:
                hemi_simple = hemi_vol // 3
                total = cyl_vol + hemi_simple
                solution = f"{total}\\pi \\text{{ cubic units}}"
            else:
                solution = f"\\left({cyl_vol} + \\frac{{{hemi_vol}}}{{3}}\\right)\\pi \\text{{ cubic units}}"

            steps = [
                f"V_{{\\text{{cylinder}}}} = \\pi r^2 h = \\pi({r})^2({h}) = {cyl_vol}\\pi",
                f"V_{{\\text{{hemisphere}}}} = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}}\\pi({r})^3 = \\frac{{{hemi_vol}}}{{3}}\\pi",
                f"V_{{\\text{{total}}}} = {cyl_vol}\\pi + \\frac{{{hemi_vol}}}{{3}}\\pi"
            ]

        elif problem_type == 'word_problem':
            # Fill a pool problem
            l = random.randint(8, 15)
            w = random.randint(5, 10)
            h = random.randint(2, 4)
            volume = l * w * h

            latex = f"\\text{{A rectangular swimming pool is {l} m long, {w} m wide, and {h} m deep. How many cubic meters of water does it hold?}}"
            solution = f"{volume} \\text{{ cubic meters}}"

            steps = [
                f"V = l \\times w \\times h",
                f"V = {l} \\times {w} \\times {h}",
                f"V = {volume} \\text{{ cubic meters}}"
            ]

        else:
            # Surface area of hemisphere
            r = random.randint(2, 5)
            # SA = 2πr² (curved) + πr² (base) = 3πr²

            latex = f"\\text{{Find the total surface area of a hemisphere with radius }} {r}. \\text{{ (In terms of }} \\pi.)"
            solution = f"{3 * r**2}\\pi \\text{{ square units}}"

            steps = [
                f"\\text{{Curved surface area}} = 2\\pi r^2 = 2\\pi({r})^2 = {2 * r**2}\\pi",
                f"\\text{{Base area}} = \\pi r^2 = \\pi({r})^2 = {r**2}\\pi",
                f"\\text{{Total SA}} = {2 * r**2}\\pi + {r**2}\\pi = {3 * r**2}\\pi"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = VolumeSurfaceAreaGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
