"""
Test script to verify problem numbering on multi-page worksheets.
"""

import os
from generators.chapter04.graphing_points import GraphingPointsGenerator
from word_problems_generator import WordProblemsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create output directory
output_dir = "test_pagination"
os.makedirs(output_dir, exist_ok=True)

pdf_gen = PDFWorksheetGenerator()

print("=" * 80)
print("TESTING PAGINATION AND PROBLEM NUMBERING")
print("=" * 80)

# Test 1: Graphing Points with 8 problems (should be 2 pages: 1-4, 5-8)
print("\nTest 1: Graphing Points - 8 problems")
print("-" * 80)
graphing_gen = GraphingPointsGenerator()
problems = graphing_gen.generate_worksheet('medium', 8)

output_path = os.path.join(output_dir, "graphing_points_8problems.pdf")
pdf_gen.generate_worksheet(
    problems,
    output_path,
    title="Graphing Points - 8 Problems Test",
    include_answer_key=True
)
print(f"[OK] Generated: {output_path}")
print("Expected:")
print("  Worksheet Page 1: Problems 1-4")
print("  Worksheet Page 2: Problems 5-8")
print("  Answer Key Page 1: Problems 1-4")
print("  Answer Key Page 2: Problems 5-8")

# Test 2: Word Problems with 8 problems (should be 2 pages: 1-4, 5-8)
print("\nTest 2: Word Problems - 8 problems")
print("-" * 80)
word_gen = WordProblemsGenerator()
problems = word_gen.generate_worksheet('medium', 8, 'mixed')

output_path = os.path.join(output_dir, "word_problems_8problems.pdf")
pdf_gen.generate_worksheet(
    problems,
    output_path,
    title="Word Problems - 8 Problems Test",
    include_answer_key=True
)
print(f"[OK] Generated: {output_path}")
print("Expected:")
print("  Worksheet Page 1: Problems 1-4")
print("  Worksheet Page 2: Problems 5-8")
print("  Answer Key Page 1: Problems 1-4")
print("  Answer Key Page 2: Problems 5-8")

# Test 3: Graphing Points with 12 problems (should be 3 pages: 1-4, 5-8, 9-12)
print("\nTest 3: Graphing Points - 12 problems")
print("-" * 80)
problems = graphing_gen.generate_worksheet('medium', 12)

output_path = os.path.join(output_dir, "graphing_points_12problems.pdf")
pdf_gen.generate_worksheet(
    problems,
    output_path,
    title="Graphing Points - 12 Problems Test",
    include_answer_key=True
)
print(f"[OK] Generated: {output_path}")
print("Expected:")
print("  Worksheet Page 1: Problems 1-4")
print("  Worksheet Page 2: Problems 5-8")
print("  Worksheet Page 3: Problems 9-12")
print("  Answer Key Page 1: Problems 1-4")
print("  Answer Key Page 2: Problems 5-8")
print("  Answer Key Page 3: Problems 9-12")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
print(f"\nTest PDFs saved to: {os.path.abspath(output_dir)}")
print("\nPlease manually verify:")
print("  1. Problem numbers are sequential (1, 2, 3, 4 on page 1)")
print("  2. Page 2 starts at problem 5 (not 9)")
print("  3. Answer keys match worksheet numbering")
