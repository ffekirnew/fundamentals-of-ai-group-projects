import numpy as np
import random
from ._knapsack_types import Items, Solution, Solutions, Temperature, WeightLimit, Value, Bit


class SimulatedAnnealingAlgorithm:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:
        self._items: Items = items
        self._weight_limit: WeightLimit = weight_limit

    def _generate_initial_solution(self) -> Solution:
        solution: Solution = []

        for _ in range(len(self._items)):
            bit: Bit = random.choice([0, 1])
            solution.append(bit)

        while self._evaluate_solution_value(solution) == -1:
            for i, bit in enumerate(solution):
                if bit == 1:
                    solution[i] = 0
                    break

        return solution

    def _evaluate_solution_value(self, solution: Solution) -> Value:
        total_weight: int = 0
        total_value: Value = 0

        for index, bit in enumerate(solution):
            if bit == 1:
                total_weight += self._items[index].weight
                if total_weight > self._weight_limit:
                    return -1

                total_value += self._items[index].value

        return total_value

    def _generate_solution_neighbours(self, solution: Solution) -> Solutions:
        neighbours: Solutions = []

        for index in range(len(self._items)):
            new_solution: Solution = solution.copy()
            new_solution[index] = 1 - new_solution[index]
            neighbours.append(new_solution)

        return neighbours

    @staticmethod
    def _accept(current_solution_value: Value, neighbour_value: Value, current_temperature: Temperature) -> bool:
        if neighbour_value > current_solution_value:
            return True

        delta = neighbour_value - current_solution_value
        return random.random() < np.exp(-delta / current_temperature)

    def run(self, current_temperature: Temperature = 100, cooling_schedule: float = 0.9995) -> tuple[int, Solution]:
        current_solution: Solution = self._generate_initial_solution()
        current_solution_value: Value = self._evaluate_solution_value(current_solution)

        while True:
            neighbours: Solutions = self._generate_solution_neighbours(current_solution)
            changed: bool = False

            for neighbour in neighbours:
                neighbour_value = self._evaluate_solution_value(neighbour)

                if self._accept(current_solution_value, neighbour_value, current_temperature):
                    current_solution = neighbour
                    current_solution_value = neighbour_value
                    changed = True
                    break

            if not changed or current_temperature < 1:
                break

            current_temperature *= cooling_schedule

        return current_solution_value, current_solution