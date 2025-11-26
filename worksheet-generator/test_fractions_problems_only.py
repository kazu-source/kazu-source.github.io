"""Test just problem generation"""
import time
from generators.K_8.Grade_3.Unit06.comparing_fractions_generator import ComparingFractionsGenerator

print("Creating generator...")
gen = ComparingFractionsGenerator()

print("Generating problems...")
start = time.time()
problems = gen.generate_worksheet('easy', 8)
gen_time = time.time() - start
print(f"Generated {len(problems)} problems in {gen_time:.4f}s")

for i, p in enumerate(problems, 1):
    print(f"{i}. {p.latex[:80]}...")
    print(f"   Solution: {p.solution[:80]}...")
