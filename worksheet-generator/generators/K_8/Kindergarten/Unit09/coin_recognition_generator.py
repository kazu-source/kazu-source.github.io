"""
Coin Recognition Generator - Kindergarten Unit 9
Generates problems about recognizing coins (penny, nickel, dime, quarter)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CoinRecognitionGenerator:
    """Generates coin recognition problems."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        coin = random.choice(['penny', 'nickel', 'dime', 'quarter'])
        latex = f"\\text{{What coin is this? (shows a {coin})}}"
        solution = coin
        return Equation(latex=latex, solution=solution, steps=[coin], difficulty='easy')

    def _generate_medium(self) -> Equation:
        coins = {
            'penny': '1 cent',
            'nickel': '5 cents',
            'dime': '10 cents',
            'quarter': '25 cents'
        }
        coin = random.choice(list(coins.keys()))
        latex = f"\\text{{What is a {coin} worth?}}"
        solution = coins[coin]
        return Equation(latex=latex, solution=solution, steps=[coins[coin]], difficulty='medium')

    def _generate_hard(self) -> Equation:
        coin_values = {
            'penny': 1,
            'nickel': 5,
            'dime': 10,
            'quarter': 25
        }
        coin1, coin2 = random.sample(list(coin_values.keys()), 2)
        latex = f"\\text{{Which is worth more: a {coin1} or a {coin2}?}}"
        solution = coin1 if coin_values[coin1] > coin_values[coin2] else coin2
        return Equation(latex=latex, solution=solution, steps=["compare values"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        value = random.choice([1, 5, 10, 25])
        coins = {1: 'penny', 5: 'nickel', 10: 'dime', 25: 'quarter'}
        latex = f"\\text{{Which coin is worth {value} cents?}}"
        solution = coins[value]
        return Equation(latex=latex, solution=solution, steps=[coins[value]], difficulty='challenge')


def main():
    generator = CoinRecognitionGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
