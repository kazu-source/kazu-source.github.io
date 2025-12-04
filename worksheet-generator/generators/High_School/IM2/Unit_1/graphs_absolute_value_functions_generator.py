"""
Graphs of Absolute Value Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphsAbsoluteValueFunctionsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        problem_type = random.choice(['vertex_form', 'find_vertex'])

        if problem_type == 'vertex_form':
            h = random.randint(-5, 5)
            k = random.randint(-5, 5)
            latex = f"\\text{{What is the vertex of }} f(x) = |x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}?"
            solution = f"({h}, {k})"
            steps = [
                f"The absolute value function is in the form f(x) = |x - h| + k",
                f"where (h, k) is the vertex",
                f"f(x) = |x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}",
                f"h = {h}, k = {k}",
                f"Vertex: ({h}, {k})"
            ]
        else:  # find_vertex
            a = random.choice([1, -1])
            h = random.randint(-4, 4)
            k = random.randint(-4, 4)
            latex = f"\\text{{Find the vertex of }} f(x) = {'' if a == 1 else '-'}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}"
            solution = f"({h}, {k})"
            steps = [
                f"Absolute value function: f(x) = {'' if a == 1 else '-'}|x - h| + k",
                f"The vertex is at (h, k)",
                f"From f(x) = {'' if a == 1 else '-'}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}",
                f"h = {h}, k = {k}",
                f"Vertex: ({h}, {k})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['with_coefficient', 'find_intercepts'])

        if problem_type == 'with_coefficient':
            a = random.choice([2, 3, -2, -3, 0.5, -0.5])
            h = random.randint(-4, 4)
            k = random.randint(-4, 4)
            latex = f"\\text{{Graph }} f(x) = {a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)} \\text{{ and identify the vertex}}"
            solution = f"Vertex: ({h}, {k}), {'opens up' if a > 0 else 'opens down'}, vertical stretch by factor {abs(a)}"
            steps = [
                f"Standard form: f(x) = a|x - h| + k",
                f"a = {a}, h = {h}, k = {k}",
                f"Vertex: ({h}, {k})",
                f"Since a = {a} {'> 0' if a > 0 else '< 0'}, the graph opens {'up' if a > 0 else 'down'}",
                f"|a| = {abs(a)} means vertical stretch by factor {abs(a)}",
                f"Vertex: ({h}, {k}), {'opens up' if a > 0 else 'opens down'}"
            ]
        else:  # find_intercepts
            h = random.randint(-3, 3)
            k = random.randint(-3, 3)
            y_int = abs(h) + k
            latex = f"\\text{{Find the y-intercept of }} f(x) = |x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}"
            solution = f"(0, {y_int})"
            steps = [
                f"To find y-intercept, substitute x = 0",
                f"f(0) = |0 {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}",
                f"f(0) = |{-h if h < 0 else h}| {'+' if k >= 0 else '-'} {abs(k)}",
                f"f(0) = {abs(h)} {'+' if k >= 0 else '-'} {abs(k)}",
                f"f(0) = {y_int}",
                f"Y-intercept: (0, {y_int})"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['transformations', 'domain_range'])

        if problem_type == 'transformations':
            a = random.choice([2, 3, -2, -3, 0.5, -0.5, 1.5])
            h = random.randint(-5, 5)
            k = random.randint(-5, 5)
            latex = f"\\text{{Describe all transformations of }} f(x) = {a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)} \\text{{ from }} g(x) = |x|"

            transformations = []
            if h != 0:
                transformations.append(f"horizontal shift {'right' if h > 0 else 'left'} by {abs(h)}")
            if k != 0:
                transformations.append(f"vertical shift {'up' if k > 0 else 'down'} by {abs(k)}")
            if abs(a) != 1:
                transformations.append(f"vertical {'stretch' if abs(a) > 1 else 'compression'} by factor {abs(a)}")
            if a < 0:
                transformations.append("reflection over x-axis")

            solution = "; ".join(transformations)
            steps = [
                f"Compare f(x) = {a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)} to g(x) = |x|",
                f"Standard form: f(x) = a|x - h| + k",
                f"a = {a}, h = {h}, k = {k}"
            ]
            steps.extend([f"• {t}" for t in transformations])
        else:  # domain_range
            a = random.choice([1, 2, -1, -2])
            h = random.randint(-4, 4)
            k = random.randint(-4, 4)
            latex = f"\\text{{Find the domain and range of }} f(x) = {'' if a == 1 else a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}"

            if a > 0:
                range_str = f"[{k}, \\infty)"
            else:
                range_str = f"(-\\infty, {k}]"

            solution = f"Domain: (-\\infty, \\infty), Range: {range_str}"
            steps = [
                f"Vertex: ({h}, {k})",
                f"a = {a}, so graph opens {'up' if a > 0 else 'down'}",
                "Domain: All real numbers = (-\\infty, \\infty)",
                f"Since vertex is at ({h}, {k}) and opens {'up' if a > 0 else 'down'}:",
                f"Range: {range_str}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        problem_type = random.choice(['write_equation', 'complex_transformations'])

        if problem_type == 'write_equation':
            h = random.randint(-5, 5)
            k = random.randint(-5, 5)
            a = random.choice([2, 3, -2, -3, 0.5, -0.5])

            # Give a point on the graph
            x_point = h + random.choice([1, 2, -1, -2])
            y_point = a * abs(x_point - h) + k

            latex = f"\\text{{Write an equation for an absolute value function with vertex }} ({h}, {k}) \\text{{ passing through }} ({x_point}, {y_point})"
            solution = f"f(x) = {a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}"
            steps = [
                f"Start with vertex form: f(x) = a|x - h| + k",
                f"Vertex: ({h}, {k}), so f(x) = a|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}",
                f"Use point ({x_point}, {y_point}) to find a:",
                f"{y_point} = a|{x_point} {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}",
                f"{y_point} = a|{x_point - h}| {'+' if k >= 0 else '-'} {abs(k)}",
                f"{y_point} = a({abs(x_point - h)}) {'+' if k >= 0 else '-'} {abs(k)}",
                f"{y_point - k} = {abs(x_point - h)}a",
                f"a = {a}",
                f"f(x) = {a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}"
            ]
        else:  # complex_transformations
            a = random.choice([2, -2, 3, -3, 0.5, -0.5])
            h = random.randint(-6, 6)
            k = random.randint(-6, 6)
            latex = f"\\text{{Find the vertex, axis of symmetry, domain, and range of }} f(x) = {a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}"

            if a > 0:
                range_str = f"[{k}, \\infty)"
            else:
                range_str = f"(-\\infty, {k}]"

            solution = f"Vertex: ({h}, {k}), Axis: x = {h}, Domain: (-\\infty, \\infty), Range: {range_str}"
            steps = [
                f"Standard form: f(x) = a|x - h| + k",
                f"From f(x) = {a}|x {'-' if h < 0 else '+'} {abs(h)}| {'+' if k >= 0 else '-'} {abs(k)}:",
                f"a = {a}, h = {h}, k = {k}",
                f"Vertex: ({h}, {k})",
                f"Axis of symmetry: x = {h}",
                "Domain: (-\\infty, \\infty)",
                f"Since a = {a} {'> 0' if a > 0 else '< 0'}, opens {'up' if a > 0 else 'down'}",
                f"Range: {range_str}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphsAbsoluteValueFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
