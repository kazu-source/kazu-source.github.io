"""
Definitions of Similarity Generator
Creates problems about similarity definitions and basic concepts
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class DefinitionsOfSimilarityGenerator:
    """Generates problems about similarity definitions."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

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
        """Basic similarity concepts"""
        problem_type = random.choice(['definition', 'scale_factor', 'similar_or_not'])

        if problem_type == 'definition':
            latex = "\\text{{What does it mean for two figures to be similar?}}"
            solution = "Same shape, proportional sides, equal angles"
            steps = [
                "\\text{{Similar figures have:}}",
                "\\text{{1. The same shape}}",
                "\\text{{2. Corresponding angles are equal}}",
                "\\text{{3. Corresponding sides are proportional}}"
            ]

        elif problem_type == 'scale_factor':
            s1 = random.randint(4, 8)
            k = random.choice([2, 3, 4])
            s2 = s1 * k

            latex = f"\\text{{{{A figure with side }}}} {s1} \\text{{{{ is similar to a figure with corresponding side }}}} {s2}. "
            latex += "\\text{{What is the scale factor?}}"
            solution = f"{k}"
            steps = [
                f"\\text{{{{Scale factor}}}} = \\frac{{{{\\text{{{{new length}}}}}}}}{{{{\\text{{{{original length}}}}}}}}",
                f"= \\frac{{{s2}}}{{{s1}}} = {k}"
            ]

        else:  # similar_or_not
            angles1 = [60, 70, 50]
            angles2 = [60, 70, 50]

            latex = f"\\text{{{{Triangle A has angles }}}} {angles1[0]}^\\circ, {angles1[1]}^\\circ, {angles1[2]}^\\circ. "
            latex += f"\\text{{{{Triangle B has angles }}}} {angles2[0]}^\\circ, {angles2[1]}^\\circ, {angles2[2]}^\\circ. "
            latex += "\\text{{Are they similar?}}"
            solution = "Yes, all corresponding angles are equal"
            steps = [
                f"\\text{{{{Triangle A: }}}} {angles1[0]}^\\circ, {angles1[1]}^\\circ, {angles1[2]}^\\circ",
                f"\\text{{{{Triangle B: }}}} {angles2[0]}^\\circ, {angles2[1]}^\\circ, {angles2[2]}^\\circ",
                "\\text{{All corresponding angles are equal}}",
                "\\text{{Therefore, the triangles are similar (AA)}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Similarity with calculations"""
        problem_type = random.choice(['proportional_sides', 'find_length', 'aa_similarity'])

        if problem_type == 'proportional_sides':
            s1, s2, s3 = 3, 4, 5
            k = random.choice([2, 3])
            t1, t2, t3 = s1 * k, s2 * k, s3 * k

            latex = f"\\text{{{{Triangle ABC has sides }}}} {s1}, {s2}, {s3}. \\text{{{{ Triangle DEF has sides }}}} {t1}, {t2}, {t3}. "
            latex += "\\text{{Are they similar? If so, find the scale factor.}}"
            solution = f"Yes, scale factor = {k}"
            steps = [
                f"\\frac{{{t1}}}{{{s1}}} = {k}, \\quad \\frac{{{t2}}}{{{s2}}} = {k}, \\quad \\frac{{{t3}}}{{{s3}}} = {k}",
                "\\text{{All ratios are equal}}",
                f"\\text{{{{Therefore similar with scale factor }}}} {k}"
            ]

        elif problem_type == 'find_length':
            s1 = random.randint(5, 10)
            k = random.choice([2, 3, 4])
            s2 = s1 * k
            t1 = random.randint(6, 12)
            t2 = t1 * k

            latex = f"\\text{{{{Two similar triangles have scale factor }}}} {k}. \\text{{{{ If one side is }}}} {s1} \\text{{{{ in the smaller triangle, "
            latex += f"\\text{{{{what is the corresponding side in the larger triangle?}}}}}}"
            solution = f"{s2}"
            steps = [
                f"\\text{{{{Corresponding side}}}} = \\text{{{{original}}}} \\times \\text{{{{scale factor}}}}",
                f"= {s1} \\times {k} = {s2}"
            ]

        else:  # aa_similarity
            a1 = random.randint(50, 70)
            a2 = random.randint(60, 80)

            latex = f"\\text{{{{Two triangles each have angles of }}}} {a1}^\\circ \\text{{{{ and }}}} {a2}^\\circ. "
            latex += "\\text{{Are they similar? By what criterion?}}"
            solution = "Yes, by AA (Angle-Angle) similarity"
            steps = [
                f"\\text{{{{Both triangles have angles }}}} {a1}^\\circ \\text{{{{ and }}}} {a2}^\\circ",
                "\\text{{Two pairs of corresponding angles are equal}}",
                "\\text{{By AA similarity criterion, triangles are similar}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Advanced similarity problems"""
        problem_type = random.choice(['sss_similarity', 'sas_similarity', 'find_scale'])

        if problem_type == 'sss_similarity':
            s1, s2, s3 = 6, 8, 10
            k = 1.5
            t1, t2, t3 = s1 * k, s2 * k, s3 * k

            latex = f"\\text{{{{Triangle ABC has sides }}}} {s1}, {s2}, {s3}. \\text{{{{ Triangle DEF has sides }}}} {t1}, {t2}, {t3}. "
            latex += "\\text{{Prove they are similar using SSS similarity.}}"
            solution = "Yes, all ratios equal 1.5"
            steps = [
                f"\\frac{{{t1}}}{{{s1}}} = {t1/s1}",
                f"\\frac{{{t2}}}{{{s2}}} = {t2/s2}",
                f"\\frac{{{t3}}}{{{s3}}} = {t3/s3}",
                "\\text{{All three ratios are equal}}",
                "\\text{{By SSS similarity, triangles are similar}}"
            ]

        elif problem_type == 'sas_similarity':
            s1, s2 = 6, 9
            angle = random.randint(50, 80)
            k = 2
            t1, t2 = s1 * k, s2 * k

            latex = f"\\text{{{{Triangle ABC has sides AB = }}}} {s1}, \\text{{{{ AC = }}}} {s2} \\text{{{{ with }}}} \\angle A = {angle}^\\circ. "
            latex += f"\\text{{{{Triangle DEF has DE = }}}} {t1}, \\text{{{{ DF = }}}} {t2} \\text{{{{ with }}}} \\angle D = {angle}^\\circ. "
            latex += "\\text{{Are they similar?}}"
            solution = "Yes, by SAS similarity"
            steps = [
                f"\\frac{{{{DE}}}}{{{{AB}}}} = \\frac{{{t1}}}{{{s1}}} = {k}",
                f"\\frac{{{{DF}}}}{{{{AC}}}} = \\frac{{{t2}}}{{{s2}}} = {k}",
                f"\\angle D = \\angle A = {angle}^\\circ",
                "\\text{{Two sides proportional and included angle equal}}",
                "\\text{{By SAS similarity, triangles are similar}}"
            ]

        else:  # find_scale
            s1 = random.randint(8, 15)
            s2 = random.randint(12, 20)
            from math import gcd
            g = gcd(s2, s1)

            latex = f"\\text{{{{Two similar polygons have corresponding sides }}}} {s1} \\text{{{{ and }}}} {s2}. "
            latex += "\\text{{Express the scale factor as a fraction in lowest terms.}}"
            solution = f"{s2//g}/{s1//g}"
            steps = [
                f"\\text{{{{Scale factor}}}} = \\frac{{{s2}}}{{{s1}}}",
                f"= \\frac{{{s2//g}}}{{{s1//g}}} \\text{{{{ (simplified)}}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex similarity concepts"""
        problem_type = random.choice(['area_ratio', 'volume_ratio', 'similarity_theorem'])

        if problem_type == 'area_ratio':
            k = random.choice([2, 3, 4])
            area1 = random.randint(8, 20)
            area2 = area1 * k * k

            latex = f"\\text{{{{Two similar figures have scale factor }}}} {k}. \\text{{{{ If the smaller has area }}}} {area1}, "
            latex += "\\text{{what is the area of the larger?}}"
            solution = f"{area2}"
            steps = [
                f"\\text{{{{Area ratio}}}} = (\\text{{{{scale factor}}}})^2 = {k}^2 = {k*k}",
                f"\\text{{{{Larger area}}}} = {area1} \\times {k*k} = {area2}"
            ]

        elif problem_type == 'volume_ratio':
            k = random.choice([2, 3])
            vol1 = random.randint(10, 30)
            vol2 = vol1 * k * k * k

            latex = f"\\text{{{{Two similar solids have scale factor }}}} {k}. \\text{{{{ If the smaller has volume }}}} {vol1}, "
            latex += "\\text{{find the volume of the larger.}}"
            solution = f"{vol2}"
            steps = [
                f"\\text{{{{Volume ratio}}}} = (\\text{{{{scale factor}}}})^3 = {k}^3 = {k**3}",
                f"\\text{{{{Larger volume}}}} = {vol1} \\times {k**3} = {vol2}"
            ]

        else:  # similarity_theorem
            latex = "\\text{{State the Fundamental Theorem of Similarity.}}"
            solution = "If angles are equal and sides proportional, figures are similar"
            steps = [
                "\\text{{Two figures are similar if and only if:}}",
                "\\text{{1. Corresponding angles are congruent}}",
                "\\text{{2. Corresponding sides are proportional}}",
                "\\text{{This is the fundamental definition of similarity}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = DefinitionsOfSimilarityGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
