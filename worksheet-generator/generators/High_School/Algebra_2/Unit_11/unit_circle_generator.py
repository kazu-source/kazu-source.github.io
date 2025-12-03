"""
Unit Circle Generator
Creates problems about values on the unit circle
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class UnitCircleGenerator:
    """Generates problems about the unit circle."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

        # Unit circle values: (degrees, radians, cos, sin)
        self.unit_circle = {
            0: ("0", "1", "0"),
            30: ("\\frac{\\pi}{6}", "\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}"),
            45: ("\\frac{\\pi}{4}", "\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}"),
            60: ("\\frac{\\pi}{3}", "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"),
            90: ("\\frac{\\pi}{2}", "0", "1"),
            120: ("\\frac{2\\pi}{3}", "-\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"),
            135: ("\\frac{3\\pi}{4}", "-\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}"),
            150: ("\\frac{5\\pi}{6}", "-\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}"),
            180: ("\\pi", "-1", "0"),
            210: ("\\frac{7\\pi}{6}", "-\\frac{\\sqrt{3}}{2}", "-\\frac{1}{2}"),
            225: ("\\frac{5\\pi}{4}", "-\\frac{\\sqrt{2}}{2}", "-\\frac{\\sqrt{2}}{2}"),
            240: ("\\frac{4\\pi}{3}", "-\\frac{1}{2}", "-\\frac{\\sqrt{3}}{2}"),
            270: ("\\frac{3\\pi}{2}", "0", "-1"),
            300: ("\\frac{5\\pi}{3}", "\\frac{1}{2}", "-\\frac{\\sqrt{3}}{2}"),
            315: ("\\frac{7\\pi}{4}", "\\frac{\\sqrt{2}}{2}", "-\\frac{\\sqrt{2}}{2}"),
            330: ("\\frac{11\\pi}{6}", "\\frac{\\sqrt{3}}{2}", "-\\frac{1}{2}"),
            360: ("2\\pi", "1", "0"),
        }

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
        """Find sin or cos for quadrant 1 angles"""
        angle = random.choice([0, 30, 45, 60, 90])
        radians, cos_val, sin_val = self.unit_circle[angle]

        trig_func = random.choice(['sin', 'cos'])

        if trig_func == 'sin':
            latex = f"\\text{{Find }} \\sin({angle}°)"
            solution = sin_val
        else:
            latex = f"\\text{{Find }} \\cos({angle}°)"
            solution = cos_val

        steps = [
            f"\\text{{On the unit circle at }} {angle}°:",
            f"\\text{{The point is }} ({cos_val}, {sin_val})",
            f"\\{trig_func}({angle}°) = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Find trig values in any quadrant using degrees"""
        angle = random.choice([120, 135, 150, 210, 225, 240, 300, 315, 330])
        radians, cos_val, sin_val = self.unit_circle[angle]

        trig_func = random.choice(['sin', 'cos', 'tan'])

        if trig_func == 'sin':
            latex = f"\\text{{Find }} \\sin({angle}°)"
            solution = sin_val
        elif trig_func == 'cos':
            latex = f"\\text{{Find }} \\cos({angle}°)"
            solution = cos_val
        else:
            # tan = sin/cos
            if cos_val == "0":
                latex = f"\\text{{Find }} \\tan({angle}°)"
                solution = "\\text{undefined}"
            else:
                latex = f"\\text{{Find }} \\tan({angle}°)"
                solution = f"\\frac{{{sin_val}}}{{{cos_val}}}"

        # Determine quadrant
        if angle < 90:
            quad = "I"
        elif angle < 180:
            quad = "II"
        elif angle < 270:
            quad = "III"
        else:
            quad = "IV"

        steps = [
            f"\\text{{{angle}° is in Quadrant {quad}}}",
            f"\\text{{Reference angle: }} {angle % 90 if angle % 90 != 0 else (180 - angle if angle < 180 else angle - 180) % 90}°" if angle % 90 != 0 else f"\\text{{On an axis}}",
            f"\\{trig_func}({angle}°) = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Find trig values using radians"""
        angle = random.choice([30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330])
        radians, cos_val, sin_val = self.unit_circle[angle]

        trig_func = random.choice(['sin', 'cos'])

        if trig_func == 'sin':
            latex = f"\\text{{Find }} \\sin\\left({radians}\\right)"
            solution = sin_val
        else:
            latex = f"\\text{{Find }} \\cos\\left({radians}\\right)"
            solution = cos_val

        steps = [
            f"{radians} \\text{{ radians}} = {angle}°",
            f"\\text{{Look up on unit circle:}}",
            f"\\{trig_func}\\left({radians}\\right) = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Find coordinates, solve for angle, or use identities"""
        problem_type = random.choice(['coordinates', 'find_angle', 'all_six'])

        if problem_type == 'coordinates':
            angle = random.choice([30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330])
            radians, cos_val, sin_val = self.unit_circle[angle]

            latex = f"\\text{{Find the coordinates of the point on the unit circle at angle }} {radians}."
            solution = f"\\left({cos_val}, {sin_val}\\right)"

            steps = [
                f"\\text{{On the unit circle, point}} = (\\cos\\theta, \\sin\\theta)",
                f"\\cos\\left({radians}\\right) = {cos_val}",
                f"\\sin\\left({radians}\\right) = {sin_val}",
                f"\\text{{Point: }} ({cos_val}, {sin_val})"
            ]

        elif problem_type == 'find_angle':
            # Given sin or cos value, find angle
            values = [
                ("\\frac{1}{2}", [30, 150], "sin"),
                ("\\frac{\\sqrt{2}}{2}", [45, 135], "sin"),
                ("\\frac{\\sqrt{3}}{2}", [60, 120], "sin"),
                ("-\\frac{1}{2}", [210, 330], "sin"),
            ]

            val, angles, func = random.choice(values)

            latex = f"\\text{{Find all angles }} \\theta \\text{{ in }} [0°, 360°) \\text{{ where }} \\{func}(\\theta) = {val}"
            solution = f"{angles[0]}° \\text{{ and }} {angles[1]}°"

            steps = [
                f"\\text{{The value }} {val} \\text{{ occurs at two angles in }} [0°, 360°)",
                f"\\text{{These are }} {angles[0]}° \\text{{ and }} {angles[1]}°"
            ]

        else:
            # Find all six trig values
            angle = random.choice([30, 45, 60])
            radians, cos_val, sin_val = self.unit_circle[angle]

            latex = f"\\text{{Find all six trigonometric values for }} {angle}°."

            if angle == 30:
                tan = "\\frac{1}{\\sqrt{3}}"
                cot = "\\sqrt{3}"
                sec = "\\frac{2}{\\sqrt{3}}"
                csc = "2"
            elif angle == 45:
                tan = "1"
                cot = "1"
                sec = "\\sqrt{2}"
                csc = "\\sqrt{2}"
            else:  # 60
                tan = "\\sqrt{3}"
                cot = "\\frac{1}{\\sqrt{3}}"
                sec = "2"
                csc = "\\frac{2}{\\sqrt{3}}"

            solution = f"\\sin={sin_val}, \\cos={cos_val}, \\tan={tan}, \\csc={csc}, \\sec={sec}, \\cot={cot}"

            steps = [
                f"\\sin({angle}°) = {sin_val}, \\cos({angle}°) = {cos_val}",
                f"\\tan = \\frac{{\\sin}}{{\\cos}} = {tan}",
                f"\\csc = \\frac{{1}}{{\\sin}} = {csc}",
                f"\\sec = \\frac{{1}}{{\\cos}} = {sec}",
                f"\\cot = \\frac{{1}}{{\\tan}} = {cot}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = UnitCircleGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
