"""
Generate K-2 Worksheets
For K-2, there are no difficulty levels - the skill itself defines the complexity.
"""
import os
import sys
from pathlib import Path
import importlib.util
from pdf_generator import PDFWorksheetGenerator
from multiprocessing import Process, Queue
import time
import argparse


def generate_single_worksheet_worker(generator_class, num_problems, file_path, title, include_answer_key, result_queue):
    """Worker function to generate a single worksheet in a separate process."""
    try:
        generator = generator_class()
        problems = generator.generate_worksheet(num_problems=num_problems)
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


def discover_generators(grade_path: Path, grade_name: str):
    """Discover all generators for a grade."""
    generators = []

    if not grade_path.exists():
        print(f"Error: {grade_name} directory not found at {grade_path}")
        return generators

    # Find all unit directories (Unit01, Unit02, etc.)
    unit_dirs = sorted([d for d in grade_path.iterdir() if d.is_dir() and d.name.startswith('Unit')])

    for unit_dir in unit_dirs:
        # Find all generator files in this unit
        generator_files = [f for f in unit_dir.glob('*_generator.py') if f.name != '__init__.py']

        for gen_file in generator_files:
            try:
                # Build module path
                relative_parts = gen_file.relative_to(Path("generators")).parts
                module_name = "generators." + ".".join(p.replace(".py", "") for p in relative_parts)

                spec = importlib.util.spec_from_file_location(module_name, gen_file)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                # Find the generator class
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
                    generator_name = gen_file.stem.replace('_generator', '').replace('_', ' ').title()
                    generators.append((unit_dir.name, generator_name, generator_class))

            except Exception as e:
                print(f"Warning: Failed to load {gen_file}: {e}")
                continue

    return generators


def sanitize_filename(text):
    """Convert text to safe filename."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        text = text.replace(char, '')
    return text.replace(' ', '_')


def generate_grade_worksheets(grade_name: str, grade_path: Path, output_dir: Path, num_problems: int = 8):
    """Generate all worksheets for a grade."""

    print(f"\nDiscovering {grade_name} generators...")
    generators = discover_generators(grade_path, grade_name)

    if not generators:
        print(f"No {grade_name} generators found!")
        return 0, 0

    print(f"Found {len(generators)} {grade_name} generators\n")
    print("=" * 70)
    print(f"GENERATING {grade_name.upper()} WORKSHEETS")
    print("=" * 70)
    print(f"Output directory: {output_dir}/")
    print(f"Problems per worksheet: {num_problems}")
    print("-" * 70 + "\n")

    successful = 0
    failed = []
    start_time = time.time()

    for i, (unit_name, generator_name, generator_class) in enumerate(generators, 1):
        worksheet_start = time.time()
        print(f"[{i}/{len(generators)}] {unit_name} - {generator_name}...", end=" ", flush=True)

        safe_name = sanitize_filename(generator_name)
        # No difficulty suffix for K-2
        filename = f"{grade_name}_{unit_name}_{safe_name}.pdf"
        file_path = output_dir / filename
        # No difficulty in title for K-2
        title = f"{grade_name} - {generator_name}"

        result_queue = Queue()
        process = Process(
            target=generate_single_worksheet_worker,
            args=(generator_class, num_problems, file_path, title, True, result_queue)
        )

        process.start()
        process.join(timeout=6.0)

        elapsed = time.time() - worksheet_start

        if process.is_alive():
            process.terminate()
            process.join()
            print(f"[TIMEOUT] ({elapsed:.1f}s)")
            failed.append((generator_name, "Timeout"))
        else:
            if not result_queue.empty():
                status, error = result_queue.get()
                if status == "success":
                    print(f"[OK] {filename} ({elapsed:.1f}s)")
                    successful += 1
                else:
                    error_msg = str(error)[:50]
                    print(f"[FAIL] {error_msg} ({elapsed:.1f}s)")
                    failed.append((generator_name, error_msg))
            else:
                print(f"[FAIL] No result ({elapsed:.1f}s)")
                failed.append((generator_name, "No result"))

    elapsed = time.time() - start_time
    print(f"\n{grade_name}: {successful}/{len(generators)} successful ({elapsed:.1f}s)")

    if failed:
        print(f"Failed worksheets for {grade_name}:")
        for name, error in failed:
            print(f"  - {name}: {error}")

    return successful, len(generators)


def main():
    """Generate K-2 worksheets."""
    parser = argparse.ArgumentParser(description='Generate K-2 worksheets (no difficulty levels)')
    parser.add_argument('--grade', '-g', choices=['kindergarten', 'grade1', 'grade2', 'all'],
                       default='all', help='Which grade to generate (default: all)')
    parser.add_argument('--output', '-o', default='worksheets',
                       help='Output directory (default: worksheets)')
    parser.add_argument('--problems', '-p', type=int, default=8,
                       help='Number of problems per worksheet (default: 8)')

    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    grades = {
        'kindergarten': ('Kindergarten', Path('generators/K_8/Kindergarten')),
        'grade1': ('Grade_1', Path('generators/K_8/Grade_1')),
        'grade2': ('Grade_2', Path('generators/K_8/Grade_2')),
    }

    total_successful = 0
    total_count = 0
    start_time = time.time()

    if args.grade == 'all':
        grades_to_process = grades.keys()
    else:
        grades_to_process = [args.grade]

    for grade_key in grades_to_process:
        grade_name, grade_path = grades[grade_key]
        successful, count = generate_grade_worksheets(
            grade_name, grade_path, output_dir, args.problems
        )
        total_successful += successful
        total_count += count

    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print(f"Total: {total_successful}/{total_count} worksheets")
    print(f"Time elapsed: {elapsed:.1f} seconds")
    print(f"Output directory: {output_dir}/")


if __name__ == "__main__":
    main()
