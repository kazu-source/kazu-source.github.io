"""
Script to add 'challenge' difficulty level to all existing generators.
This will systematically update each generator to support challenge-level problems.
"""

import os
from pathlib import Path

# List of all generator files to update (from topic_registry.py)
GENERATORS_TO_UPDATE = [
    # Chapter 1
    ("generators/chapter01", "variables_generator.py"),
    ("generators/chapter01", "exponents_generator.py"),
    ("generators/chapter01", "evaluating_expressions_generator.py"),
    ("generators/chapter01", "substitution_generator.py"),
    ("generators/chapter01", "combining_like_terms_generator.py"),

    # Chapter 2
    ("generators/chapter02", "equations_intro_generator.py"),
    ("generators/chapter02", "inputs_outputs_generator.py"),
    ("generators/chapter02", "solutions_generator.py"),
    ("generators/chapter02", "variables_both_sides_generator.py"),

    # Root level
    (".", "properties_generator.py"),
    (".", "properties_mult_div_generator.py"),
    (".", "multistep_generator.py"),
    (".", "equation_generator.py"),
    (".", "word_problems_generator.py"),
    (".", "inequalities_generator.py"),
    (".", "systems_generator.py"),

    # Chapter 4
    ("generators/chapter04", "graphing_points.py"),
    ("generators/chapter04", "graphing_lines.py"),
    ("generators/chapter04", "graphing_slope_intercept.py"),
    ("generators/chapter04", "graphing_point_slope.py"),
    ("generators/chapter04", "graphing_standard_form.py"),

    # Chapter 5
    ("generators/chapter05", "graphing_systems.py"),

    # Chapter 11
    ("generators/chapter11", "graphing_parabolas.py"),
]

def check_generators():
    """Check which generators already have challenge mode."""
    print("=" * 80)
    print("GENERATOR CHALLENGE MODE STATUS")
    print("=" * 80)

    base_dir = Path(__file__).parent

    for subdir, filename in GENERATORS_TO_UPDATE:
        filepath = base_dir / subdir / filename

        if not filepath.exists():
            print(f"MISSING: {filepath}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        has_challenge = '_generate_challenge' in content or 'elif difficulty == \'challenge\'' in content
        status = "OK" if has_challenge else "NEEDS UPDATE"

        print(f"{status:15} {subdir}/{filename}")

if __name__ == "__main__":
    check_generators()
