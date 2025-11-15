"""
Test script for word problems worksheets.
"""

import os
from word_problems_generator import WordProblemsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create test_output directory if it doesn't exist
TEST_OUTPUT_DIR = "test_output"
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

def test_word_problems_worksheet():
    """Test word problems worksheet generation."""
    print("=" * 60)
    print("Testing Word Problems Worksheet")
    print("=" * 60)
    print()

    # Test mixed (addition and subtraction)
    print("1. Testing MIXED (addition and subtraction) - 8 problems...")
    generator = WordProblemsGenerator()
    problems = generator.generate_worksheet('medium', 8, 'mixed')

    pdf_gen = PDFWorksheetGenerator()
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_word_problems_mixed.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Word Problems - Addition & Subtraction",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 8 problems (mixed addition/subtraction)")
    print(f"  - Single column layout")
    print()

    # Test addition only
    print("2. Testing ADDITION only - 8 problems...")
    problems = generator.generate_worksheet('medium', 8, 'addition')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_word_problems_addition.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Word Problems - Addition",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 8 problems (addition only)")
    print()

    # Test subtraction only
    print("3. Testing SUBTRACTION only - 8 problems...")
    problems = generator.generate_worksheet('medium', 8, 'subtraction')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_word_problems_subtraction.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Word Problems - Subtraction",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 8 problems (subtraction only)")
    print()

    # Test different difficulty levels
    print("4. Testing EASY difficulty...")
    problems = generator.generate_worksheet('easy', 8, 'mixed')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_word_problems_easy.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Word Problems - Easy",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print()

    print("5. Testing HARD difficulty...")
    problems = generator.generate_worksheet('hard', 8, 'mixed')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_word_problems_hard.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Word Problems - Hard",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print()

    print("=" * 60)
    print("All word problems worksheet tests completed!")
    print("=" * 60)
    print()
    print("Check the following in the generated PDFs:")
    print("  1. Each problem shows: Word problem text, blanks for equation and solution")
    print("  2. Answer key shows equation and solution in RED")
    print("  3. Instructions are clear and centered")
    print("  4. Dynamic spacing works correctly")

if __name__ == "__main__":
    test_word_problems_worksheet()
