"""
Test script for Systems of Equations Graphing with PDF generation.
Tests all 4 difficulty levels.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.chapter05.graphing_systems import GraphingSystemsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
gen = GraphingSystemsGenerator(seed=500)
pdf_gen = PDFWorksheetGenerator()

# Generate and save PDFs for each difficulty level
difficulties = ['easy', 'medium', 'hard', 'challenge']

for difficulty in difficulties:
    print(f"\nGenerating {difficulty.upper()} systems graphing worksheet...")
    problems = gen.generate_worksheet(difficulty, 4)

    print(f"  Generated {len(problems)} problems:")
    for i, prob in enumerate(problems, 1):
        print(f"    {i}. Equation 1: {prob.equation1_latex}")
        print(f"       Equation 2: {prob.equation2_latex}")
        print(f"       Solution: {prob.solution}")

    output_path = f"tests/systems_graphing_{difficulty}.pdf"
    pdf_gen.generate_worksheet(
        problems,
        output_path,
        title=f"Systems of Equations - Graphing ({difficulty.capitalize()})",
        include_answer_key=True
    )
    print(f"  [OK] Saved to: {output_path}")

print("\n" + "="*60)
print("All systems graphing PDFs generated successfully!")
print("="*60)
print("\nFiles created:")
for difficulty in difficulties:
    print(f"  - systems_graphing_{difficulty}.pdf")

print("\n" + "="*60)
print("FEATURES:")
print("="*60)
print("\nWorksheet Pages:")
print("  - Blank coordinate planes (2x2 grid)")
print("  - Equations shown at top of each graph")
print("  - Students graph both lines and find intersection")

print("\nAnswer Key Pages:")
print("  - Red line (first equation)")
print("  - Blue line (second equation)")
print("  - Green point at intersection (solution)")
print("  - Solution coordinates labeled")

print("\nDifficulty Levels:")
print("  EASY:      Integer slopes (±1, ±2), integer solutions")
print("  MEDIUM:    Fractional slopes, mixed forms")
print("  HARD:      Standard form, may have fractional solutions")
print("  CHALLENGE: Complex forms, fractional solutions")
print("="*60)
