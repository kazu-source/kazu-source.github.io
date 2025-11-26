"""
Auto-generate generator_registry.py for PyInstaller packaging.

This script scans all generator files and creates a registry with explicit imports.
This is necessary because PyInstaller cannot detect dynamic imports using importlib.
"""

from pathlib import Path
import sys
import importlib.util


def discover_all_generators():
    """
    Scan generators directory and return all generators with their metadata.
    Returns: dict of {subject_path: {topic_name: (module_path, class_name)}}
    """
    generators_by_subject = {}
    generators_base = Path("generators")

    if not generators_base.exists():
        print(f"Error: generators directory not found")
        return generators_by_subject

    # Find K-8 and High_School directories
    category_dirs = []
    for category in ['K_8', 'High_School']:
        category_path = generators_base / category
        if category_path.exists() and category_path.is_dir():
            category_dirs.append((category, category_path))

    for category_name, category_path in category_dirs:
        # Find all subject/grade directories
        subject_dirs = sorted([d for d in category_path.iterdir() if d.is_dir()])

        for subject_dir in subject_dirs:
            # Create display name
            category_display = category_name.replace('_', '-')
            subject_display = subject_dir.name.replace('_', ' ')
            full_path = f"{category_display} - {subject_display}"

            generators_by_subject[full_path] = {}

            # Find all generator files (both in root and Unit folders)
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
                    # Determine module path
                    if gen_file.parent.name.startswith('Unit_'):
                        module_name = f"generators.{category_name}.{subject_dir.name}.{gen_file.parent.name}.{gen_file.stem}"
                    else:
                        module_name = f"generators.{category_name}.{subject_dir.name}.{gen_file.stem}"

                    # Load module to find class name
                    spec = importlib.util.spec_from_file_location(module_name, gen_file)
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)

                    # Find the generator class
                    generator_class_name = None
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if (isinstance(attr, type) and
                            attr_name.endswith('Generator') and
                            attr_name != 'Generator' and
                            hasattr(attr, 'generate_worksheet')):
                            generator_class_name = attr_name
                            break

                    if generator_class_name:
                        # Create friendly name
                        topic_name = gen_file.stem.replace('_generator', '').replace('_', ' ').title()
                        generators_by_subject[full_path][topic_name] = (module_name, generator_class_name)
                        print(f"  Found: {full_path} - {topic_name}")

                except Exception as e:
                    print(f"  Warning: Failed to load {gen_file}: {e}")
                    continue

    return generators_by_subject


def generate_registry_file(generators_dict, output_file="generator_registry.py"):
    """
    Generate generator_registry.py with all imports and registry dict.
    """
    lines = []

    # Header
    lines.append('"""')
    lines.append('Auto-generated Generator Registry for PyInstaller')
    lines.append('')
    lines.append('This file explicitly imports all generator classes so PyInstaller')
    lines.append('can detect and include them in the executable.')
    lines.append('')
    lines.append('DO NOT EDIT MANUALLY - Run build_generator_registry.py to regenerate.')
    lines.append('"""')
    lines.append('')

    # Collect all unique imports
    import_statements = []
    registry_data = {}

    for subject_path, topics in sorted(generators_dict.items()):
        registry_data[subject_path] = {}

        for topic_name, (module_path, class_name) in sorted(topics.items()):
            import_stmt = f"from {module_path} import {class_name}"
            if import_stmt not in import_statements:
                import_statements.append(import_stmt)

            registry_data[subject_path][topic_name] = class_name

    # Write imports
    lines.append('# Generator imports')
    for imp in sorted(import_statements):
        lines.append(imp)

    lines.append('')
    lines.append('')
    lines.append('# Generator registry mapping')
    lines.append('# Structure: {subject_path: {topic_name: GeneratorClass}}')
    lines.append('GENERATOR_REGISTRY = {')

    # Write registry dictionary
    for subject_path, topics in sorted(registry_data.items()):
        lines.append(f'    "{subject_path}": {{')
        for topic_name, class_name in sorted(topics.items()):
            lines.append(f'        "{topic_name}": {class_name},')
        lines.append('    },')

    lines.append('}')
    lines.append('')

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\nGenerated {output_file} successfully!")
    print(f"Total subjects: {len(registry_data)}")
    print(f"Total generators: {sum(len(topics) for topics in registry_data.values())}")


if __name__ == "__main__":
    print("Scanning generators directory...")
    print()

    generators = discover_all_generators()

    if not generators:
        print("No generators found!")
        sys.exit(1)

    print()
    print("Generating registry file...")
    generate_registry_file(generators)
    print("Done!")
