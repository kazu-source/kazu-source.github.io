"""
Flexible Batch Worksheet Generator
Automatically discovers and generates worksheets from all generators in generators/chapter##/ directories.

Usage:
    python batch_generate_worksheets.py --difficulty easy --output easy_worksheets
    python batch_generate_worksheets.py --difficulty medium --output medium_worksheets
    python batch_generate_worksheets.py --difficulty hard --chapters 1 2 3
    python batch_generate_worksheets.py --all-difficulties --output all_worksheets
"""

import os
import sys
import time
import argparse
import importlib.util
from pathlib import Path
from typing import List, Tuple, Optional
from pdf_generator import PDFWorksheetGenerator
import multiprocessing
from multiprocessing import Process, Queue
import signal


def generate_single_worksheet_worker(generator_class, difficulty, num_problems, file_path, title, include_answer_key, result_queue):
    """Worker function to generate a single worksheet in a separate process."""
    try:
        # Instantiate generator
        generator = generator_class()

        # Generate problems
        problems = generator.generate_worksheet(difficulty, num_problems)

        # Generate PDF
        pdf_gen = PDFWorksheetGenerator()
        pdf_gen.generate_worksheet(
            problems,
            str(file_path),
            title=title,
            include_answer_key=include_answer_key
        )

        result_queue.put(("success", None))
    except Exception as e:
        result_queue.put(("error", str(e)))


def discover_generators(chapter_filter: Optional[List[int]] = None) -> List[Tuple[str, str, type]]:
    """
    Automatically discover all generator files in generators/K_8/ and generators/High_School/ directories.

    Args:
        chapter_filter: Optional list (deprecated, kept for backwards compatibility)

    Returns:
        List of tuples: (subject_path, generator_name, generator_class)
        where subject_path is like "High School - Algebra" or "K-8 - Grade 5"
    """
    generators = []
    generators_base = Path("generators")

    if not generators_base.exists():
        print(f"Error: generators directory not found at {generators_base}")
        return generators

    # Find K-8 and High_School directories
    category_dirs = []
    for category in ['K_8', 'High_School']:
        category_path = generators_base / category
        if category_path.exists() and category_path.is_dir():
            category_dirs.append((category, category_path))

    for category_name, category_path in category_dirs:
        # Find all subject/grade directories within this category
        subject_dirs = sorted([d for d in category_path.iterdir() if d.is_dir()])

        for subject_dir in subject_dirs:
            # Create display name like "High School - Algebra" or "K-8 - Grade 5"
            category_display = category_name.replace('_', '-')
            subject_display = subject_dir.name.replace('_', ' ')
            full_path = f"{category_display} - {subject_display}"

            # Find all generator files in this subject/grade (both in root and Unit folders)
            generator_files = []

            # Check for generators directly in subject folder
            generator_files.extend([f for f in subject_dir.glob('*_generator.py')
                                   if f.name != '__init__.py'])

            # Check for generators in Unit subfolders
            unit_dirs = [d for d in subject_dir.iterdir()
                       if d.is_dir() and d.name.startswith('Unit_')]
            for unit_dir in unit_dirs:
                generator_files.extend([f for f in unit_dir.glob('*_generator.py')
                                      if f.name != '__init__.py'])

            for gen_file in generator_files:
                try:
                    # Determine module path based on whether it's in a Unit folder
                    if gen_file.parent.name.startswith('Unit_'):
                        # In a unit folder
                        module_name = f"generators.{category_name}.{subject_dir.name}.{gen_file.parent.name}.{gen_file.stem}"
                    else:
                        # Directly in subject folder
                        module_name = f"generators.{category_name}.{subject_dir.name}.{gen_file.stem}"

                    spec = importlib.util.spec_from_file_location(module_name, gen_file)
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)

                    # Find the generator class (should end with 'Generator')
                    generator_class = None
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if (isinstance(attr, type) and
                            attr_name.endswith('Generator') and
                            attr_name != 'Generator' and
                            hasattr(attr, 'generate_worksheet')):
                            generator_class = attr
                            break

                    if generator_class:
                        # Create a friendly name from the file name
                        generator_name = gen_file.stem.replace('_generator', '').replace('_', ' ').title()
                        generators.append((full_path, generator_name, generator_class))

                except Exception as e:
                    print(f"Warning: Failed to load {gen_file}: {e}")
                    continue

    return generators


def sanitize_filename(text: str) -> str:
    """Convert text to safe filename."""
    # Replace invalid filename characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        text = text.replace(char, '')
    return text.replace(' ', '_')


