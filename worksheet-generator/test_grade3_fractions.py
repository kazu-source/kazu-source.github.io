"""
Test script for all Grade 3 Fractions generators (Units 5-6)
"""

import sys
import os

# Add the worksheet-generator directory to the path
sys.path.insert(0, os.path.dirname(__file__))

from generators.K_8.Grade_3.Unit05.fractions_intro_generator import FractionsIntroGenerator
from generators.K_8.Grade_3.Unit05.fractions_in_contexts_generator import FractionsInContextsGenerator
from generators.K_8.Grade_3.Unit05.fractions_and_whole_numbers_generator import FractionsAndWholeNumbersGenerator
from generators.K_8.Grade_3.Unit06.comparing_fractions_generator import ComparingFractionsGenerator
from generators.K_8.Grade_3.Unit06.comparing_fractions_of_different_wholes_generator import ComparingFractionsOfDifferentWholesGenerator
from generators.K_8.Grade_3.Unit06.equivalent_fractions_generator import EquivalentFractionsGenerator


def test_generator(name, generator_class):
    """Test a single generator across all difficulty levels."""
    print(f"\n{'='*70}")
    print(f"Testing: {name}")
    print('='*70)

    generator = generator_class()

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()}:")
        problems = generator.generate_worksheet(difficulty, 2)

        for i, problem in enumerate(problems, 1):
            print(f"  Problem {i}:")
            # Truncate long latex strings
            latex_display = problem.latex if len(problem.latex) <= 80 else problem.latex[:77] + "..."
            print(f"    Q: {latex_display}")

            # Truncate long solutions
            solution_display = str(problem.solution) if len(str(problem.solution)) <= 60 else str(problem.solution)[:57] + "..."
            print(f"    A: {solution_display}")


def main():
    """Run all tests."""
    print("="*70)
    print("GRADE 3 FRACTIONS GENERATORS TEST SUITE")
    print("Units 5-6: Introduction, Contexts, and Comparisons")
    print("="*70)

    generators = [
        ("Unit 5.1: Fractions Introduction", FractionsIntroGenerator),
        ("Unit 5.2: Fractions in Contexts", FractionsInContextsGenerator),
        ("Unit 5.3: Fractions and Whole Numbers", FractionsAndWholeNumbersGenerator),
        ("Unit 6.1: Comparing Fractions (Same Denominator)", ComparingFractionsGenerator),
        ("Unit 6.2: Comparing Fractions of Different Wholes", ComparingFractionsOfDifferentWholesGenerator),
        ("Unit 6.3: Equivalent Fractions", EquivalentFractionsGenerator),
    ]

    for name, generator_class in generators:
        try:
            test_generator(name, generator_class)
            print(f"\n[PASS] {name}")
        except Exception as e:
            print(f"\n[FAIL] {name}: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "="*70)
    print("ALL TESTS COMPLETED")
    print("="*70)


if __name__ == '__main__':
    main()
