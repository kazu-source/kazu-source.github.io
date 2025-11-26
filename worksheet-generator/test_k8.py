from generator_registry import GENERATOR_REGISTRY

print("K-8 Grade topic counts:")
for grade_name in sorted(GENERATOR_REGISTRY.keys()):
    if grade_name.startswith('K-8'):
        topic_count = len(GENERATOR_REGISTRY[grade_name])
        print(f"  {grade_name}: {topic_count} topics")
        if topic_count > 0:
            print(f"    First topic: {list(GENERATOR_REGISTRY[grade_name].keys())[0]}")
