"""
Generate all Grade 3 Easy Worksheets
"""
import os
import sys
from pathlib import Path
import importlib.util
from pdf_generator import PDFWorksheetGenerator
from multiprocessing import Process, Queue
import time

def generate_single_worksheet_worker(generator_class, difficulty, num_problems, file_path, title, include_answer_key, result_queue):
    """Worker function to generate a single worksheet in a separate process."""
    try:
        generator = generator_class()
        problems = generator.generate_worksheet(difficulty, num_problems)
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

def discover_grade3_generators():
    """Discover all Grade 3 generators."""
    generators = []
    grade3_path = Path("generators/K_8/Grade_3")

    if not grade3_path.exists():
        print(f"Error: Grade 3 directory not found at {grade3_path}")
        return generators

    # Find all unit directories
    unit_dirs = sorted([d for d in grade3_path.iterdir() if d.is_dir() and d.name.startswith('Unit')])

    for unit_dir in unit_dirs:
        # Find all generator files in this unit
        generator_files = [f for f in unit_dir.glob('*_generator.py') if f.name != '__init__.py']

        for gen_file in generator_files:
            try:
                module_name = f"generators.K_8.Grade_3.{unit_dir.name}.{gen_file.stem}"
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

def main():
    """Generate all Grade 3 easy worksheets."""
    output_dir = Path("easy_worksheets")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Discovering Grade 3 generators...")
    generators = discover_grade3_generators()

    if not generators:
        print("No Grade 3 generators found!")
        return

    print(f"Found {len(generators)} Grade 3 generators\n")
    print("=" * 70)
    print("GENERATING GRADE 3 EASY WORKSHEETS")
    print("=" * 70)
    print(f"Output directory: easy_worksheets/")
    print(f"Problems per worksheet: 8")
    print("-" * 70 + "\n")

    successful = 0
    failed = []
    start_time = time.time()

    for i, (unit_name, generator_name, generator_class) in enumerate(generators, 1):
        worksheet_start = time.time()
        print(f"[{i}/{len(generators)}] {unit_name} - {generator_name}...", end=" ", flush=True)

        safe_name = sanitize_filename(generator_name)
        filename = f"Grade3_{unit_name}_{safe_name}_easy.pdf"
        file_path = output_dir / filename
        title = f"Grade 3 - {generator_name} - Easy"

        result_queue = Queue()
        process = Process(
            target=generate_single_worksheet_worker,
            args=(generator_class, 'easy', 8, file_path, title, True, result_queue)
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
    print("\n" + "=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print(f"Successful: {successful}/{len(generators)}")
    print(f"Failed: {len(failed)}/{len(generators)}")
    print(f"Time elapsed: {elapsed:.1f} seconds")
    print(f"Output directory: easy_worksheets/")

    if failed:
        print("\nFailed worksheets:")
        for name, error in failed:
            print(f"  - {name}: {error}")

if __name__ == "__main__":
    main()
