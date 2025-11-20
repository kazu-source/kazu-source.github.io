"""
Test script to verify answer key layout and column overflow for all problem types.
Generates worksheets with various problem counts to ensure proper formatting.
"""

import os
from equation_generator import LinearEquationGenerator
from systems_generator import SystemsOfEquationsGenerator
from inequalities_generator import InequalityGenerator
from generators.chapter03.compound_inequalities_generator import CompoundInequalityGenerator
from properties_generator import PropertiesOfEqualityGenerator
from pdf_generator import PDFWorksheetGenerator

# Create output directory
output_dir = "test_output_answer_keys"
os.makedirs(output_dir, exist_ok=True)

pdf_gen = PDFWorksheetGenerator()

print("=" * 80)
print("TESTING ANSWER KEY LAYOUTS")
print("=" * 80)

# Test configurations: (generator, name, test_counts)
test_configs = [
    # Linear equations (10 per page)
    (LinearEquationGenerator(), "Linear_Equations", [4, 8, 10, 12, 16]),

    # Systems (8 per page)
    (SystemsOfEquationsGenerator(), "Systems_of_Equations", [4, 8, 12, 16]),

    # Inequalities (8 per page)
    (InequalityGenerator(), "Inequalities", [4, 8, 12, 16]),

    # Compound Inequalities (8 per page)
    (CompoundInequalityGenerator(), "Compound_Inequalities_Mixed", [4, 8, 12, 16]),

    # Properties (10 per page)
    (PropertiesOfEqualityGenerator(), "Properties_of_Equality", [4, 8, 10, 12, 16]),
]

for generator, name, test_counts in test_configs:
    print(f"\n{'-' * 80}")
    print(f"Testing: {name}")
    print(f"{'-' * 80}")

    for count in test_counts:
        try:
            # Generate problems
            if "Compound" in name:
                problems = generator.generate_worksheet('medium', count)
            else:
                problems = generator.generate_worksheet('medium', count)

            # Generate PDF
            output_path = os.path.join(output_dir, f"{name}_{count}problems.pdf")
            pdf_gen.generate_worksheet(
                problems,
                output_path,
                title=f"{name} - Medium ({count} problems)",
                include_answer_key=True
            )

            print(f"  [OK] Generated {count} problems -> {output_path}")

        except Exception as e:
            print(f"  [ERROR] Failed to generate {count} problems: {str(e)}")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
print(f"\nAll test PDFs saved to: {os.path.abspath(output_dir)}")
print("\nPlease manually review the PDFs to verify:")
print("  1. Answer key columns don't overflow")
print("  2. Answers align properly in 2-column layout")
print("  3. Multi-page answer keys work correctly")
print("  4. Spacing is even and utilizes available space")
