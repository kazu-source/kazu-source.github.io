"""
Batch Generation Script - Regenerate All Worksheets
Generates all 92 worksheets (23 topics × 4 difficulty levels)
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from topic_registry import get_registry, register_all_generators
from pdf_generator import PDFWorksheetGenerator
from worksheet_config import get_config


def generate_all_worksheets(output_base_dir: str = "output/comprehensive_tests", difficulties: list = None):
    """
    Generate all worksheets for all implemented topics.

    Args:
        output_base_dir: Base output directory (default: "output/comprehensive_tests")
        difficulties: List of difficulties to generate (default: ['easy', 'medium', 'hard', 'challenge'])
    """
    if difficulties is None:
        difficulties = ['easy', 'medium', 'hard', 'challenge']
    # Register all generators
    register_all_generators()
    registry = get_registry()

    # Get all implemented topics
    implemented_topics = registry.get_implemented_topics()

    # Initialize PDF generator
    pdf_gen = PDFWorksheetGenerator()

    # Statistics
    total_worksheets = 0
    successful = 0
    failed = []

    output_dir = Path(output_base_dir)

    print("=" * 80)
    print("BATCH WORKSHEET GENERATION")
    print("=" * 80)
    print(f"\nGenerating worksheets for {len(implemented_topics)} topics...")
    print(f"Output directory: {output_dir.absolute()}\n")

    start_time = datetime.now()

    for topic_meta in implemented_topics:
        unit = topic_meta.unit
        topic_type = topic_meta.type.value
        topic = topic_meta.topic

        print(f"\n{'-' * 80}")
        print(f"Unit {unit} | {topic_type} | {topic}")
        print(f"{'-' * 80}")

        # Generate for specified difficulty levels
        for difficulty in difficulties:
            total_worksheets += 1

            try:
                # Get generator
                generator = registry.get_generator(unit, topic_type, topic)
                if not generator:
                    print(f"  X {difficulty.upper()}: Generator not found")
                    failed.append(f"{topic} ({difficulty})")
                    continue

                # Get config
                config = get_config(topic_meta.config_key)
                num_problems = config.get_default_num_problems(difficulty)

                # Generate problems (handle compound inequality types)
                if 'compound_inequality_and' in topic_meta.config_key:
                    problems = generator.generate_worksheet(difficulty, num_problems, compound_type='and')
                elif 'compound_inequality_or' in topic_meta.config_key:
                    problems = generator.generate_worksheet(difficulty, num_problems, compound_type='or')
                else:
                    problems = generator.generate_worksheet(difficulty, num_problems)

                # Create output path directly in base directory (no subdirectories)
                output_dir.mkdir(parents=True, exist_ok=True)

                # Generate filename
                date_str = datetime.now().strftime("%Y%m%d")
                topic_clean = topic.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("?", "")
                filename = f"{topic_clean}_{difficulty}_{date_str}.pdf"
                output_path = output_dir / filename

                # Generate PDF
                title = f"Algebra 1 - Unit {int(unit)} - {topic} ({difficulty.capitalize()})"
                pdf_gen.generate_worksheet(
                    problems,
                    str(output_path),
                    title=title
                )

                successful += 1
                print(f"  OK {difficulty.upper()}: {output_path.name}")

            except Exception as e:
                print(f"  X {difficulty.upper()}: ERROR - {str(e)}")
                failed.append(f"{topic} ({difficulty}): {str(e)}")

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    # Print summary
    print("\n" + "=" * 80)
    print("GENERATION SUMMARY")
    print("=" * 80)
    print(f"\nTotal worksheets: {total_worksheets}")
    print(f"Successful: {successful} ({successful/total_worksheets*100:.1f}%)")
    print(f"Failed: {len(failed)} ({len(failed)/total_worksheets*100:.1f}%)")
    print(f"Duration: {duration:.1f} seconds")

    if failed:
        print("\n" + "=" * 80)
        print("FAILED WORKSHEETS")
        print("=" * 80)
        for failure in failed:
            print(f"  - {failure}")

    print("\n" + "=" * 80)
    print(f"All worksheets saved to: {output_dir.absolute()}")
    print("=" * 80)


if __name__ == "__main__":
    generate_all_worksheets()