def generate_worksheets(
    difficulty: str,
    output_dir: str,
    num_problems: int = 8,
    chapter_filter: Optional[List[int]] = None,
    include_answer_key: bool = True
) -> Tuple[int, int]:
    """
    Generate worksheets for all discovered generators.

    Args:
        difficulty: Difficulty level ('easy', 'medium', 'hard', 'challenge')
        output_dir: Output directory for PDFs
        num_problems: Number of problems per worksheet
        chapter_filter: Optional list of chapter numbers to include
        include_answer_key: Whether to include answer keys

    Returns:
        Tuple of (successful_count, total_count)
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Discover all generators
    print("Discovering generators...")
    generators = discover_generators(chapter_filter)

    if not generators:
        print("No generators found!")
        return 0, 0

    print(f"Found {len(generators)} generators")

    # Initialize PDF generator
    pdf_gen = PDFWorksheetGenerator()

    # Statistics
    successful = 0
    failed = []
    start_time = time.time()

    print("\n" + "=" * 70)
    print(f"GENERATING {difficulty.upper()} WORKSHEETS")
    print("=" * 70)
    print(f"Output directory: {output_dir}")
    print(f"Problems per worksheet: {num_problems}")
    print(f"Include answer key: {include_answer_key}")
    print("-" * 70 + "\n")

    for i, (subject_path, name, generator_class) in enumerate(generators, 1):
        worksheet_start = time.time()
        print(f"[{i}/{len(generators)}] {subject_path} - {name}...", end=" ", flush=True)

        # Create filename with subject prefix to prevent duplicates
        # Convert "High-School - Algebra" to "HS_Alg" or "K-8 - Grade 5" to "K8_Gr5"
        parts = subject_path.split(' - ')
        if len(parts) == 2:
            category_part = parts[0].replace('High-School', 'HS').replace('K-8', 'K8')
            subject_part = parts[1].replace('Grade ', 'Gr').replace(' ', '')[:6]  # Limit to 6 chars
            prefix = f"{category_part}_{subject_part}"
        else:
            prefix = sanitize_filename(subject_path)[:10]

        safe_name = sanitize_filename(name)
        filename = f"{prefix}_{safe_name}_{difficulty}.pdf"
        file_path = output_path / filename
        # Title on PDF does NOT include subject prefix
        title = f"{name} - {difficulty.capitalize()}"

        # Create queue for result communication
        result_queue = Queue()

        # Create and start process with timeout
        process = Process(
            target=generate_single_worksheet_worker,
            args=(generator_class, difficulty, num_problems, file_path, title, include_answer_key, result_queue)
        )

        process.start()
        process.join(timeout=6.0)  # Wait max 6 seconds

        elapsed = time.time() - worksheet_start

        if process.is_alive():
            # Process timed out
            process.terminate()
            process.join()  # Clean up
            print(f"[TIMEOUT] Exceeded 6s limit ({elapsed:.1f}s)")
            failed.append((name, f"Generation timed out after {elapsed:.1f}s"))
        else:
            # Process completed
            if not result_queue.empty():
                status, error = result_queue.get()
                if status == "success":
                    print(f"[OK] {filename} ({elapsed:.1f}s)")
                    successful += 1
                else:
                    error_msg = str(error)[:50]
                    print(f"[FAIL] Error: {error_msg} ({elapsed:.1f}s)")
                    failed.append((name, error_msg))
            else:
                print(f"[FAIL] No result returned ({elapsed:.1f}s)")
                failed.append((name, "Process completed but returned no result"))

    # Print summary
    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print(f"Successful: {successful}/{len(generators)}")
    print(f"Failed: {len(failed)}/{len(generators)}")
    print(f"Time elapsed: {elapsed:.1f} seconds")
    print(f"Output directory: {output_dir}/")

    if failed:
        print("\nFailed worksheets:")
        for name, error in failed[:10]:  # Show first 10
            print(f"  - {name}: {error[:60]}")
        if len(failed) > 10:
            print(f"  ... and {len(failed) - 10} more")

    return successful, len(generators)


def main():
    """Main entry point with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description='Batch generate worksheets from all discovered generators',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate all easy worksheets:
    python batch_generate_worksheets.py --difficulty easy --output easy_worksheets

  Generate medium worksheets for chapters 1-3 only:
    python batch_generate_worksheets.py --difficulty medium --chapters 1 2 3

  Generate all difficulty levels:
    python batch_generate_worksheets.py --all-difficulties --output all_worksheets

  Generate hard worksheets with 12 problems each:
    python batch_generate_worksheets.py --difficulty hard --problems 12
        """
    )

    parser.add_argument(
        '--difficulty', '-d',
        choices=['easy', 'medium', 'hard', 'challenge'],
        help='Difficulty level to generate'
    )

    parser.add_argument(
        '--all-difficulties', '-a',
        action='store_true',
        help='Generate all difficulty levels'
    )

    parser.add_argument(
        '--output', '-o',
        default='generated_worksheets',
        help='Output directory (default: generated_worksheets)'
    )

    parser.add_argument(
        '--problems', '-p',
        type=int,
        default=8,
        help='Number of problems per worksheet (default: 8)'
    )

    parser.add_argument(
        '--chapters', '-c',
        type=int,
        nargs='+',
        help='Filter by chapter numbers (e.g., --chapters 1 2 3)'
    )

    parser.add_argument(
        '--no-answer-key',
        action='store_true',
        help='Exclude answer keys from worksheets'
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.difficulty and not args.all_difficulties:
        parser.error("Must specify either --difficulty or --all-difficulties")

    if args.difficulty and args.all_difficulties:
        parser.error("Cannot specify both --difficulty and --all-difficulties")

    # Generate worksheets
    if args.all_difficulties:
        difficulties = ['easy', 'medium', 'hard', 'challenge']
        total_successful = 0
        total_count = 0

        for difficulty in difficulties:
            output_dir = f"{args.output}/{difficulty}_worksheets"
            print(f"\n{'='*70}")
            print(f"GENERATING {difficulty.upper()} LEVEL")
            print(f"{'='*70}\n")

            successful, count = generate_worksheets(
                difficulty=difficulty,
                output_dir=output_dir,
                num_problems=args.problems,
                chapter_filter=args.chapters,
                include_answer_key=not args.no_answer_key
            )

            total_successful += successful
            total_count += count

        print(f"\n{'='*70}")
        print("ALL DIFFICULTIES COMPLETE")
        print(f"{'='*70}")
        print(f"Total worksheets: {total_successful}/{total_count * len(difficulties)}")

    else:
        generate_worksheets(
            difficulty=args.difficulty,
            output_dir=args.output,
            num_problems=args.problems,
            chapter_filter=args.chapters,
            include_answer_key=not args.no_answer_key
        )


if __name__ == "__main__":
    multiprocessing.freeze_support()  # Required for Windows
    main()
