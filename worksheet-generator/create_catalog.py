"""
Worksheet Catalog Generator
Creates an index/manifest of all available worksheets
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from topic_registry import get_registry, register_all_generators
from worksheet_config import get_config


def create_catalog(output_dir: str = "output"):
    """
    Create a catalog of all available worksheets.

    Args:
        output_dir: Output directory containing worksheets
    """
    # Register all generators
    register_all_generators()
    registry = get_registry()

    # Get all implemented topics
    implemented_topics = registry.get_implemented_topics()

    catalog_lines = []

    # Header
    catalog_lines.append("=" * 80)
    catalog_lines.append("ALGEBRA 1 WORKSHEET CATALOG")
    catalog_lines.append("=" * 80)
    catalog_lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    catalog_lines.append(f"Total Topics: {len(implemented_topics)}")
    catalog_lines.append(f"Total Worksheets: {len(implemented_topics) * 3} (3 difficulty levels each)")

    # Statistics
    stats = registry.get_coverage_stats()
    catalog_lines.append("\n" + "=" * 80)
    catalog_lines.append("COVERAGE STATISTICS")
    catalog_lines.append("=" * 80)
    catalog_lines.append(f"\nOverall: {stats['implemented']}/{stats['total_topics']} ({stats['percentage']:.1f}%)")
    catalog_lines.append("\nBy Type:")
    for type_name, type_stats in stats['by_type'].items():
        catalog_lines.append(f"  {type_name}: {type_stats['implemented']}/{type_stats['total']} ({type_stats['percentage']:.1f}%)")

    # Organize by unit
    topics_by_unit = {}
    for topic_meta in implemented_topics:
        unit = topic_meta.unit
        if unit not in topics_by_unit:
            topics_by_unit[unit] = []
        topics_by_unit[unit].append(topic_meta)

    # Generate catalog by unit
    catalog_lines.append("\n" + "=" * 80)
    catalog_lines.append("WORKSHEETS BY UNIT")
    catalog_lines.append("=" * 80)

    for unit in sorted(topics_by_unit.keys()):
        catalog_lines.append(f"\n{'=' * 80}")
        catalog_lines.append(f"UNIT {int(unit)}")
        catalog_lines.append(f"{'=' * 80}")

        # Organize by type
        topics_by_type = {}
        for topic_meta in topics_by_unit[unit]:
            topic_type = topic_meta.type.value
            if topic_type not in topics_by_type:
                topics_by_type[topic_type] = []
            topics_by_type[topic_type].append(topic_meta)

        for topic_type in sorted(topics_by_type.keys()):
            catalog_lines.append(f"\n{topic_type} Worksheets:")
            catalog_lines.append("-" * 80)

            for topic_meta in topics_by_type[topic_type]:
                config = get_config(topic_meta.config_key)

                catalog_lines.append(f"\n  • {topic_meta.topic}")
                catalog_lines.append(f"    - Default problems: {config.default_num_problems}")
                catalog_lines.append(f"    - Difficulty levels: Easy, Medium, Hard")
                catalog_lines.append(f"    - File pattern: Unit{int(unit)}/{topic_type}/{topic_meta.topic.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')}_{{difficulty}}_{{date}}.pdf")
                catalog_lines.append(f"    - Instructions: {config.instructions}")

    # File listing
    output_path = Path(output_dir)
    if output_path.exists():
        catalog_lines.append("\n" + "=" * 80)
        catalog_lines.append("GENERATED FILES")
        catalog_lines.append("=" * 80)

        for unit_dir in sorted(output_path.glob("Unit*")):
            unit_num = unit_dir.name.replace("Unit", "")
            catalog_lines.append(f"\nUnit {unit_num}:")

            for type_dir in sorted(unit_dir.glob("*")):
                if type_dir.is_dir():
                    pdf_files = sorted(type_dir.glob("*.pdf"))
                    if pdf_files:
                        catalog_lines.append(f"  {type_dir.name}/ ({len(pdf_files)} files)")
                        for pdf_file in pdf_files:
                            file_size = pdf_file.stat().st_size / 1024  # KB
                            catalog_lines.append(f"    - {pdf_file.name} ({file_size:.1f} KB)")

    # Quick reference guide
    catalog_lines.append("\n" + "=" * 80)
    catalog_lines.append("QUICK REFERENCE - TOPIC CODES")
    catalog_lines.append("=" * 80)
    catalog_lines.append("\nUnit 1 - Basics:")
    catalog_lines.append("  • Variables, Exponents, Evaluating Expressions")
    catalog_lines.append("  • Substitution, Combining Like Terms")
    catalog_lines.append("\nUnit 2 - Equations:")
    catalog_lines.append("  • Equations Intro, Inputs/Outputs, Solutions")
    catalog_lines.append("  • Variables on Both Sides, Property of Equality")
    catalog_lines.append("  • Multi-Step Equations, Linear Equations")
    catalog_lines.append("\nUnit 3 - Inequalities:")
    catalog_lines.append("  • One-Step Inequalities")
    catalog_lines.append("\nUnit 4 - Linear Equations (Two Variables):")
    catalog_lines.append("  • Graphing Points, Lines, Slope-Intercept")
    catalog_lines.append("  • Point-Slope Form, Standard Form")
    catalog_lines.append("\nUnit 5 - Systems of Equations:")
    catalog_lines.append("  • Systems of Equations (Intro & Graphing)")
    catalog_lines.append("\nUnit 11 - Quadratic Functions:")
    catalog_lines.append("  • Graphing Parabolas")

    # Save catalog
    catalog_path = Path("WORKSHEET_CATALOG.txt")
    with open(catalog_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(catalog_lines))

    print(f"Catalog created: {catalog_path.absolute()}")
    print(f"Total lines: {len(catalog_lines)}")

    # Also create markdown version
    md_path = Path("WORKSHEET_CATALOG.md")
    md_lines = []

    md_lines.append("# Algebra 1 Worksheet Catalog")
    md_lines.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    md_lines.append(f"\n**Total Topics:** {len(implemented_topics)}")
    md_lines.append(f"**Total Worksheets:** {len(implemented_topics) * 3} (3 difficulty levels each)")

    md_lines.append("\n## Coverage Statistics")
    md_lines.append(f"\n- **Overall:** {stats['implemented']}/{stats['total_topics']} ({stats['percentage']:.1f}%)")
    md_lines.append("- **By Type:**")
    for type_name, type_stats in stats['by_type'].items():
        md_lines.append(f"  - {type_name}: {type_stats['implemented']}/{type_stats['total']} ({type_stats['percentage']:.1f}%)")

    md_lines.append("\n## Worksheets by Unit")

    for unit in sorted(topics_by_unit.keys()):
        md_lines.append(f"\n### Unit {int(unit)}")

        topics_by_type = {}
        for topic_meta in topics_by_unit[unit]:
            topic_type = topic_meta.type.value
            if topic_type not in topics_by_type:
                topics_by_type[topic_type] = []
            topics_by_type[topic_type].append(topic_meta)

        for topic_type in sorted(topics_by_type.keys()):
            md_lines.append(f"\n#### {topic_type} Worksheets")

            for topic_meta in topics_by_type[topic_type]:
                config = get_config(topic_meta.config_key)
                md_lines.append(f"\n**{topic_meta.topic}**")
                md_lines.append(f"- Default problems: {config.default_num_problems}")
                md_lines.append(f"- Difficulty levels: Easy, Medium, Hard")
                md_lines.append(f"- Instructions: _{config.instructions}_")

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))

    print(f"Markdown catalog created: {md_path.absolute()}")

    return catalog_path, md_path


if __name__ == "__main__":
    create_catalog()
