from math import inf
from typing import Tuple, List, Any

from ._knapsack_types import Items, WeightLimit, Solution, Bit, Value, Solutions
from random import choice


class HillClimbingAlgorithm:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:

        self.items: Items = items
        self.weight_limit: WeightLimit = weight_limit

    def evaluate_solution_value(self, solution: Solution) -> Value:
        """The evaluate_solution_value function takes a solution and returns the total value of all items in the knapsack.
        If the total weight exceeds the weight limit, then it returns - 1.

        :param self: Represent the instance of the class
        :param solution: Solution: Pass the solution to be evaluated
        :return: The total value of the items in a solution
        """
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
        """The generate_initial_solution function generates a random solution.

        :param self: Access the attributes and methods of the class
        :return: A list of 0s and 1s
        """
        solution: Solution = []

        # generate the random genes and append to the solution
        for bit in range(len(self.items)):
            bit: Bit = choice([0, 1])
            solution.append(bit)

        while self.evaluate_solution_value(solution) == -1:
            for i, bit in enumerate(solution):
                if bit == 1:
                    solution[i] = 0
                    break

        return solution

    def generate_solution_neighbour(self, solution: Solution) -> tuple[list[int], int]:
        """The generate_solution_neighbour function takes a solution and returns the best neighbour of that solution.
        The best neighbour is defined as the one with the highest value, where value is calculated by evaluating
        the fitness function on a given solution.

        :param self: Refer to the object itself
        :param solution: Solution: Pass the solution to be evaluated
        :return: The best neighbour and its value
        :doc-author: Trelent
        """
        best_neighbour: Solution = []
        best_neighbour_value: Value = -inf

        for i, bit in enumerate(solution):
            if not bit:
                new_solution: Solution = solution.copy()
                new_solution[i] = 1

                if self.evaluate_solution_value(new_solution) > best_neighbour_value:
                    best_neighbour = new_solution
                    best_neighbour_value = self.evaluate_solution_value(best_neighbour)

        return best_neighbour, best_neighbour_value

    def run(self) -> tuple[int, list[Any]]:
        """The run function is the main function of this class. It generates an initial solution, evaluates its value and then
        generates a neighbour for it. If the neighbour has a higher value than the current solution, it becomes the new
        current_solution and we generate another neighbour for it. This process repeats until no better neighbours can be found.

        :param self: Access the instance variables of the class
        :return: A tuple of the value and items in the solution
        :doc-author: Trelent
        """
        current_solution: Solution = self.generate_initial_solution()
        current_solution_value: Value = self.evaluate_solution_value(current_solution)

        while True:
            neighbour, neighbour_value = self.generate_solution_neighbour(current_solution)

            if neighbour_value > current_solution_value:
                current_solution = neighbour
                current_solution_value = neighbour_value
            else:
                break

        current_solution_items = [self.items[i].name for i in range(len(self.items)) if current_solution[i]]
        return current_solution_value, current_solution_items
