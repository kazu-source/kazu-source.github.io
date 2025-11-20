"""
Generate challenge-level worksheets for all implemented topics.
Outputs to output/comprehensive_tests folder for manual review.
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from topic_registry import get_registry, register_all_generators
from pdf_generator import PDFWorksheetGenerator


def generate_all_challenge_worksheets():
    """Generate challenge-level worksheets for all topics."""

    # Initialize
    register_all_generators()
    registry = get_registry()
    pdf_gen = PDFWorksheetGenerator()

    # Get all implemented topics
    topics = registry.get_implemented_topics()

    print("=" * 80)
    print("CHALLENGE WORKSHEET GENERATOR")
    print("=" * 80)
    print(f"\nGenerating challenge-level worksheets for {len(topics)} topics...")
    print(f"Output folder: output/comprehensive_tests/\n")

    # Create output directory
    output_dir = Path("output") / "comprehensive_tests"
    output_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0
    error_count = 0

    for i, topic_meta in enumerate(topics, 1):
        try:
            print(f"[{i}/{len(topics)}] Generating: Unit {int(topic_meta.unit)} - {topic_meta.topic} ({topic_meta.type.value})")

            # Get generator
            generator = registry.get_generator(
                topic_meta.unit,
                topic_meta.type.value,
                topic_meta.topic
            )

            if not generator:
                print(f"  ERROR: Generator not found")
                error_count += 1
                continue

            # Generate challenge problems
            problems = generator.generate_worksheet('challenge', 10)

            # Create filename
            unit_str = f"Unit{int(topic_meta.unit)}"
            type_str = topic_meta.type.value
            topic_clean = topic_meta.topic.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("?", "")
            filename = f"{unit_str}_{type_str}_{topic_clean}_Challenge.pdf"
            output_path = output_dir / filename

            # Create title
            pdf_title = f"{topic_meta.topic} (Challenge)"

            # Generate PDF
            pdf_gen.generate_worksheet(problems, str(output_path), title=pdf_title)

            print(f"  SUCCESS: {filename}")
            success_count += 1

        except Exception as e:
            print(f"  ERROR: {e}")
            error_count += 1

    print("\n" + "=" * 80)
    print("GENERATION COMPLETE")
    print("=" * 80)
    print(f"Success: {success_count}/{len(topics)}")
    print(f"Errors: {error_count}/{len(topics)}")
    print(f"\nWorksheets saved to: {output_dir.absolute()}")


if __name__ == "__main__":
    generate_all_challenge_worksheets()
