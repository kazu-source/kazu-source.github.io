"""
Test script for multi-step equations worksheets.
"""

import os
from multistep_generator import MultiStepEquationGenerator
from pdf_generator import PDFWorksheetGenerator

# Create test_output directory if it doesn't exist
TEST_OUTPUT_DIR = "test_output"
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

def test_multistep_equations_worksheet():
    """Test multi-step equations worksheet generation."""
    print("=" * 60)
    print("Testing Multi-Step Equations Worksheet")
    print("=" * 60)
    print()

    # Test with 10 problems (2 columns x 5 rows)
    print("1. Testing MEDIUM difficulty - 10 problems...")
    generator = MultiStepEquationGenerator()
    problems = generator.generate_worksheet('medium', 10)

    pdf_gen = PDFWorksheetGenerator()
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_multistep_medium.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Multi-Step Equations - Medium",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (two-step equations)")
    print(f"  - 2 columns x 5 rows layout")
    print()

    # Test EASY difficulty
    print("2. Testing EASY difficulty - 10 problems...")
    problems = generator.generate_worksheet('easy', 10)
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_multistep_easy.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Multi-Step Equations - Easy",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (easy level)")
    print()

    # Test HARD difficulty
    print("3. Testing HARD difficulty - 10 problems...")
    problems = generator.generate_worksheet('hard', 10)
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_multistep_hard.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Multi-Step Equations - Hard",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (hard level)")
    print()

    print("=" * 60)
    print("All multi-step equations worksheet tests completed!")
    print("=" * 60)
    print()
    print("Check the following in the generated PDFs:")
    print("  1. Each problem shows a two-step equation (ax + b = c or x/a + b = c)")
    print("  2. Answer key shows the solution in RED")
    print("  3. Layout is 2 columns x 5 rows")
    print("  4. Instructions say 'Solve each two-step equation. Show your work.'")
    print("  5. Dynamic spacing works correctly")

if __name__ == "__main__":
    test_multistep_equations_worksheet()
