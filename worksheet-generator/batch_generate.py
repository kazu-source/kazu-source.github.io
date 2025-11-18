#!/usr/bin/env python3
"""
Batch Worksheet Generator - CLI tool for generating worksheets in batches.

Usage:
    python batch_generate.py --filter intro,graphing --difficulty easy
    python batch_generate.py --unit 4 --type graphing
    python batch_generate.py --all
    python batch_generate.py --coverage
"""

import argparse
import sys
from pathlib import Path

from topic_registry import get_registry, register_all_generators
from excel_config_loader import ExcelConfigLoader
from batch_orchestrator import BatchOrchestrator, GenerationTask
from output_manager import OutputManager


def setup_argparse() -> argparse.ArgumentParser:
    """Setup command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Batch Worksheet Generator - Generate multiple worksheets at once",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate all Intro and Graphing worksheets:
    python batch_generate.py --filter intro,graphing

  Generate all worksheets for Unit 4:
    python batch_generate.py --unit 4

  Generate only Graphing worksheets for Unit 5:
    python batch_generate.py --unit 5 --type graphing

  Generate all implemented worksheets:
    python batch_generate.py --all

  Show coverage report only (no generation):
    python batch_generate.py --coverage

  Generate with custom difficulty and problem count:
    python batch_generate.py --filter intro --difficulty medium --num-problems 15

  Skip existing files:
    python batch_generate.py --filter intro --skip-existing
        """
    )

    # Filter options
    filter_group = parser.add_argument_group("Filter Options")
    filter_group.add_argument(
        "--filter",
        type=str,
        help="Comma-separated list of types to generate (e.g., 'intro,graphing')"
    )
    filter_group.add_argument(
        "--unit",
        type=float,
        help="Generate only worksheets for specific unit number"
    )
    filter_group.add_argument(
        "--type",
        type=str,
        help="Generate only worksheets of specific type (e.g., 'intro' or 'graphing')"
    )
    filter_group.add_argument(
        "--all",
        action="store_true",
        help="Generate all implemented worksheets (no filter)"
    )

    # Generation options
    gen_group = parser.add_argument_group("Generation Options")
    gen_group.add_argument(
        "--difficulty",
        type=str,
        default="easy",
        choices=["easy", "medium", "hard"],
        help="Difficulty level (default: easy)"
    )
    gen_group.add_argument(
        "--num-problems",
        type=int,
        help="Number of problems per worksheet (default: use config default)"
    )
    gen_group.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip generation if output file already exists"
    )

    # Output options
    output_group = parser.add_argument_group("Output Options")
    output_group.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Base output directory (default: output)"
    )
    output_group.add_argument(
        "--generate-index",
        action="store_true",
        help="Generate HTML index after batch generation"
    )

    # Report options
    report_group = parser.add_argument_group("Report Options")
    report_group.add_argument(
        "--coverage",
        action="store_true",
        help="Show coverage report only (don't generate)"
    )
    report_group.add_argument(
        "--list-topics",
        action="store_true",
        help="List all topics and exit"
    )

    # Configuration
    config_group = parser.add_argument_group("Configuration")
    config_group.add_argument(
        "--excel",
        type=str,
        default="High School Worksheet Topics List.xlsx",
        help="Path to Excel configuration file"
    )

    return parser


def print_coverage_report(registry, excel_loader):
    """Print coverage report showing implemented vs. planned topics."""
    print("\n" + "=" * 70)
    print("WORKSHEET GENERATOR COVERAGE REPORT")
    print("=" * 70)

    # Registry stats
    stats = registry.get_coverage_stats()
    print(f"\nOverall Implementation:")
    print(f"  Implemented: {stats['implemented']:3d}")
    print(f"  Planned:     {stats['total_topics']:3d}")
    print(f"  Coverage:    {stats['percentage']:5.1f}%")

    # By type
    print(f"\nBy Type:")
    for type_name, type_stats in stats['by_type'].items():
        pct = type_stats['percentage']
        impl = type_stats['implemented']
        total = type_stats['total']
        print(f"  {type_name:15s}: {impl:3d}/{total:3d} ({pct:5.1f}%)")

    # Show unimplemented topics for Intro and Graphing
    print(f"\n" + "=" * 70)
    print("UNIMPLEMENTED TOPICS (Intro & Graphing)")
    print("=" * 70)

    unimplemented = registry.get_unimplemented_topics(type_filter=["Intro", "Graphing"])
    if unimplemented:
        for topic in unimplemented:
            status = "[ X]" if not topic.implemented else "[OK]"
            print(f"  {status} Unit {topic.unit:4.1f} | {topic.type.value:10s} | {topic.topic}")
    else:
        print("  All Intro and Graphing topics are implemented!")

    # Show implemented topics
    print(f"\n" + "=" * 70)
    print("IMPLEMENTED TOPICS (Ready for Generation)")
    print("=" * 70)

    implemented = registry.get_implemented_topics(type_filter=["Intro", "Graphing"])
    if implemented:
        for topic in implemented:
            status = "[OK]" if topic.implemented else "[ X]"
            print(f"  {status} Unit {topic.unit:4.1f} | {topic.type.value:10s} | {topic.topic}")
    else:
        print("  No topics implemented yet.")


