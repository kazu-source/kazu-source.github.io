"""Statistical Questions Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class StatisticalQuestionsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        latex = f"\\text{{Is this statistical: 'How tall is the tallest student?'}}"
        return Equation(latex=latex, solution="No", steps=["Not statistical - one answer"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        latex = f"\\text{{Is this statistical: 'How tall are students in 6th grade?'}}"
        return Equation(latex=latex, solution="Yes", steps=["Statistical - expects variability"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        questions = [
            ("What is the capital of France?", "No"),
            ("What are the favorite colors of students?", "Yes"),
            ("How many days in a week?", "No"),
            ("What are the test scores in class?", "Yes")
        ]
        q, ans = random.choice(questions)
        latex = f"\\text{{Is this a statistical question: '{q}'}}"
        return Equation(latex=latex, solution=ans, steps=[f"{ans} - {'expects variability' if ans=='Yes' else 'single answer'}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{Write a statistical question about student ages.}}"
        return Equation(latex=latex, solution="What are the ages of students in our school?", steps=["Expects variability in ages"], difficulty='challenge')

def main():
    gen = StatisticalQuestionsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
