"""
Test script to generate and display a compound inequality problem.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'generators/chapter03')))

from compound_inequalities_generator import CompoundInequalityGenerator

# Create generator
generator = CompoundInequalityGenerator(seed=42)

# Generate one problem of each type
print("=" * 60)
print("COMPOUND INEQUALITY TEST - GENERATING SAMPLE PROBLEMS")
print("=" * 60)

difficulties = ['easy', 'medium', 'hard', 'challenge']
types = ['and', 'or']

for difficulty in difficulties:
    print(f"\n{'='*60}")
    print(f"{difficulty.upper()} DIFFICULTY")
    print('='*60)

    for compound_type in types:
        print(f"\n{compound_type.upper()} Type:")
        print("-" * 40)

        prob = generator.generate_inequality(difficulty, compound_type)

        print(f"Problem (LaTeX): {prob.latex}")
        print(f"Compound Type: {prob.compound_type}")
        print(f"Boundary 1: {prob.boundary_1}")
        print(f"Boundary 2: {prob.boundary_2}")
        print(f"Inequality Type 1: {prob.inequality_type_1}")
        print(f"Inequality Type 2: {prob.inequality_type_2}")
        print(f"Number Line Range: [{prob.number_line_min}, {prob.number_line_max}]")
        print(f"\nSolution Steps:")
        for i, step in enumerate(prob.steps, 1):
            print(f"  {i}. {step}")

        # Save images
        if prob.worksheet_image:
            worksheet_filename = f"test_compound_{difficulty}_{compound_type}_worksheet.png"
            prob.worksheet_image.save(worksheet_filename)
            print(f"\n[OK] Worksheet image saved: {worksheet_filename}")

        if prob.answer_image:
            answer_filename = f"test_compound_{difficulty}_{compound_type}_answer.png"
            prob.answer_image.save(answer_filename)
            print(f"[OK] Answer image saved: {answer_filename}")

print("\n" + "=" * 60)
print("SAMPLE GENERATION COMPLETE!")
print("=" * 60)
print("\nGenerated 8 problems (4 difficulties × 2 types)")
print("Check the current directory for PNG images of number lines.")