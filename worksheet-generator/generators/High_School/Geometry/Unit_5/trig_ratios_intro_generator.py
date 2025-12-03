"""
Trigonometric Ratios Introduction Generator
Creates problems about sine, cosine, and tangent ratios
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class TrigRatiosIntroGenerator:
    """Generates problems about basic trigonometric ratios."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
        # Pythagorean triples for clean ratios
        self.triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]

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
        """Identify the ratio (SOH-CAH-TOA)"""
        ratios = [
            ("\\sin", "opposite", "hypotenuse", "SOH: Sine = Opposite / Hypotenuse"),
            ("\\cos", "adjacent", "hypotenuse", "CAH: Cosine = Adjacent / Hypotenuse"),
            ("\\tan", "opposite", "adjacent", "TOA: Tangent = Opposite / Adjacent"),
        ]

        func, num, den, mnemonic = random.choice(ratios)

        latex = f"\\text{{In a right triangle, }} {func}(\\theta) = \\frac{{?}}{{?}}. \\text{{ Fill in the sides.}}"
        solution = f"\\frac{{\\text{{{num}}}}}{{\\text{{{den}}}}}"

        steps = [
            f"\\text{{{mnemonic}}}",
            f"{func}(\\theta) = \\frac{{\\text{{{num}}}}}{{\\text{{{den}}}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Find trig ratio given triangle sides"""
        a, b, c = random.choice(self.triples)
        # a = opposite, b = adjacent, c = hypotenuse

        angle = random.choice(['A', 'B'])
        func = random.choice(['sin', 'cos', 'tan'])

        if angle == 'A':  # Angle opposite to side a
            if func == 'sin':
                num, den = a, c
            elif func == 'cos':
                num, den = b, c
            else:
                num, den = a, b
        else:  # Angle opposite to side b
            if func == 'sin':
                num, den = b, c
            elif func == 'cos':
                num, den = a, c
            else:
                num, den = b, a

        latex = f"\\text{{In right triangle with legs }} {a}, {b} \\text{{ and hypotenuse }} {c}, \\text{{ find }} \\{func}({angle})."
        solution = f"\\frac{{{num}}}{{{den}}}"

        steps = [
            f"\\text{{Identify sides relative to angle }} {angle}:",
            f"\\text{{Opposite = {a if angle == 'A' else b}, Adjacent = {b if angle == 'A' else a}, Hypotenuse = {c}}}",
            f"\\{func}({angle}) = \\frac{{{num}}}{{{den}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Use trig ratio to find a missing side"""
        a, b, c = random.choice(self.triples)

        # Scale the triple
        scale = random.randint(1, 3)
        a, b, c = a * scale, b * scale, c * scale

        problem_type = random.choice(['find_opp', 'find_adj', 'find_hyp'])

        if problem_type == 'find_opp':
            # Given angle A (where sin A = a/c), hypotenuse, find opposite
            latex = f"\\text{{In a right triangle, the hypotenuse is }} {c} \\text{{ and }} \\sin(A) = \\frac{{{a}}}{{{c}}}. \\text{{ Find the opposite side.}}"
            solution = str(a)

            steps = [
                f"\\sin(A) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}}",
                f"\\frac{{{a}}}{{{c}}} = \\frac{{x}}{{{c}}}",
                f"x = {a}"
            ]

        elif problem_type == 'find_adj':
            # Given angle and hypotenuse, find adjacent using cos
            latex = f"\\text{{In a right triangle, the hypotenuse is }} {c} \\text{{ and }} \\cos(A) = \\frac{{{b}}}{{{c}}}. \\text{{ Find the adjacent side.}}"
            solution = str(b)

            steps = [
                f"\\cos(A) = \\frac{{\\text{{adjacent}}}}{{\\text{{hypotenuse}}}}",
                f"\\frac{{{b}}}{{{c}}} = \\frac{{x}}{{{c}}}",
                f"x = {b}"
            ]

        else:
            # Given opposite and angle, find hypotenuse
            latex = f"\\text{{In a right triangle, the opposite side is }} {a} \\text{{ and }} \\sin(A) = \\frac{{{a}}}{{{c}}}. \\text{{ Find the hypotenuse.}}"
            solution = str(c)

            steps = [
                f"\\sin(A) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}}",
                f"\\frac{{{a}}}{{{c}}} = \\frac{{{a}}}{{x}}",
                f"x = {c}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Find all six trig ratios or apply to word problem"""
        problem_type = random.choice(['all_six', 'word_problem'])

        if problem_type == 'all_six':
            a, b, c = random.choice(self.triples)

            latex = f"\\text{{In a right triangle with legs }} {a}, {b} \\text{{ and hypotenuse }} {c}, \\text{{ find all 6 trig ratios for angle A (opposite to leg {a}).}}"
            solution = f"\\sin A = \\frac{{{a}}}{{{c}}}, \\cos A = \\frac{{{b}}}{{{c}}}, \\tan A = \\frac{{{a}}}{{{b}}}"

            steps = [
                f"\\text{{For angle A: opp = {a}, adj = {b}, hyp = {c}}}",
                f"\\sin A = \\frac{{\\text{{opp}}}}{{\\text{{hyp}}}} = \\frac{{{a}}}{{{c}}}",
                f"\\cos A = \\frac{{\\text{{adj}}}}{{\\text{{hyp}}}} = \\frac{{{b}}}{{{c}}}",
                f"\\tan A = \\frac{{\\text{{opp}}}}{{\\text{{adj}}}} = \\frac{{{a}}}{{{b}}}",
                f"\\csc A = \\frac{{{c}}}{{{a}}}, \\sec A = \\frac{{{c}}}{{{b}}}, \\cot A = \\frac{{{b}}}{{{a}}}"
            ]

        else:
            # Word problem
            height = random.randint(20, 100)
            a, b, c = 3, 4, 5
            scale = random.randint(5, 15)
            dist = b * scale

            latex = f"\\text{{From a point {dist} ft from a building, the angle of elevation to the top is such that }} \\tan(\\theta) = \\frac{{{a}}}{{{b}}}. \\text{{ How tall is the building?}}"
            answer = a * scale
            solution = f"{answer} \\text{{ ft}}"

            steps = [
                f"\\tan(\\theta) = \\frac{{\\text{{height}}}}{{\\text{{distance}}}}",
                f"\\frac{{{a}}}{{{b}}} = \\frac{{h}}{{{dist}}}",
                f"h = \\frac{{{a} \\times {dist}}}{{{b}}} = {answer} \\text{{ ft}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = TrigRatiosIntroGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
