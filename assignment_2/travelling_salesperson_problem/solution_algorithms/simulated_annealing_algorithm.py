import math
import random
from travelling_salesperson_types import City, Weight, Graph, Energy, Tour, List, Temperature


class SimulatedAnnealingAlgorithm:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        pass

    def is_tour_valid(self, tour: Tour) -> bool:
        start_city: City = tour[0]

        for city in tour:
            if city is not start_city and city not in self.graph[start_city]:
                return False
            start_city = city

        return True

    def generate_initial_tour(self) -> Tour:
        tour: List[City] = list(self.graph.keys())

        while not self.is_tour_valid(tour):
            random.shuffle(tour)

        return tour

    def evaluate_cost(self, possible_solution_tour: Tour) -> Energy:
        total_cost: Energy = 0

        # do something
        for i in range(len(possible_solution_tour) - 1):
            city_1: City = possible_solution_tour[i]
            city_2: City = possible_solution_tour[i + 1]

            total_cost += self.graph[city_1][city_2]

        return total_cost

    def generate_neighbour(self, current_tour: Tour) -> Tour:
        for i in range(len(current_tour) - 1):
            new_tour: Tour = current_tour.copy()
            new_tour[i], new_tour[i + 1] = new_tour[i + 1], new_tour[i]

            if self.is_tour_valid(new_tour):
                return new_tour

    def accept(self, current_cost, new_cost, temperature):
        if new_cost < current_cost:
            return True
        else:
            delta = new_cost - current_cost
            return random.random() < math.exp(-delta / temperature)

    def run(self, initial_temperature=1000, cooling_rate=0.99, threshold=0.1):
        current_tour = self.generate_initial_tour()
        current_cost = self.evaluate_cost(current_tour)

        temperature = initial_temperature
        while temperature > threshold:
            new_tour = self.neighbor(current_tour)
            new_cost = self.total_cost(new_tour)

            if self.accept(current_cost, new_cost, temperature):
                current_tour = new_tour
                current_cost = new_cost

            temperature *= cooling_rate

        return current_tour, current_cost
