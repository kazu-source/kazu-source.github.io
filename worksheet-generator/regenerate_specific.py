"""Quick script to regenerate specific worksheets."""

import sys
from pathlib import Path
from topic_registry import get_registry, register_all_generators
from pdf_generator import PDFWorksheetGenerator
from worksheet_config import get_config

# Register all generators
register_all_generators()
registry = get_registry()

# Worksheets to regenerate
worksheets = [
    (2.0, "Intro", "Equations"),
    (2.0, "Intro", "Inputs and Outputs"),
]

output_dir = Path("output")
pdf_gen = PDFWorksheetGenerator()

for unit, type_, topic in worksheets:
    for difficulty in ['easy', 'medium', 'hard']:
        # Get generator
        generator = registry.get_generator(unit, type_, topic)
        if not generator:
            print(f"X Unit {unit} | {type_} | {topic} - Not implemented")
            continue

        # Get config
        topic_meta = registry.get_topic(unit, type_, topic)
        config = get_config(topic_meta.config_key)
        num_problems = config.default_num_problems

        # Generate problems
        problems = generator.generate_worksheet(difficulty, num_problems)

        # Create output path
        unit_dir = output_dir / f"Unit{int(unit)}" / type_
        unit_dir.mkdir(parents=True, exist_ok=True)

        from datetime import datetime
        date_str = datetime.now().strftime("%Y%m%d")
        topic_clean = topic.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        filename = f"{topic_clean}_{difficulty}_{date_str}.pdf"
        output_path = unit_dir / filename

        # Generate PDF
        title = f"Algebra 1 - Unit {int(unit)} - {topic} ({difficulty.capitalize()})"
        pdf_gen.generate_worksheet(
            problems,
            str(output_path),
            title=title
        )

        print(f"OK {output_path}")

print("\nRegeneration complete!")