def print_topic_list(registry):
    """Print list of all registered topics."""
    print("\n" + "=" * 70)
    print("ALL REGISTERED TOPICS")
    print("=" * 70)

    for unit in registry.get_units():
        print(f"\nUnit {unit}:")
        unit_topics = registry.get_all_topics(unit_filter=unit)
        for topic in unit_topics:
            status = "[OK]" if topic.implemented else "[ X]"
            print(f"  {status} {topic.type.value:15s} | {topic.topic}")


def main():
    """Main entry point for batch generation CLI."""
    parser = setup_argparse()
    args = parser.parse_args()

    # Initialize registry
    print("Initializing worksheet generator registry...")
    register_all_generators()
    registry = get_registry()

    # Load Excel configuration
    excel_path = Path(args.excel)
    if not excel_path.exists():
        print(f"Error: Excel file not found: {excel_path}")
        print("Please ensure the Excel configuration file exists.")
        sys.exit(1)

    print(f"Loading Excel configuration from: {excel_path}")
    excel_loader = ExcelConfigLoader(str(excel_path))
    excel_loader.load()

    # Sync Excel topics to registry
    type_filter = None
    if args.filter:
        type_filter = [t.strip().title() for t in args.filter.split(",")]
    elif args.type:
        type_filter = [args.type.strip().title()]

    sync_stats = excel_loader.sync_to_registry(registry, type_filter=type_filter)
    print(f"Synced {sync_stats['synced']} topics from Excel")

    # Handle report-only modes
    if args.coverage:
        print_coverage_report(registry, excel_loader)
        return

    if args.list_topics:
        print_topic_list(registry)
        return

    # Setup batch generation
    output_mgr = OutputManager(base_dir=args.output_dir)
    orchestrator = BatchOrchestrator(registry, output_base_dir=args.output_dir)

    # Determine type filter
    type_filter = None
    if args.filter:
        type_filter = [t.strip().title() for t in args.filter.split(",")]
    elif args.type:
        type_filter = [args.type.strip().title()]
    elif not args.all:
        # Default to Intro and Graphing if no filter specified
        type_filter = ["Intro", "Graphing"]
        print("\nNo filter specified - defaulting to Intro and Graphing types")

    # Create generation tasks
    print("\nCreating generation tasks...")
    tasks = orchestrator.create_tasks_from_registry(
        type_filter=type_filter,
        unit_filter=args.unit,
        difficulty=args.difficulty,
        num_problems=args.num_problems
    )

    if not tasks:
        print("\nNo tasks to generate!")
        print("This could mean:")
        print("  - No generators are implemented for the selected filters")
        print("  - The filters excluded all topics")
        print("\nTry running with --coverage to see what's implemented.")
        return

    print(f"Created {len(tasks)} generation tasks")

    # Confirm with user
    print(f"\nGeneration Plan:")
    print(f"  Tasks:       {len(tasks)}")
    print(f"  Difficulty:  {args.difficulty}")
    print(f"  Output dir:  {args.output_dir}")
    if args.skip_existing:
        print(f"  Mode:        Skip existing files")

    response = input("\nProceed with generation? [y/N]: ")
    if response.lower() != 'y':
        print("Cancelled.")
        return

    # Generate worksheets
    print("\nStarting batch generation...")
    results = orchestrator.generate_batch(tasks, skip_existing=args.skip_existing)

    # Register generated worksheets with output manager
    print("\nRegistering generated worksheets...")
    for result in results:
        if result.success and result.output_path:
            output_mgr.register_worksheet(
                course=result.task.course,
                unit=result.task.unit,
                type=result.task.type,
                topic=result.task.topic,
                difficulty=result.task.difficulty,
                num_problems=result.task.num_problems or 10,
                file_path=result.output_path
            )

    # Generate HTML index if requested
    if args.generate_index:
        print("\nGenerating HTML index...")
        index_path = output_mgr.generate_index_html()
        print(f"Index generated: {index_path}")

    # Show statistics
    print("\n" + "=" * 70)
    print("OUTPUT STATISTICS")
    print("=" * 70)
    stats = output_mgr.get_statistics()
    print(f"Total worksheets: {stats['total_worksheets']}")
    print(f"Total size: {stats['total_size_mb']:.2f} MB")

    print("\nDone!")


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
