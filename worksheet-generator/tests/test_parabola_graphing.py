"""
Test script for Parabola Graphing with PDF generation.
Tests all 4 difficulty levels.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.chapter11.graphing_parabolas import ParabolaGraphingGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
gen = ParabolaGraphingGenerator(seed=1100)
pdf_gen = PDFWorksheetGenerator()

# Generate and save PDFs for each difficulty level
difficulties = ['easy', 'medium', 'hard', 'challenge']

for difficulty in difficulties:
    print(f"\nGenerating {difficulty.upper()} parabola graphing worksheet...")
    problems = gen.generate_worksheet(difficulty, 4)

    print(f"  Generated {len(problems)} problems:")
    for i, prob in enumerate(problems, 1):
        print(f"    {i}. Equation: {prob.equation_latex}")
        print(f"       Vertex: {prob.vertex}")
        print(f"       Opens: {'upward' if prob.opens_upward else 'downward'}")
        print(f"       a = {prob.a}")

    output_path = f"tests/parabola_graphing_{difficulty}.pdf"
    pdf_gen.generate_worksheet(
        problems,
        output_path,
        title=f"Graphing Parabolas ({difficulty.capitalize()})",
        include_answer_key=True
    )
    print(f"  [OK] Saved to: {output_path}")

print("\n" + "="*60)
print("All parabola graphing PDFs generated successfully!")
print("="*60)
print("\nFiles created:")
for difficulty in difficulties:
    print(f"  - parabola_graphing_{difficulty}.pdf")

print("\n" + "="*60)
print("FEATURES:")
print("="*60)
print("\nWorksheet Pages:")
print("  - Blank coordinate planes (2x2 grid)")
print("  - Equation shown at top of each graph")
print("  - Students graph the parabola and identify vertex")

print("\nAnswer Key Pages:")
print("  - Purple parabola curve")
print("  - Vertex plotted and labeled")
print("  - Equation displayed at top")

print("\nDifficulty Levels:")
print("  EASY:      y = x² or y = -x² (vertex at origin)")
print("  MEDIUM:    y = (x - h)² + k (integer h, k)")
print("  HARD:      y = a(x - h)² + k (a ≠ 1, stretch/compress)")
print("  CHALLENGE: Fractional a, h, or k values")
print("="*60)
