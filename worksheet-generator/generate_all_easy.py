"""
Generate all easy-level worksheets for all implemented topics.
Saves to easy_worksheets/ directory.
"""

import time
from pdf_generator import PDFWorksheetGenerator
from topic_registry import register_all_generators, get_registry


def generate_all_easy_worksheets():
    """Generate easy worksheets for all implemented topics."""

    # Initialize registry
    register_all_generators()
    registry = get_registry()

    # Get all implemented topics
    topics = registry.get_implemented_topics()

    pdf_gen = PDFWorksheetGenerator()

    print("=" * 70)
    print("GENERATING ALL EASY WORKSHEETS")
    print("=" * 70)
    print(f"\nTotal topics: {len(topics)}")
    print("Difficulty: EASY")
    print("Problems per worksheet: 8")
    print("\n" + "-" * 70)

    generated_files = []
    start_time = time.time()

    for i, topic_meta in enumerate(topics, 1):
        # Create filename from topic - sanitize for Windows
        filename = topic_meta.topic.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").replace("?", "")
        filename = f"{filename}_easy"

        print(f"\n[{i}/{len(topics)}] {topic_meta.topic}...")

        try:
            # Get generator instance
            generator = registry.get_generator(topic_meta.unit, topic_meta.type.value, topic_meta.topic)

            if not generator:
                print(f"  [X] No generator found")
                continue

            # Generate problems
            problems = generator.generate_worksheet('easy', 8)

            # Create output path
            output_path = f"easy_worksheets/{filename}.pdf"

            # Generate PDF with format: "Topic - Difficulty"
            title = f"{topic_meta.topic} - Easy"
            pdf_gen.generate_worksheet(problems, output_path, title=title, include_answer_key=True)

            generated_files.append(output_path)
            print(f"  [OK] Generated: {output_path}")

        except Exception as e:
            print(f"  [X] Error: {str(e)}")

    elapsed = time.time() - start_time

    print("\n" + "=" * 70)
    print(f"GENERATION COMPLETE")
    print("=" * 70)
    print(f"\nSuccessfully generated: {len(generated_files)}/{len(topics)} worksheets")
    print(f"Time elapsed: {elapsed:.1f} seconds")
    print(f"\nFiles saved to: easy_worksheets/")

    return generated_files


if __name__ == "__main__":
    files = generate_all_easy_worksheets()

    print("\n" + "-" * 70)
    print("Generated files:")
    for f in files:
        print(f"  - {f}")
    print("-" * 70)
