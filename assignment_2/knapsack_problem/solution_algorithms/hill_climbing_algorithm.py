from math import inf
from .knapsack_types import Items, WeightLimit, Solution, Bit, Value, Solutions
from random import choice

class HillClimbingAlgorithm:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:
        self.items: Items = items
        self.weight_limit: WeightLimit = weight_limit

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

    def generate_initial_solution(self):
        solution: Solution = []

        # generate the random genes and append to the solution
        for bit in range(len(self.items)):
            bit: Bit = choice([0, 1])
            solution.append(bit)
        
        while self.evalueate_solution_value(solution) == -1:
            for i, bit in enumerate(solution):
                if bit == 1:
                    solution[i] = 0
                    break

        return solution
    
    def generate_solution_neighbour(self, solution: Solution) -> Value:
        best_neighbour: Solution = None
        best_neighbour_value: Solution = -inf


        for i, bit in enumerate(solution):
            if not bit:
                new_solution: Solution = solution.copy()
                new_solution[i] = 1

                if self.evalueate_solution_value(new_solution) > best_neighbour_value:
                    best_neighbour = new_solution
                    best_neighbour_value = self.evalueate_solution_value(best_neighbour)
        
        return best_neighbour, best_neighbour_value
    
    def run(self):
        current_solution: Solution = self.generate_initial_solution()
        current_solution_value: Value = self.evalueate_solution_value(current_solution)

        while True:
            neighbour, neighbour_value = self.generate_solution_neighbour(current_solution)
            
            if neighbour_value > current_solution_value:
                current_solution = neighbour
                current_solution_value = neighbour_value
            else:
                break

        current_solution_items = [self.items[i].name for i in range(len(self.items)) if current_solution[i]]
        return current_solution_value, current_solution_items

