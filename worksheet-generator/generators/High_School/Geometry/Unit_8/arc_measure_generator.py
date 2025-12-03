"""
Arc Measure Generator
Creates problems about central angles and arc measures
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ArcMeasureGenerator:
    """Generates problems about arc measures and central angles."""

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
        """Central angle equals arc measure"""
        central_angle = random.randint(30, 150)

        problem_type = random.choice(['find_arc', 'find_angle'])

        if problem_type == 'find_arc':
            latex = f"\\text{{A central angle measures }} {central_angle}°. \\text{{ What is the measure of its intercepted arc?}}"
            solution = f"{central_angle}°"
            steps = [
                f"\\text{{The measure of an arc equals its central angle.}}",
                f"\\text{{Arc measure}} = {central_angle}°"
            ]
        else:
            latex = f"\\text{{An arc measures }} {central_angle}°. \\text{{ What is the measure of its central angle?}}"
            solution = f"{central_angle}°"
            steps = [
                f"\\text{{A central angle equals the measure of its intercepted arc.}}",
                f"\\text{{Central angle}} = {central_angle}°"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Minor and major arcs"""
        minor_arc = random.randint(40, 170)
        major_arc = 360 - minor_arc

        problem_type = random.choice(['find_major', 'find_minor'])

        if problem_type == 'find_major':
            latex = f"\\text{{Minor arc AB measures }} {minor_arc}°. \\text{{ Find the measure of major arc AB.}}"
            solution = f"{major_arc}°"
            steps = [
                f"\\text{{Minor arc + Major arc = 360°}}",
                f"\\text{{Major arc}} = 360° - {minor_arc}° = {major_arc}°"
            ]
        else:
            latex = f"\\text{{Major arc AB measures }} {major_arc}°. \\text{{ Find the measure of minor arc AB.}}"
            solution = f"{minor_arc}°"
            steps = [
                f"\\text{{Minor arc + Major arc = 360°}}",
                f"\\text{{Minor arc}} = 360° - {major_arc}° = {minor_arc}°"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Arc addition or algebraic problems"""
        problem_type = random.choice(['arc_addition', 'algebraic'])

        if problem_type == 'arc_addition':
            # Three points on circle: find total arc
            arc1 = random.randint(30, 80)
            arc2 = random.randint(30, 80)
            arc3 = 360 - arc1 - arc2

            latex = f"\\text{{Points A, B, C are on a circle. Arc AB = }} {arc1}°, \\text{{ arc BC = }} {arc2}°. \\text{{ Find arc AC (the long way, through B).}}"
            solution = f"{arc1 + arc2}°"

            steps = [
                f"\\text{{Arc AC (through B) = Arc AB + Arc BC}}",
                f"= {arc1}° + {arc2}° = {arc1 + arc2}°"
            ]
        else:
            # Solve for x
            x = random.randint(5, 20)
            a = random.randint(2, 5)
            b = random.randint(1, 30)
            arc1 = a * x + b
            arc2 = 360 - arc1

            latex = f"\\text{{Two arcs of a circle measure }} ({a}x + {b})° \\text{{ and }} {arc2}°. \\text{{ Find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Sum of arcs}} = 360°",
                f"({a}x + {b}) + {arc2} = 360",
                f"{a}x + {b + arc2} = 360",
                f"{a}x = {360 - b - arc2}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Congruent arcs or arcs from congruent chords"""
        problem_type = random.choice(['congruent_chords', 'inscribed_polygon'])

        if problem_type == 'congruent_chords':
            arc = random.randint(40, 90)

            latex = f"\\text{{In a circle, two chords are congruent. One chord intercepts an arc of }} {arc}°. \\text{{ What arc does the other chord intercept?}}"
            solution = f"{arc}°"

            steps = [
                f"\\text{{Congruent chords intercept congruent arcs.}}",
                f"\\text{{Both arcs measure }} {arc}°"
            ]
        else:
            # Regular polygon inscribed in circle
            n = random.choice([3, 4, 5, 6, 8])
            names = {3: "triangle", 4: "square", 5: "pentagon", 6: "hexagon", 8: "octagon"}
            arc = 360 // n

            latex = f"\\text{{A regular {names[n]} is inscribed in a circle. Find the measure of each arc between consecutive vertices.}}"
            solution = f"{arc}°"

            steps = [
                f"\\text{{A regular {names[n]} has {n} equal sides.}}",
                f"\\text{{It divides the circle into {n} equal arcs.}}",
                f"\\text{{Each arc}} = \\frac{{360°}}{{{n}}} = {arc}°"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = ArcMeasureGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
