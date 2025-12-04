"""
Systems Word Problems Rate Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SystemsWordProblemsRateGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        speed1 = random.randint(40, 60)
        speed2 = random.randint(50, 70)
        time = random.randint(2, 4)
        total_distance = (speed1 + speed2) * time

        latex = f"\\text{{Two cars travel opposite directions. Speed {speed1} mph and {speed2} mph. {total_distance} mi apart after how long?}}"
        solution = f"{time} \\text{{ hours}}"
        steps = [f"Combined speed: {speed1} + {speed2} = {speed1 + speed2} mph", f"Distance = Rate × Time", f"{total_distance} = {speed1 + speed2} × t", f"t = {time} hours"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        speed_walk = random.randint(3, 5)
        speed_bike = random.randint(12, 18)
        total_time = random.randint(3, 6)
        time_walk = random.randint(1, total_time - 1)
        time_bike = total_time - time_walk
        distance = speed_walk * time_walk + speed_bike * time_bike

        latex = f"\\text{{Traveled {distance} miles in {total_time} hours. Walk {speed_walk} mph, bike {speed_bike} mph. Time each?}}"
        solution = f"Walk: {time_walk} hrs, Bike: {time_bike} hrs"
        steps = [f"w + b = {total_time}", f"{speed_walk}w + {speed_bike}b = {distance}", f"w = {time_walk}, b = {time_bike}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        speed_current = random.randint(2, 5)
        speed_boat = random.randint(15, 25)
        downstream = speed_boat + speed_current
        upstream = speed_boat - speed_current

        latex = f"\\text{{Boat speed {speed_boat} mph, current {speed_current} mph. Find downstream and upstream speeds.}}"
        solution = f"Downstream: {downstream} mph, Upstream: {upstream} mph"
        steps = [f"Downstream: boat + current = {downstream}", f"Upstream: boat - current = {upstream}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        speed_a = random.randint(50, 70)
        speed_b = random.randint(60, 80)
        head_start = random.randint(1, 3)

        # When does B catch up to A?
        # distance_a = speed_a * (t + head_start)
        # distance_b = speed_b * t
        # Set equal: speed_a * (t + head_start) = speed_b * t
        # speed_a * t + speed_a * head_start = speed_b * t
        # speed_a * head_start = (speed_b - speed_a) * t
        time_catchup = (speed_a * head_start) / (speed_b - speed_a)

        latex = f"\\text{{Car A goes {speed_a} mph with {head_start} hour head start. Car B goes {speed_b} mph. When does B catch A?}}"
        solution = f"{time_catchup:.1f} \\text{{ hours}}"
        steps = [f"A distance: {speed_a}(t + {head_start})", f"B distance: {speed_b}t", f"Set equal and solve", f"t = {time_catchup:.1f} hours"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SystemsWordProblemsRateGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
