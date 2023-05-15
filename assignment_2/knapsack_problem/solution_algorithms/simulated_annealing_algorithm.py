import numpy as np
import random
from ._knapsack_types import Items, Solution, Solutions, Temperature, WeightLimit, Value, Bit


class SimulatedAnnealingAlgorithm:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:
        """The __init__ function is the constructor for a class.

        :param self: Represent the instance of the object itself
        :param items: Items: Store the items that are passed to the constructor
        :param weight_limit: WeightLimit: Set the weight limit of the backpack
        :return: Nothing
        """
        self.items: Items = items
        self.weight_limit: WeightLimit = weight_limit

    def generate_initial_solution(self) -> Solution:
        """The generate_initial_solution function generates a random solution.

        :param self: Access the attributes of the class
        :return: A solution that is a list of 0's and 1's
        """
        solution: Solution = []

        # generate the random genes and append to the solution
        for bit in range(len(self.items)):
            bit: Bit = random.choice([0, 1])
            solution.append(bit)

        while self.evaluate_solution_value(solution) == -1:
            for i, bit in enumerate(solution):
                if bit == 1:
                    solution[i] = 0
                    break

        return solution

    def evaluate_solution_value(self, solution: Solution) -> Value:
        """The evaluate_solution_value function takes a solution and returns the value of that solution.

        :param self: Refer to the object itself
        :param solution: Solution: Pass in the solution that we want to evaluate
        :return: The total value of the items in the solution
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

    def generate_solution_neighbours(self, solution: Solution) -> Solutions:
        """The generate_solution_neighbours function generates a fixed number of neighbours by flipping one bit at a time.

        :param self: Bind the method to an object
        :param solution: Solution: Create a copy of the solution
        :return: A list of neighbours
        """
        neighbours: Solutions = []

        # Generate a fixed number of neighbors by flipping one bit at a time
        for index in range(len(self.items)):
            new_solution: Solution = solution.copy()
            # flip the bit
            new_solution[index] = 1 - new_solution[index]
            neighbours.append(new_solution)

        return neighbours

    @staticmethod
    def accept(current_solution_value: Value, neighbour_value: Value, current_temperature: Temperature) -> bool:
        """The accept function is used to determine whether a new solution should be accepted.

        :param current_solution_value: Value: Compare the current solution value to the neighbour_value: value parameter
        :param neighbour_value: Value: Compare the current solution value to the neighbour_value
        :param current_temperature: Temperature: Determine the probability of accepting a solution
        :return: A boolean value
        """
        if neighbour_value > current_solution_value:
            return True

        delta = neighbour_value - current_solution_value
        return random.random() < np.exp(-delta / current_temperature)

    def run(self, current_temperature: Temperature = 100, cooling_schedule: float = 0.9995) -> tuple[int, Solution]:
        """The run function is the main function of the simulated annealing algorithm.
        It takes two parameters: current_temperature and cooling_schedule.
        The current temperature is a float value that represents how likely it is to accept a worse solution than the
        one we have now.
        The cooling schedule determines how much we decrease our temperature after each iteration, so that eventually,
        when it reaches 1 or below,
        we stop accepting worse solutions and return our best solution found so far.

        :param self: Refer to the object itself
        :param current_temperature: Temperature: Define the initial temperature of the system
        :param cooling_schedule: float: Determine how fast the temperature will cool down
        :return: A tuple of the solution value and the solution itself
        :doc-author: Trelent
        """
        current_solution: Solution = self.generate_initial_solution()
        current_solution_value: Value = self.evaluate_solution_value(current_solution)

        while True:
            neighbours: Solutions = self.generate_solution_neighbours(current_solution)
            changed: bool = False

            for neighbour in neighbours:
                neighbour_value = self.evaluate_solution_value(neighbour)

                if self.accept(current_solution_value, neighbour_value, current_temperature):
                    current_solution = neighbour
                    current_solution_value = neighbour_value
                    changed = True
                    break

            if not changed or current_temperature < 1:
                break

            current_temperature *= cooling_schedule

        return current_solution_value, current_solution
