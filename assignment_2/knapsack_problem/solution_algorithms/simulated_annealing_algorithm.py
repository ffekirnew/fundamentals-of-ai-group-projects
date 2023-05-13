import math
import random
from .knapsack_types import Items, Solution, Solutions, Temperature, WeightLimit, Value, Bit


class SimulatedAnnealingAlgorithm:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:
        self.items: Items = items
        self.weight_limit: WeightLimit = weight_limit
    
    def generate_initial_solution(self):
        solution: Solution = []

        # generate the random genes and append to the solution
        for bit in range(len(self.items)):
            bit: Bit = random.choice([0, 1])
            solution.append(bit)
        
        while self.evalueate_solution_value(solution) == -1:
            for i, bit in enumerate(solution):
                if bit == 1:
                    solution[i] = 0
                    break

        return solution

    def evalueate_solution_value(self, solution: Solution) -> Value:
        total_weight: int = 0
        total_value: Value = 0

        for index, bit in enumerate(solution):
            if bit == 1:
                total_weight += self.items[index].weight
                if total_weight > self.weight_limit:
                    # solution is disqualified
                    return -1

                total_value += self.items[index].value

        return total_value

    def generate_solution_neighbours(self, solution: Solution) -> Solutions:
        neighbours: Solutions = []

        # Generate a fixed number of neighbors by swapping two bits in the solution
        for i in range(10):
            new_solution: Solution = solution.copy()

            # Select two random indices in the solution
            index1, index2 = random.sample(range(len(solution)), 2)

            # Swap the values at those indices
            new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]

            neighbours.append(new_solution)

        return neighbours

    def accept(self, current_solution_value: Value, neighbour_value: Value, current_temperature: Temperature) -> bool:
        if neighbour_value > current_solution_value:
            return True
        
        delta = neighbour_value - current_solution_value
        print(-delta, current_temperature)
        return random.random() < math.exp(-delta / current_temperature)


    def run(self, current_temperature: Temperature = 100, cooling_schedule: float = 0.9) -> tuple[int, Solution]:
        current_solution: Solution = self.generate_initial_solution()
        current_solution_value: Value = self.evalueate_solution_value(current_solution)

        while True:
            neighbours: Solutions = self.generate_solution_neighbours(current_solution)
            changed: bool = False

            for neighbour in neighbours:
                neighbour_value = self.evalueate_solution_value(neighbour)

                if self.accept(current_solution_value, neighbour_value, current_temperature):
                    current_solution = neighbour
                    current_solution_value = neighbour_value
                    changed = True
                    break
            
            if not changed or current_temperature < 1:
                break

            current_temperature *= cooling_schedule
        
        return current_solution_value, current_solution
                

