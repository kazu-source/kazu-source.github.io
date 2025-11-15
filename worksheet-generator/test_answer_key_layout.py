"""
Test script to verify answer key layouts match worksheet layouts for all problem types.
"""

import os
from equation_generator import LinearEquationGenerator
from systems_generator import SystemsOfEquationsGenerator
from inequalities_generator import InequalityGenerator
from pdf_generator import PDFWorksheetGenerator

# Create test_output directory if it doesn't exist
TEST_OUTPUT_DIR = "test_output"
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

def test_linear_equations():
    """Test linear equations with 10 problems."""
    print("Testing Linear Equations (10 problems)...")
    generator = LinearEquationGenerator()
    equations = generator.generate_worksheet('medium', 10)

    pdf_gen = PDFWorksheetGenerator()
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_linear_answer_key.pdf")
    pdf_gen.generate_worksheet(equations, output_file,
                               title="Linear Equations Test",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - Worksheet: 3 columns x 5 rows layout")
    print(f"  - Answer Key: Should match worksheet layout with RED answers\n")

def test_systems():
    """Test systems of equations with 8 problems."""
    print("Testing Systems of Equations (8 problems)...")
    generator = SystemsOfEquationsGenerator()
    systems = generator.generate_worksheet('medium', 8)

    pdf_gen = PDFWorksheetGenerator()
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_systems_answer_key.pdf")
    pdf_gen.generate_worksheet(systems, output_file,
                               title="Systems of Equations Test",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - Worksheet: 2 columns x 4 rows layout")
    print(f"  - Answer Key: Should match worksheet layout with RED answers\n")

def test_inequalities():
    """Test inequalities with 8 problems."""
    print("Testing Inequalities (8 problems)...")
    generator = InequalityGenerator()
    inequalities = generator.generate_worksheet('medium', 8)

    pdf_gen = PDFWorksheetGenerator()
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_inequality_answer_key.pdf")
    pdf_gen.generate_worksheet(inequalities, output_file,
                               title="Inequalities Test",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - Worksheet: 2 columns x 4 rows layout with blank number lines")
    print(f"  - Answer Key: Should match worksheet layout with solved number lines and RED algebraic solutions\n")

def test_edge_cases():
    """Test edge cases with different problem counts."""
    print("Testing Edge Cases...")

    # Linear equations with 15 problems (max)
    print("  - Linear equations with 15 problems (max)...")
    generator = LinearEquationGenerator()
    equations = generator.generate_worksheet('medium', 15)
    pdf_gen = PDFWorksheetGenerator()
    pdf_gen.generate_worksheet(equations, os.path.join(TEST_OUTPUT_DIR, "test_linear_15.pdf"),
                               title="Linear Equations - 15 Problems",
                               include_answer_key=True)

    # Linear equations with 3 problems (minimal)
    print("  - Linear equations with 3 problems (minimal)...")
    equations = generator.generate_worksheet('medium', 3)
    pdf_gen.generate_worksheet(equations, os.path.join(TEST_OUTPUT_DIR, "test_linear_3.pdf"),
                               title="Linear Equations - 3 Problems",
                               include_answer_key=True)

    print("  [OK] Edge case tests completed\n")

if __name__ == "__main__":
    print("=" * 60)
    print("Answer Key Layout Test Suite")
    print("=" * 60)
    print()

    test_linear_equations()
    test_systems()
    test_inequalities()
    test_edge_cases()

    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)
    print()
    print("Please verify:")
    print("  1. Answer keys match worksheet layouts (same column/row structure)")
    print("  2. All answers are displayed in RED color")
    print("  3. Dynamic spacing works correctly")
    print("  4. Headers, footers, and logos are consistent")
