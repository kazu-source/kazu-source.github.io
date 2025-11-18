"""
Test script for all problem types (linear equations and systems).
"""

from equation_generator import LinearEquationGenerator
from systems_generator import SystemsOfEquationsGenerator
from pdf_generator import PDFWorksheetGenerator


def test_all_problem_types():
    """Test both linear equations and systems of equations."""
    linear_gen = LinearEquationGenerator()
    systems_gen = SystemsOfEquationsGenerator()
    pdf_gen = PDFWorksheetGenerator()

    print("Math Worksheet Generator - Complete Test\n")
    print("=" * 60)

    # Test Linear Equations
    print("\n1. LINEAR EQUATIONS")
    print("-" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n  {difficulty.upper()} difficulty:")
        equations = linear_gen.generate_worksheet(difficulty, 10)

        # Show samples
        print(f"    Samples:")
        for i, eq in enumerate(equations[:2], 1):
            print(f"      {eq.latex} -> x = {eq.solution}")

        # Generate PDF
        output_file = f"tests/test_linear_{difficulty}.pdf"
        pdf_gen.generate_worksheet(
            equations,
            output_file,
            title=f"Linear Equations - {difficulty.capitalize()}",
            include_answer_key=True
        )
        print(f"    PDF: {output_file}")

    # Test Systems of Equations
    print("\n\n2. SYSTEMS OF EQUATIONS")
    print("-" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n  {difficulty.upper()} difficulty:")
        systems = systems_gen.generate_worksheet(difficulty, 8)

        # Show samples
        print(f"    Samples:")
        for i, sys in enumerate(systems[:2], 1):
            print(f"      {sys.equation1_latex}")
            print(f"      {sys.equation2_latex}")
            print(f"      Solution: {sys.solution}")

        # Generate PDF
        output_file = f"tests/test_systems_{difficulty}.pdf"
        pdf_gen.generate_worksheet(
            systems,
            output_file,
            title=f"Systems of Equations - {difficulty.capitalize()}",
            include_answer_key=True
        )
        print(f"    PDF: {output_file}")

    print("\n" + "=" * 60)
    print("TESTING COMPLETE!")
    print("\nGenerated PDFs:")
    print("\nLinear Equations:")
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"  - test_linear_{diff}.pdf")
    print("\nSystems of Equations:")
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"  - test_systems_{diff}.pdf")


if __name__ == "__main__":
    test_all_problem_types()
