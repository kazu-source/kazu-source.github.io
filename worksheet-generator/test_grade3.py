from generator_registry import GENERATOR_REGISTRY

grade3 = GENERATOR_REGISTRY.get('K-8 - Grade 3', {})
print(f'Grade 3 has {len(grade3)} topics')
print('\nFirst 5 topics with module paths:')
for i, (topic, gen_class) in enumerate(list(grade3.items())[:5]):
    print(f'  {topic}: {gen_class.__module__}')
