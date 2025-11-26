"""
Test auto-discovery functionality for GUI.
"""
import sys
from pathlib import Path
import importlib.util


def discover_generators():
    """
    Discover all generator files in generators/K_8/ and generators/High_School/ directories.
    Returns dict: {subject_path: {topic_name: generator_class}}
    where subject_path is like "High School - Algebra" or "K-8 - Grade 5"
    """
    generators_by_subject = {}
    generators_base = Path("generators")

    if not generators_base.exists():
        return generators_by_subject

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

            generators_by_subject[full_path] = {}

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
                        # Create friendly name from file name
                        topic_name = gen_file.stem.replace('_generator', '').replace('_', ' ').title()
                        generators_by_subject[full_path][topic_name] = generator_class

                except Exception as e:
                    print(f"Warning: Failed to load {gen_file}: {e}")
                    continue

    return generators_by_subject


if __name__ == "__main__":
    print("Testing auto-discovery...")
    discovered = discover_generators()

    print(f"\n[OK] Discovered {len(discovered)} subjects/grades")

    total_topics = sum(len(topics) for topics in discovered.values())
    print(f"[OK] Found {total_topics} total topics")

    print("\nSubjects/Grades and topic counts:")
    for subject_name, topics in sorted(discovered.items()):
        print(f"  {subject_name}: {len(topics)} topics")

    print("\nFirst subject topics:")
    if discovered:
        first_subject = list(discovered.keys())[0]
        print(f"\n{first_subject}:")
        for topic_name in sorted(discovered[first_subject].keys())[:10]:
            print(f"  - {topic_name}")
        if len(discovered[first_subject]) > 10:
            print(f"  ... and {len(discovered[first_subject]) - 10} more")

    print("\n[OK] Auto-discovery test complete!")
