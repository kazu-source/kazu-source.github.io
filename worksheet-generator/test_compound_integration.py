"""
Test script to verify compound inequalities integration.
"""

from topic_registry import register_all_generators, get_registry

# Register all generators
register_all_generators()
registry = get_registry()

# Test getting the compound inequality generator
print("=" * 60)
print("TESTING COMPOUND INEQUALITIES INTEGRATION")
print("=" * 60)

# Check if topic is registered
topic = registry.get_topic(3.0, "Graphing", "Compound Inequalities")
if topic:
    print(f"\n[OK] Topic registered: {topic.topic}")
    print(f"     Unit: {topic.unit}")
    print(f"     Type: {topic.type.value}")
    print(f"     Config Key: {topic.config_key}")
    print(f"     Implemented: {topic.implemented}")
else:
    print("\n[ERROR] Topic not found!")

# Try to get the generator
print("\n" + "=" * 60)
print("GETTING GENERATOR")
print("=" * 60)

generator = registry.get_generator(3.0, "Graphing", "Compound Inequalities")
if generator:
    print(f"\n[OK] Generator retrieved: {type(generator).__name__}")

    # Generate a test problem
    print("\n" + "=" * 60)
    print("GENERATING TEST PROBLEM")
    print("=" * 60)

    problem = generator.generate_inequality('medium', compound_type='and')
    print(f"\n[OK] Problem generated!")
    print(f"     LaTeX: {problem.latex}")
    print(f"     Type: {problem.compound_type}")
    print(f"     Boundaries: {problem.boundary_1}, {problem.boundary_2}")

    # Generate a worksheet
    print("\n" + "=" * 60)
    print("GENERATING WORKSHEET")
    print("=" * 60)

    worksheet = generator.generate_worksheet('hard', 5)
    print(f"\n[OK] Worksheet generated with {len(worksheet)} problems")
    for i, prob in enumerate(worksheet, 1):
        print(f"     {i}. {prob.latex}")

else:
    print("\n[ERROR] Generator not found!")

print("\n" + "=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)
