"""
Generate all challenge-level worksheets for testing.
Saves to output/test/ directory.
"""

import sys
import os
from pdf_generator import PDFWorksheetGenerator

# Chapter 1 Generators
from generators.chapter01.combining_like_terms_generator import CombiningLikeTermsGenerator
from generators.chapter01.evaluating_expressions_generator import EvaluatingExpressionsGenerator
from generators.chapter01.exponents_generator import ExponentsGenerator
from generators.chapter01.substitution_generator import SubstitutionGenerator
from generators.chapter01.variables_generator import VariablesGenerator

# Chapter 2 Generators
from generators.chapter02.equations_intro_generator import EquationsIntroGenerator
from generators.chapter02.inputs_outputs_generator import InputsOutputsGenerator
from generators.chapter02.solutions_generator import SolutionsGenerator
from generators.chapter02.variables_both_sides_generator import VariablesBothSidesGenerator

# Chapter 3 Generators
from generators.chapter03.compound_inequalities_generator import CompoundInequalityGenerator

def generate_all_challenge_worksheets():
    """Generate challenge worksheets for all generators."""

    pdf_gen = PDFWorksheetGenerator()

    generators = [
        # Chapter 1 - (generator, filename, title)
        (CombiningLikeTermsGenerator(), "ch01_combining_like_terms", "Combining Like Terms"),
        (EvaluatingExpressionsGenerator(), "ch01_evaluating_expressions", "Evaluating Expressions"),
        (ExponentsGenerator(), "ch01_exponents", "Exponents"),
        (SubstitutionGenerator(), "ch01_substitution", "Substitution"),
        (VariablesGenerator(), "ch01_variables", "Variables"),

        # Chapter 2
        (EquationsIntroGenerator(), "ch02_equations_intro", "Introduction to Equations"),
        (InputsOutputsGenerator(), "ch02_inputs_outputs", "Inputs and Outputs"),
        (SolutionsGenerator(), "ch02_solutions", "Solutions to Equations"),
        (VariablesBothSidesGenerator(), "ch02_variables_both_sides", "Variables on Both Sides"),

        # Chapter 3
        (CompoundInequalityGenerator(), "ch03_compound_inequalities", "Compound Inequalities"),
    ]

    print("=" * 70)
    print("GENERATING ALL CHALLENGE WORKSHEETS")
    print("=" * 70)
    print(f"\nTotal generators: {len(generators)}")
    print("Difficulty: CHALLENGE")
    print("Problems per worksheet: 16")
    print("\n" + "-" * 70)

    generated_files = []

    for i, (generator, filename, topic_title) in enumerate(generators, 1):
        print(f"\n[{i}/{len(generators)}] {filename}...")

        try:
            # Generate problems
            problems = generator.generate_worksheet('challenge', 16)

            # Create output path
            output_path = f"output/test/{filename}_challenge.pdf"

            # Generate PDF with format: "Topic - Difficulty"
            title = f"{topic_title} - Challenge"
            pdf_gen.generate_worksheet(problems, output_path, title=title)

            generated_files.append(output_path)
            print(f"  [OK] Generated: {output_path}")
            print(f"       Title: {title}")

        except Exception as e:
            print(f"  [X] Error: {str(e)}")

    print("\n" + "=" * 70)
    print(f"GENERATION COMPLETE")
    print("=" * 70)
    print(f"\nSuccessfully generated: {len(generated_files)}/{len(generators)} worksheets")
    print(f"\nFiles saved to: output/test/")

    return generated_files

if __name__ == "__main__":
    files = generate_all_challenge_worksheets()

    print("\n" + "-" * 70)
    print("Generated files:")
    for f in files:
        print(f"  - {f}")
    print("-" * 70)
