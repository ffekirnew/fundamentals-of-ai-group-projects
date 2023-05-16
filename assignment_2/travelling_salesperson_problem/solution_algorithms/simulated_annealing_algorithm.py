import random
import numpy as np
from _travelling_salesperson_types import romanian_map


class SimulatedAnnealingTSP:
    def __init__(self, cities):
        self.cities = cities

    @staticmethod
    def distance(city1, city2):
        return romanian_map[city1][city2]

    def total_distance(self, route):
        total = 0
        for i in range(len(route) - 1):
            city1 = route[i]
            city2 = route[(i + 1) % len(route)]
            total += self.distance(city1, city2)
        return total

    def generate_initial_solution(self):
        cities = self.cities
        num_cities = len(cities)

        # Randomly select a starting city
        start_city = random.choice(cities)

        # Initialize the visited cities and the solution
        visited_cities = {start_city}
        solution = [start_city]

        while len(visited_cities) < num_cities:
            # Find the nearest unvisited city to the current solution
            nearest_neighbor = None
            nearest_distance = float('inf')

            for city in visited_cities:
                for neighbor in cities:
                    if neighbor not in visited_cities:
                        distance = self.distance(city, neighbor)
                        if distance < nearest_distance:
                            nearest_distance = distance
                            nearest_neighbor = neighbor

            # Find the best position to insert the nearest neighbor in the solution
            best_position = None
            best_distance_increase = float('inf')

            for i in range(len(solution)):
                current_distance = self.distance(solution[i], solution[(i + 1) % len(solution)])
                new_distance = (
                        self.distance(solution[i], nearest_neighbor)
                        + self.distance(nearest_neighbor, solution[(i + 1) % len(solution)])
                )
                distance_increase = new_distance - current_distance

                if distance_increase < best_distance_increase:
                    best_distance_increase = distance_increase
                    best_position = i

            # Insert the nearest neighbor at the best position in the solution
            solution.insert(best_position + 1, nearest_neighbor)
            visited_cities.add(nearest_neighbor)

        return solution

    @staticmethod
    def generate_neighbor(route):
        # Apply 2-opt: Reverse a random segment of the route
        new_route = route.copy()
        i = random.randint(0, len(new_route) - 1)
        j = random.randint(0, len(new_route) - 1)
        i, j = min(i, j), max(i, j)
        new_route[i:j+1] = reversed(new_route[i:j+1])
        return new_route

    @staticmethod
    def accept(current_distance, new_distance, temperature):
        if new_distance < current_distance:
            return True

        delta = new_distance - current_distance
        acceptance_probability = np.exp(-delta / temperature)
        return random.random() < acceptance_probability

    def solve(self, initial_temperature, cooling_rate, iterations):
        # Initialize the current solution as a random permutation of cities
        current_solution = self.generate_initial_solution()
        print(current_solution)
        current_distance = self.total_distance(current_solution)

        # Set the initial temperature
        temperature = initial_temperature

        for _ in range(iterations):
            # Generate a new neighbor solution
            new_solution = self.generate_neighbor(current_solution)
            new_distance = self.total_distance(new_solution)

            # Decide whether to accept the new solution
            if self.accept(current_distance, new_distance, temperature):
                current_solution = new_solution
                current_distance = new_distance

            # Cool down the temperature
            temperature *= cooling_rate

        return current_solution, current_distance

if __name__ == "__main__":
    cities = ['Arad', 'Zerind', 'Oradea', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia',
              'Drobeta', 'Craiova', 'Rimnicu Vilcea', 'Fagaras', 'Pitesti', 'Bucharest']

    solver = SimulatedAnnealingTSP(cities)
    route, distance = solver.solve(initial_temperature=1000, cooling_rate=0.99, iterations=10000)

    print("Best route:", route)
    print("Total distance:", distance)