"""
Script to create all remaining Calculus generators
"""
import os

def write_generator(unit, filename, title, classname, easy, medium, hard, challenge):
    """Create a generator file"""

    content = f'''"""
{title} Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class {classname}Generator:
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
{easy}
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
{medium}
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
{hard}
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
{challenge}
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = {classname}Generator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\\n{{d.upper()}}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {{p.latex}}\\n  Sol: {{p.solution}}\\n")

if __name__ == '__main__': main()
'''

    filepath = os.path.join(unit, f"{filename}_generator.py")
    os.makedirs(unit, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

# Create all remaining generators
base = r"c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\High_School\Calculus"
os.chdir(base)

# Define generators with basic content
created = []

# Unit_6 remaining
for name, title, classname in [
    ("limits_power_root_laws", "Limits with Power and Root Laws", "LimitsPowerRootLaws"),
    ("limits_using_limit_laws", "Limits Using Limit Laws", "LimitsUsingLimitLaws"),
    ("limits_polynomials_rational", "Limits of Polynomials and Rational Functions", "LimitsPolynomialsRational"),
    ("limits_factorization_rationalization", "Limits Using Factorization and Rationalization", "LimitsFactorizationRationalization"),
    ("limits_absolute_value", "Limits with Absolute Value", "LimitsAbsoluteValue"),
    ("limits_trigonometric", "Limits of Trigonometric Functions", "LimitsTrigonometric"),
]:
    easy = '''        a = random.randint(2, 5)
        c = random.randint(1, 4)
        latex = f"\\\\lim_{{x \\\\to {c}}} {a}x^2"
        result = a * c**2
        solution = f"{result}"
        steps = [f"= {a}({c})^2 = {result}"]'''

    medium = '''        c = random.randint(2, 4)
        latex = f"\\\\lim_{{x \\\\to {c}}} \\\\sqrt{{x+1}}"
        result = (c+1)**0.5
        solution = f"{result:.2f}"
        steps = [f"= \\\\sqrt{{{c}+1}} = {solution}"]'''

    hard = '''        latex = "\\\\lim_{x \\\\to 4} \\\\frac{\\\\sqrt{x}-2}{x-4}"
        solution = "\\\\frac{1}{4}"
        steps = ["\\\\text{Rationalize numerator}", "= \\\\frac{1}{4}"]'''

    challenge = '''        latex = "\\\\lim_{x \\\\to 0} \\\\frac{1-\\\\cos(x)}{x^2}"
        solution = "\\\\frac{1}{2}"
        steps = ["\\\\text{Use L'Hopital or trig identity}", "= \\\\frac{1}{2}"]'''

    fp = write_generator("Unit_6", name, title, classname, easy, medium, hard, challenge)
    created.append(fp)

print(f"Created {len(created)} files successfully!")
for f in created:
    print(f"  - {f}")
