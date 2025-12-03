"""
Test script for Why Square Roots Are Positive Generator
"""

import sys
sys.path.insert(0, '.')

from generators.High_School.Algebra.Unit_8.why_square_roots_are_positive_generator import WhySquareRootsArePositiveGenerator

def test_generator():
    gen = WhySquareRootsArePositiveGenerator()

    print("Testing Why Square Roots Are Positive Generator")
    print("=" * 80)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 80)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}")
            if problem.steps:
                print(f"   Steps:")
                for step in problem.steps:
                    print(f"      {step}")
            print()

if __name__ == "__main__":
    test_generator()
