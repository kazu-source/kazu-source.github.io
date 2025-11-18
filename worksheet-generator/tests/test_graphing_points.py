"""
Test script for Graphing Points with PDF generation.
Tests all 4 difficulty levels.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.chapter04.graphing_points import GraphingPointsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
gen = GraphingPointsGenerator(seed=400)
pdf_gen = PDFWorksheetGenerator()

# Generate and save PDFs for each difficulty level
difficulties = ['easy', 'medium', 'hard', 'challenge']

for difficulty in difficulties:
    print(f"\nGenerating {difficulty.upper()} graphing points worksheet...")
    problems = gen.generate_worksheet(difficulty, 4)

    print(f"  Generated {len(problems)} problems:")
    for i, prob in enumerate(problems, 1):
        print(f"    {i}. Points: {prob.points}")
        print(f"       Labels: {prob.labels}")
        print(f"       Bounds: x({prob.x_min},{prob.x_max}), y({prob.y_min},{prob.y_max})")

    output_path = f"tests/graphing_points_{difficulty}.pdf"
    pdf_gen.generate_worksheet(
        problems,
        output_path,
        title=f"Graphing Points ({difficulty.capitalize()})",
        include_answer_key=True
    )
    print(f"  [OK] Saved to: {output_path}")

print("\n" + "="*60)
print("All graphing points PDFs generated successfully!")
print("="*60)
print("\nFiles created:")
for difficulty in difficulties:
    print(f"  - graphing_points_{difficulty}.pdf")

print("\n" + "="*60)
print("FEATURES:")
print("="*60)
print("\nWorksheet Pages:")
print("  - Blank coordinate planes")
print("  - Point labels and coordinates shown at top")
print("  - Students plot the points on the grid")

print("\nAnswer Key Pages:")
print("  - Points plotted with labels")
print("  - Color-coded for visibility")

print("\nDifficulty Levels:")
print("  EASY:      3 points in first quadrant (0-10)")
print("  MEDIUM:    4 points in all quadrants (-5 to 5)")
print("  HARD:      5 points across all quadrants (-10 to 10)")
print("  CHALLENGE: 6 points including points on axes")
print("="*60)
