"""
Test worksheet demonstrating all advanced notation types from FORMATTING_STANDARDS.md
This generates a visual reference showing how each notation type renders in PDFs.
"""

from equation_generator import Equation
from pdf_generator import PDFWorksheetGenerator

def create_notation_examples():
    """Create example problems demonstrating each notation type (20 problems max for clean display)."""
    problems = []

    # ABSOLUTE VALUES
    problems.append(Equation(latex=r"\left|x + 3\right| = 7", solution=4, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\left|2x - 5\right| = 9", solution=7, steps=[], difficulty='demo'))

    # SQUARE ROOTS AND RADICALS
    problems.append(Equation(latex=r"\sqrt{16} = ?", solution=4, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\sqrt{2x + 5} = 5", solution=10, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\sqrt[3]{27} = ?", solution=3, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\sqrt[4]{16} = ?", solution=2, steps=[], difficulty='demo'))

    # LOGARITHMS
    problems.append(Equation(latex=r"\log(100) = ?", solution=2, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\ln(e^2) = ?", solution=2, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\log_{2}(8) = ?", solution=3, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\log_{3}(x) = 2", solution=9, steps=[], difficulty='demo'))

    # FACTORED FORMS
    problems.append(Equation(latex=r"(x + 2)(x - 3) = 0", solution=3, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"(x + 3)^2 = x^2 + 6x + ?", solution=9, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"3(2x + 5) = ?", solution=15, steps=[], difficulty='demo'))

    # POLYNOMIALS
    problems.append(Equation(latex=r"2x^2 + 5x - 3 = 0", solution=0.5, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"x^3 - 4x^2 + 5x = 0", solution=0, steps=[], difficulty='demo'))

    # RATIONAL EXPRESSIONS
    problems.append(Equation(latex=r"\frac{x + 3}{x - 2} = 0", solution=-3, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"\frac{2x + 1}{3x - 5} = ?", solution=0, steps=[], difficulty='demo'))

    # QUADRATIC FORMULA
    problems.append(Equation(latex=r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", solution=0, steps=[], difficulty='demo'))

    # INEQUALITIES
    problems.append(Equation(latex=r"2x + 3 \leq 11", solution=4, steps=[], difficulty='demo'))
    problems.append(Equation(latex=r"-3 < x \leq 5", solution=0, steps=[], difficulty='demo'))

    return problems


if __name__ == "__main__":
    print("=" * 70)
    print("ADVANCED NOTATION TEST WORKSHEET")
    print("=" * 70)
    print("\nGenerating examples of all advanced notation types...")
    print("Reference: FORMATTING_STANDARDS.md v1.1")

    # Create problems
    problems = create_notation_examples()

    print(f"\nGenerated {len(problems)} notation examples")
    print("\nSample problems:")
    for i, p in enumerate(problems[:5], 1):
        print(f"  {i}. {p.latex}")
    print(f"  ... and {len(problems) - 5} more")

    # Generate PDF
    pdf_gen = PDFWorksheetGenerator()
    output_path = "output/advanced_notation_reference.pdf"

    pdf_gen.generate_worksheet(
        problems,
        output_path,
        title='Advanced Notation Reference'
    )

    print(f"\n{'-' * 70}")
    print(f"PDF generated: {output_path}")
    print(f"{'-' * 70}")
    print("\nThis worksheet demonstrates:")
    print("  - Absolute values (\\left|...\\right|)")
    print("  - Square roots and nth roots (\\sqrt{}, \\sqrt[n]{})")
    print("  - Logarithms (\\log, \\ln, \\log_{})")
    print("  - Factored forms and parentheses")
    print("  - Polynomials (standard descending form)")
    print("  - Rational expressions (\\frac{}{})")
    print("  - Quadratic formula")
    print("  - Inequality symbols (\\leq, \\geq)")
    print("\n" + "=" * 70)
    print("Opening in browser...")
    print("=" * 70)
