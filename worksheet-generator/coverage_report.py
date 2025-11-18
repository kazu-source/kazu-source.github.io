#!/usr/bin/env python3
"""
Coverage Report Tool - Analyzes and reports on worksheet generator coverage.
Compares Excel topic lists with implemented generators.
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

from topic_registry import get_registry, register_all_generators, TopicMetadata
from excel_config_loader import ExcelConfigLoader, MultiCourseLoader


class CoverageReporter:
    """Generates detailed coverage reports for worksheet generators."""

    def __init__(self):
        """Initialize coverage reporter."""
        self.registry = get_registry()
        self.excel_loaders: Dict[str, ExcelConfigLoader] = {}

    def add_excel_config(self, path: str, course_name: str = None):
        """
        Add an Excel configuration file.

        Args:
            path: Path to Excel file
            course_name: Optional course name (auto-detected if not provided)
        """
        loader = ExcelConfigLoader(path)
        loader.load()

        name = course_name if course_name else loader.course_name
        self.excel_loaders[name] = loader

        # Sync to registry
        loader.sync_to_registry(self.registry)

    def generate_full_report(self) -> str:
        """
        Generate comprehensive coverage report.

        Returns:
            Formatted report string
        """
        lines = []
        lines.append("=" * 80)
        lines.append("WORKSHEET GENERATOR COVERAGE REPORT")
        lines.append("=" * 80)
        lines.append("")

        # Overall statistics
        stats = self.registry.get_coverage_stats()
        lines.append("OVERALL STATISTICS")
        lines.append("-" * 80)
        lines.append(f"Total Topics:       {stats['total_topics']:4d}")
        lines.append(f"Implemented:        {stats['implemented']:4d} ({stats['percentage']:.1f}%)")
        lines.append(f"Not Implemented:    {stats['unimplemented']:4d}")
        lines.append("")

        # By type
        lines.append("COVERAGE BY TYPE")
        lines.append("-" * 80)
        lines.append(f"{'Type':<20s} {'Total':>8s} {'Implemented':>12s} {'Coverage':>10s}")
        lines.append("-" * 80)

        for type_name, type_stats in sorted(stats['by_type'].items()):
            total = type_stats['total']
            implemented = type_stats['implemented']
            pct = type_stats['percentage']
            lines.append(f"{type_name:<20s} {total:>8d} {implemented:>12d} {pct:>9.1f}%")

        lines.append("")

        # Focus on Intro and Graphing (current priority)
        lines.append("=" * 80)
        lines.append("PRIORITY TYPES: INTRO & GRAPHING")
        lines.append("=" * 80)
        lines.append("")

        intro_graphing = self.registry.get_all_topics(type_filter=["Intro", "Graphing"])
        implemented_ig = [t for t in intro_graphing if t.implemented]
        unimplemented_ig = [t for t in intro_graphing if not t.implemented]

        lines.append(f"Total Intro/Graphing Topics: {len(intro_graphing)}")
        lines.append(f"Implemented:                 {len(implemented_ig)} ({len(implemented_ig)/len(intro_graphing)*100:.1f}%)")
        lines.append(f"Not Implemented:             {len(unimplemented_ig)}")
        lines.append("")

        # Implemented topics
        if implemented_ig:
            lines.append("IMPLEMENTED (Intro & Graphing)")
            lines.append("-" * 80)
            for topic in sorted(implemented_ig, key=lambda t: (t.unit, t.type.value, t.topic)):
                lines.append(f"[OK] Unit {topic.unit:4.1f} | {topic.type.value:10s} | {topic.topic}")
            lines.append("")

        # Unimplemented topics
        if unimplemented_ig:
            lines.append("NOT IMPLEMENTED (Intro & Graphing)")
            lines.append("-" * 80)
            for topic in sorted(unimplemented_ig, key=lambda t: (t.unit, t.type.value, t.topic)):
                lines.append(f"[ X] Unit {topic.unit:4.1f} | {topic.type.value:10s} | {topic.topic}")
            lines.append("")

        # By unit breakdown
        lines.append("=" * 80)
        lines.append("COVERAGE BY UNIT")
        lines.append("=" * 80)
        lines.append("")

        unit_coverage = self._calculate_unit_coverage()
        lines.append(f"{'Unit':<8s} {'Total':>8s} {'Implemented':>12s} {'Coverage':>10s}")
        lines.append("-" * 80)

        for unit in sorted(unit_coverage.keys()):
            stats = unit_coverage[unit]
            total = stats['total']
            implemented = stats['implemented']
            pct = implemented / total * 100 if total > 0 else 0
            lines.append(f"{unit:<8.1f} {total:>8d} {implemented:>12d} {pct:>9.1f}%")

        lines.append("")

        # Gap analysis
        lines.append("=" * 80)
        lines.append("GAP ANALYSIS - WHAT'S MISSING?")
        lines.append("=" * 80)
        lines.append("")

        gaps = self._identify_gaps()
        if gaps:
            for unit, gap_info in sorted(gaps.items()):
                if gap_info['missing']:
                    lines.append(f"Unit {unit}:")
                    for topic in gap_info['missing']:
                        lines.append(f"  [ X] {topic.type.value:10s} | {topic.topic}")
                    lines.append("")
        else:
            lines.append("No gaps found! All topics are implemented.")
            lines.append("")

        return "\n".join(lines)

    def generate_summary_report(self) -> str:
        """
        Generate brief summary report.

        Returns:
            Formatted summary string
        """
        lines = []
        stats = self.registry.get_coverage_stats()

        lines.append("=" * 60)
        lines.append("COVERAGE SUMMARY")
        lines.append("=" * 60)
        lines.append(f"Implemented: {stats['implemented']}/{stats['total_topics']} ({stats['percentage']:.1f}%)")
        lines.append("")

        # Priority types
        intro_graphing = self.registry.get_all_topics(type_filter=["Intro", "Graphing"])
        implemented_ig = len([t for t in intro_graphing if t.implemented])

        if intro_graphing:
            pct = implemented_ig / len(intro_graphing) * 100
            lines.append(f"Intro & Graphing: {implemented_ig}/{len(intro_graphing)} ({pct:.1f}%)")

        return "\n".join(lines)

    def export_csv(self, output_path: str):
        """
        Export coverage data to CSV.

        Args:
            output_path: Path to output CSV file
        """
        import csv

        all_topics = self.registry.get_all_topics()

        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # Header
            writer.writerow(['Unit', 'Type', 'Topic', 'Implemented', 'Config Key'])

            # Data
            for topic in sorted(all_topics, key=lambda t: (t.unit, t.type.value, t.topic)):
                writer.writerow([
                    topic.unit,
                    topic.type.value,
                    topic.topic,
                    'Yes' if topic.implemented else 'No',
                    topic.config_key or ''
                ])

        print(f"Coverage data exported to: {output_path}")

    def _calculate_unit_coverage(self) -> Dict[float, Dict]:
        """Calculate coverage statistics by unit."""
        unit_stats = defaultdict(lambda: {'total': 0, 'implemented': 0})

        for topic in self.registry.get_all_topics():
            unit_stats[topic.unit]['total'] += 1
            if topic.implemented:
                unit_stats[topic.unit]['implemented'] += 1

        return dict(unit_stats)

    def _identify_gaps(self) -> Dict[float, Dict]:
        """Identify missing generators by unit."""
        gaps = defaultdict(lambda: {'missing': [], 'total': 0})

        for topic in self.registry.get_all_topics():
            gaps[topic.unit]['total'] += 1
            if not topic.implemented:
                gaps[topic.unit]['missing'].append(topic)

        return dict(gaps)


def setup_argparse() -> argparse.ArgumentParser:
    """Setup command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Coverage Report Tool - Analyze worksheet generator coverage",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate full coverage report:
    python coverage_report.py --full

  Generate summary report:
    python coverage_report.py --summary

  Export coverage to CSV:
    python coverage_report.py --export coverage.csv

  Focus on Intro and Graphing types:
    python coverage_report.py --full --filter intro,graphing
        """
    )

    parser.add_argument(
        "--full",
        action="store_true",
        help="Generate full detailed report (default)"
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Generate brief summary report"
    )
    parser.add_argument(
        "--export",
        type=str,
        metavar="FILE",
        help="Export coverage data to CSV file"
    )
    parser.add_argument(
        "--filter",
        type=str,
        help="Filter by types (comma-separated, e.g., 'intro,graphing')"
    )
    parser.add_argument(
        "--excel",
        type=str,
        default="High School Worksheet Topics List.xlsx",
        help="Path to Excel configuration file"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Save report to file instead of printing to console"
    )

    return parser


def main():
    """Main entry point for coverage report tool."""
    parser = setup_argparse()
    args = parser.parse_args()

    # Initialize
    print("Initializing worksheet generator registry...")
    register_all_generators()

    # Create reporter
    reporter = CoverageReporter()

    # Load Excel config
    excel_path = Path(args.excel)
    if not excel_path.exists():
        print(f"Error: Excel file not found: {excel_path}")
        sys.exit(1)

    print(f"Loading Excel configuration from: {excel_path}")
    reporter.add_excel_config(str(excel_path))

    # Generate report
    if args.summary:
        report = reporter.generate_summary_report()
    else:
        # Full report is default
        report = reporter.generate_full_report()

    # Output report
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to: {args.output}")
    else:
        print("\n" + report)

    # Export CSV if requested
    if args.export:
        reporter.export_csv(args.export)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
