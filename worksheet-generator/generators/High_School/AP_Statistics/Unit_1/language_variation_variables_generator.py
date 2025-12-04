"""
Language of Variation and Variables Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LanguageVariationVariablesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

        self.scenarios = [
            ("Students in a class", ["age", "grade level", "favorite subject", "hours studied per week", "GPA"]),
            ("Cars in a parking lot", ["color", "make", "model year", "number of doors", "miles per gallon"]),
            ("Houses on a street", ["number of bedrooms", "square footage", "price", "paint color", "year built"]),
            ("Trees in a forest", ["species", "height", "diameter", "age", "number of branches"]),
            ("Athletes on a team", ["jersey number", "position", "height", "weight", "years of experience"])
        ]

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        subject, variables = random.choice(self.scenarios)
        var = random.choice(variables)

        question = f"\\text{{Identify whether ''{var}'' for {subject} is categorical or quantitative.}}"

        quantitative_keywords = ["age", "year", "hours", "GPA", "bedrooms", "footage", "price", "height",
                                "diameter", "number", "weight", "experience", "miles"]
        is_quantitative = any(keyword in var.lower() for keyword in quantitative_keywords)

        solution = "Quantitative" if is_quantitative else "Categorical"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        subject, variables = random.choice(self.scenarios)
        var = random.choice(variables)

        question = f"\\text{{For the variable ''{var}'' measured on {subject}, classify it as:}}\\\\"\
                   f"\\text{{(a) Categorical or Quantitative}}\\\\"\
                   f"\\text{{(b) If quantitative, is it discrete or continuous?}}"

        quantitative_keywords = ["age", "year", "hours", "GPA", "bedrooms", "footage", "price", "height",
                                "diameter", "number", "weight", "experience", "miles"]
        is_quantitative = any(keyword in var.lower() for keyword in quantitative_keywords)

        if is_quantitative:
            continuous_keywords = ["footage", "price", "height", "diameter", "weight", "miles", "GPA"]
            is_continuous = any(keyword in var.lower() for keyword in continuous_keywords)
            solution = f"(a) Quantitative, (b) {'Continuous' if is_continuous else 'Discrete'}"
        else:
            solution = "(a) Categorical, (b) Not applicable"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        subject, variables = random.choice(self.scenarios)
        selected_vars = random.sample(variables, 3)

        question = f"\\text{{For {subject}, classify each variable:}}\\\\"\
                   f"\\text{{1. {selected_vars[0]}}}\\\\"\
                   f"\\text{{2. {selected_vars[1]}}}\\\\"\
                   f"\\text{{3. {selected_vars[2]}}}\\\\"\
                   f"\\text{{as (a) Categorical or Quantitative, (b) If quantitative: discrete or continuous}}"

        solutions = []
        quantitative_keywords = ["age", "year", "hours", "GPA", "bedrooms", "footage", "price", "height",
                                "diameter", "number", "weight", "experience", "miles"]
        continuous_keywords = ["footage", "price", "height", "diameter", "weight", "miles", "GPA"]

        for var in selected_vars:
            is_quantitative = any(keyword in var.lower() for keyword in quantitative_keywords)
            if is_quantitative:
                is_continuous = any(keyword in var.lower() for keyword in continuous_keywords)
                solutions.append(f"Quantitative, {'Continuous' if is_continuous else 'Discrete'}")
            else:
                solutions.append("Categorical")

        solution = f"1. {solutions[0]}, 2. {solutions[1]}, 3. {solutions[2]}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        subject = "a research study on college students"

        question = f"\\text{{A researcher collects the following data on college students:}}\\\\"\
                   f"\\text{{- Student ID number}}\\\\"\
                   f"\\text{{- Class standing (Freshman, Sophomore, Junior, Senior)}}\\\\"\
                   f"\\text{{- Credit hours completed}}\\\\"\
                   f"\\text{{- Current GPA}}\\\\"\
                   f"\\text{{Classify each variable and explain why Student ID is coded numerically}}\\\\"\
                   f"\\text{{but is not considered quantitative.}}"

        solution = "Student ID: Categorical (numeric label, no mathematical meaning); "\
                   "Class standing: Categorical (ordinal); "\
                   "Credit hours: Quantitative discrete; "\
                   "GPA: Quantitative continuous. "\
                   "Student ID uses numbers as labels, not for calculations."

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = LanguageVariationVariablesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
