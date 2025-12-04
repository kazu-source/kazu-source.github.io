import os

# This script will generate all remaining Calculus generators

base_path = r"c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\High_School\Calculus"

# Template for a basic generator
template = '''"""
{title} Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class {class_name}Generator:
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
{easy_content}

    def _generate_medium(self) -> Equation:
{medium_content}

    def _generate_hard(self) -> Equation:
{hard_content}

    def _generate_challenge(self) -> Equation:
{challenge_content}

def main():
    gen = {class_name}Generator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{{d.upper()}}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {{p.latex}}\n  Sol: {{p.solution}}\n")

if __name__ == '__main__': main()
'''

print("Script created successfully")
