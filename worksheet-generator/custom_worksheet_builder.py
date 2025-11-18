"""
Custom Worksheet Builder - Interactive CLI for creating custom worksheets
Allows teachers to easily build worksheets with specific topics and difficulties
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from topic_registry import get_registry, register_all_generators
from pdf_generator import PDFWorksheetGenerator


def print_header():
    """Print welcome header."""
    print("=" * 80)
    print("CUSTOM WORKSHEET BUILDER")
    print("Interactive tool for creating custom Algebra 1 worksheets")
    print("=" * 80)
    print()


def list_units(registry):
    """List all available units."""
    units = registry.get_units()
    print("\nAvailable Units:")
    for unit in units:
        unit_topics = [t for t in registry.get_implemented_topics() if t.unit == unit]
        print(f"  Unit {int(unit)}: {len(unit_topics)} topics available")
    return units


def list_topics(registry, unit):
    """List all topics for a unit."""
    topics = [t for t in registry.get_implemented_topics() if t.unit == unit]
    print(f"\nTopics in Unit {int(unit)}:")
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. {topic.topic} ({topic.type.value})")
    return topics


def get_user_choice(prompt, max_value):
    """Get a valid integer choice from user."""
    while True:
        try:
            choice = input(prompt).strip()
            if choice.lower() in ['q', 'quit', 'exit']:
                return None
            value = int(choice)
            if 1 <= value <= max_value:
                return value
            print(f"Please enter a number between 1 and {max_value}")
        except ValueError:
            print("Please enter a valid number (or 'q' to quit)")


def get_difficulty():
    """Get difficulty level from user."""
    print("\nSelect difficulty level:")
    print("  1. Easy")
    print("  2. Medium")
    print("  3. Hard")
    print("  4. Challenge")
    print("  5. Mixed (random selection)")

    difficulties = ['easy', 'medium', 'hard', 'challenge', 'mixed']
    choice = get_user_choice("Enter choice (1-5): ", 5)
    if choice is None:
        return None
    return difficulties[choice - 1]


def get_num_problems():
    """Get number of problems from user."""
    while True:
        try:
            num = input("\nHow many problems? (1-30, or press Enter for 10): ").strip()
            if not num:
                return 10
            if num.lower() in ['q', 'quit', 'exit']:
                return None
            value = int(num)
            if 1 <= value <= 30:
                return value
            print("Please enter a number between 1 and 30")
        except ValueError:
            print("Please enter a valid number")


def get_worksheet_title():
    """Get custom title from user."""
    title = input("\nWorksheet title (or press Enter for auto-generated): ").strip()
    return title if title else None


def build_worksheet_interactive():
    """Interactive worksheet building."""
    print_header()

    # Initialize
    register_all_generators()
    registry = get_registry()
    pdf_gen = PDFWorksheetGenerator()

    # Show available units
    units = list_units(registry)

    # Select unit
    unit_choice = get_user_choice(f"\nSelect unit (1-{len(units)}, or 'q' to quit): ", len(units))
    if unit_choice is None:
        print("\nExiting...")
        return

    selected_unit = units[unit_choice - 1]

    # Show topics for selected unit
    topics = list_topics(registry, selected_unit)

    # Select topic
    topic_choice = get_user_choice(f"\nSelect topic (1-{len(topics)}, or 'q' to quit): ", len(topics))
    if topic_choice is None:
        print("\nExiting...")
        return

    selected_topic = topics[topic_choice - 1]

    # Get difficulty
    difficulty = get_difficulty()
    if difficulty is None:
        print("\nExiting...")
        return

    # Get number of problems
    num_problems = get_num_problems()
    if num_problems is None:
        print("\nExiting...")
        return

    # Get custom title
    custom_title = get_worksheet_title()

    # Generate worksheet
    print("\n" + "-" * 80)
    print("Generating worksheet...")
    print("-" * 80)

    try:
        # Get generator
        generator = registry.get_generator(
            selected_topic.unit,
            selected_topic.type.value,
            selected_topic.topic
        )

        if not generator:
            print(f"ERROR: Generator not found for {selected_topic.topic}")
            return

        # Generate problems
        if difficulty == 'mixed':
            # Generate mixed difficulty
            import random
            problems = []
            difficulties = ['easy', 'medium', 'hard', 'challenge']
            for _ in range(num_problems):
                diff = random.choice(difficulties)
                problem = generator.generate_worksheet(diff, 1)
                problems.extend(problem)
        else:
            problems = generator.generate_worksheet(difficulty, num_problems)

        # Create output path
        date_str = datetime.now().strftime("%Y%m%d")
        topic_clean = selected_topic.topic.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("?", "")
        output_dir = Path("output") / f"Unit{int(selected_topic.unit)}" / "Custom"
        output_dir.mkdir(parents=True, exist_ok=True)

        if custom_title:
            title_clean = custom_title.replace(" ", "_")
            filename = f"{title_clean}_{date_str}.pdf"
            pdf_title = custom_title
        else:
            filename = f"{topic_clean}_{difficulty}_{num_problems}problems_{date_str}.pdf"
            pdf_title = f"Algebra 1 - Unit {int(selected_topic.unit)} - {selected_topic.topic} ({difficulty.capitalize()})"

        output_path = output_dir / filename

        # Generate PDF
        pdf_gen.generate_worksheet(problems, str(output_path), title=pdf_title)

        print(f"\nWorksheet created successfully!")
        print(f"Location: {output_path.absolute()}")
        print(f"Title: {pdf_title}")
        print(f"Problems: {len(problems)}")
        print(f"Difficulty: {difficulty}")

    except Exception as e:
        print(f"\nERROR generating worksheet: {e}")
        import traceback
        traceback.print_exc()


def build_from_args():
    """Build worksheet from command-line arguments."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Custom Worksheet Builder - Create custom Algebra 1 worksheets",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python custom_worksheet_builder.py

  # Generate 15 medium equations problems
  python custom_worksheet_builder.py --unit 2 --topic "Equations" --difficulty medium --num 15

  # Generate 20 mixed difficulty systems problems
  python custom_worksheet_builder.py --unit 5 --topic "Systems of Equations" --difficulty mixed --num 20 --title "Systems Review"
        """
    )

    parser.add_argument('--unit', type=float, help='Unit number (e.g., 1.0, 2.0, 5.0)')
    parser.add_argument('--topic', type=str, help='Topic name (must match exactly)')
    parser.add_argument('--type', type=str, default="Intro", help='Topic type (default: Intro)')
    parser.add_argument('--difficulty', type=str, choices=['easy', 'medium', 'hard', 'challenge', 'mixed'],
                        default='medium', help='Difficulty level (default: medium)')
    parser.add_argument('--num', type=int, default=10, help='Number of problems (default: 10)')
    parser.add_argument('--title', type=str, help='Custom worksheet title')
    parser.add_argument('--output', type=str, help='Custom output path')

    args = parser.parse_args()

    # If no arguments, run interactive mode
    if not args.unit and not args.topic:
        build_worksheet_interactive()
        return

    # Validate arguments
    if not args.unit or not args.topic:
        parser.error("--unit and --topic are required for non-interactive mode")

    # Initialize
    register_all_generators()
    registry = get_registry()
    pdf_gen = PDFWorksheetGenerator()

    print("=" * 80)
    print("CUSTOM WORKSHEET BUILDER - Command Line Mode")
    print("=" * 80)
    print()

    try:
        # Get generator
        generator = registry.get_generator(args.unit, args.type, args.topic)

        if not generator:
            print(f"ERROR: Generator not found for Unit {args.unit} - {args.type} - {args.topic}")
            print("\nAvailable topics:")
            topics = [t for t in registry.get_implemented_topics() if t.unit == args.unit]
            for topic in topics:
                print(f"  - {topic.topic} ({topic.type.value})")
            return

        # Generate problems
        print(f"Generating {args.num} {args.difficulty} problems for {args.topic}...")

        if args.difficulty == 'mixed':
            import random
            problems = []
            difficulties = ['easy', 'medium', 'hard', 'challenge']
            for _ in range(args.num):
                diff = random.choice(difficulties)
                problem = generator.generate_worksheet(diff, 1)
                problems.extend(problem)
        else:
            problems = generator.generate_worksheet(args.difficulty, args.num)

        # Create output path
        if args.output:
            output_path = Path(args.output)
        else:
            date_str = datetime.now().strftime("%Y%m%d")
            topic_clean = args.topic.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("?", "")
            output_dir = Path("output") / f"Unit{int(args.unit)}" / "Custom"
            output_dir.mkdir(parents=True, exist_ok=True)

            if args.title:
                title_clean = args.title.replace(" ", "_")
                filename = f"{title_clean}_{date_str}.pdf"
            else:
                filename = f"{topic_clean}_{args.difficulty}_{args.num}problems_{date_str}.pdf"

            output_path = output_dir / filename

        # Create title
        if args.title:
            pdf_title = args.title
        else:
            pdf_title = f"Algebra 1 - Unit {int(args.unit)} - {args.topic} ({args.difficulty.capitalize()})"

        # Generate PDF
        pdf_gen.generate_worksheet(problems, str(output_path), title=pdf_title)

        print(f"\nWorksheet created successfully!")
        print(f"Location: {output_path.absolute()}")
        print(f"Title: {pdf_title}")
        print(f"Problems: {len(problems)}")
        print(f"Difficulty: {args.difficulty}")

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    build_from_args()
