"""
Generate all 108 easy worksheets using both existing and new Opus generators.
Saves all PDFs to opus_easy_worksheets/ directory.
"""

import json
import time
import sys
import os
import importlib.util

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_generator import PDFWorksheetGenerator
from topic_registry import register_all_generators, get_registry

def load_opus_generator(filename, class_name):
    """Dynamically load an Opus generator."""
    module_path = os.path.join('opus_worksheet_generators', f'{filename}_generator.py')
    spec = importlib.util.spec_from_file_location(filename, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    generator_class = getattr(module, f'{class_name}Generator')
    return generator_class()

def sanitize_filename(text):
    """Sanitize text for use as filename."""
    # Remove or replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        text = text.replace(char, '')
    # Replace other problematic characters
    text = text.replace('(', '').replace(')', '').replace(',', '')
    text = text.replace(' ', '_').replace('__', '_')
    return text

def main():
    """Generate all 108 easy worksheets."""
    print("=" * 70)
    print("GENERATING ALL 108 OPUS EASY WORKSHEETS")
    print("=" * 70)

    # Initialize registry for existing generators
    register_all_generators()
    registry = get_registry()

    # Load mappings
    with open('opus_worksheet_generators/all_topics.json', 'r') as f:
        all_topics = json.load(f)

    with open('opus_worksheet_generators/generator_mapping.json', 'r') as f:
        mapping = json.load(f)

    with open('opus_worksheet_generators/created_generators.json', 'r') as f:
        created_generators = json.load(f)

    # Create lookup for created generators
    created_lookup = {item['topic']: item for item in created_generators}

    # Create lookup for existing generators
    existing_lookup = {item['topic']: item['existing'] for item in mapping['existing_generators']}

    pdf_gen = PDFWorksheetGenerator()

    print(f"Total topics: {len(all_topics)}")
    print(f"Existing generators: {len(existing_lookup)}")
    print(f"New Opus generators: {len(created_lookup)}")
    print("Difficulty: EASY")
    print("Problems per worksheet: 8")
    print("\n" + "-" * 70)

    generated_files = []
    errors = []
    start_time = time.time()

    # List of expansion topics to skip
    expansion_topics = [
        'Of Why Dividing by Zero Does Not Work',
        'Parenthesis Explanation (multiplication)',
        'Which Type of Equation Is Best for Each Situation',
        'Understanding the Limits of the Three Different Types, Use Cases',
        'Dartboard (picking a random point and understanding the meaning of the x and y value)',
        'Explanation of Why an Even Square Root Cannot Be Negative',
        'Special Products of Polynomials',
        'Factoring Tips and Tricks',
        'Interpreting the Roots of Quadratic Equations (factored form)',
        'Understanding the Three Main Ways to Solve + Graph Quadratics; What Is the Point? (vertex form, standard form, factored form)',
        'When to Use Each Type of Factoring'
    ]

    for i, topic_data in enumerate(all_topics, 1):
        topic = topic_data['topic']
        unit = topic_data['unit']
        topic_type = topic_data.get('type', 'Intro')

        print(f"\n[{i}/{len(all_topics)}] Unit {int(unit)} - {topic}")

        # Skip expansion topics
        if topic in expansion_topics or topic_type == 'Expansion':
            print(f"  [SKIP] Expansion topic - will be created manually")
            continue

        try:
            generator = None

            # Check if it's an existing generator
            if topic in existing_lookup:
                existing_topic = existing_lookup[topic]
                generator = registry.get_generator(unit, topic_type, existing_topic)
                if not generator:
                    # Try with different type
                    for try_type in ['Intro', 'Graphing', 'Solving']:
                        generator = registry.get_generator(unit, try_type, existing_topic)
                        if generator:
                            break
                print(f"  Using existing generator: {existing_topic}")

            # Otherwise, use new Opus generator
            elif topic in created_lookup:
                gen_info = created_lookup[topic]
                generator = load_opus_generator(gen_info['filename'], gen_info['class_name'])
                print(f"  Using Opus generator: {gen_info['class_name']}")

            else:
                print(f"  [X] No generator found for: {topic}")
                errors.append(f"No generator: {topic}")
                continue

            if not generator:
                print(f"  [X] Failed to load generator")
                errors.append(f"Failed to load: {topic}")
                continue

            # Generate problems
            problems = generator.generate_worksheet('easy', 8)

            # Create output filename
            safe_topic = sanitize_filename(topic)
            output_path = f"opus_easy_worksheets/Unit{int(unit):02d}_{safe_topic}_easy.pdf"

            # Generate PDF
            title = f"Unit {int(unit)} - {topic} (Easy)"
            pdf_gen.generate_worksheet(problems, output_path, title=title, include_answer_key=True)

            generated_files.append(output_path)
            print(f"  [OK] Generated: {output_path}")

        except Exception as e:
            error_msg = f"{topic}: {str(e)}"
            errors.append(error_msg)
            print(f"  [X] Error: {str(e)}")

    elapsed = time.time() - start_time

    print("\n" + "=" * 70)
    print(f"GENERATION COMPLETE")
    print("=" * 70)
    print(f"\nSuccessfully generated: {len(generated_files)}/{len(all_topics)} worksheets")
    print(f"Errors: {len(errors)}")
    print(f"Time elapsed: {elapsed:.1f} seconds")
    print(f"\nFiles saved to: opus_easy_worksheets/")

    if errors:
        print("\n" + "-" * 70)
        print("ERRORS:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")

    # Save summary
    summary = {
        'total_topics': len(all_topics),
        'generated': len(generated_files),
        'errors': len(errors),
        'time_seconds': elapsed,
        'generated_files': generated_files,
        'error_details': errors
    }

    with open('opus_easy_worksheets/generation_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\nSummary saved to: opus_easy_worksheets/generation_summary.json")

    return generated_files

if __name__ == "__main__":
    files = main()