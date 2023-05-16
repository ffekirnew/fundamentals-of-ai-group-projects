import heapq
import random
import math
from math import inf


class SimulatedAnnealingAlgorithm:
    def __init__(self, map, cities):
        self.map = map
        self.cities = cities
        self.distances = self.all_distances()

    def dijkstra(self, start):
        graph = self.map

        distances = {city: float('inf') for city in graph}
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, current_city = heapq.heappop(queue)

            if current_distance > distances[current_city]:
                continue

            for neighbor, weight in graph[current_city]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

    def all_distances(self):
        all_distances = {}
        for city in self.cities:
            distances = self.dijkstra(city)
            all_distances[city] = distances

        return all_distances

    def generate_initial_solution(self):
        return random.sample(self.cities, len(self.cities))

    def distance(self, city1, city2):
        return self.distances[city1][city2]

    def calculate_total_distance(self, route):
        total = 0
        for i in range(len(route) - 1):
            city1 = route[i]
            city2 = route[(i + 1) % len(route)]
            total += self.distance(city1, city2)
        return total

    def generate_solution_neighbor(self, solution):
        new_solution = solution.copy()

        index1, index2 = random.randint(0, len(self.cities) - 1), random.randint(0, len(self.cities) - 1)
        new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]

        return new_solution

    def path_between_cities(self, start, end):
        queue = [(0, start, [])]
        visited = set()

        while queue:
            cost, city, path = heapq.heappop(queue)

            if city == end:
                return path + [city]

            if city in visited:
                continue

            visited.add(city)

            for neighbor, edge_cost in self.map[city]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [city]))

        return None

    def acceptance_probability(self,current_cost,new_cost, temperature):
        delta = new_cost - current_cost

        if delta < 0:
            return 1.0
        return math.exp(-delta / temperature)

    def run(self):
        current_solution = self.generate_initial_solution()
        best_solution = current_solution
        current_cost = self.calculate_total_distance(current_solution)
        best_cost = current_cost
        temperature = 1.0
        max_iterations=10000
        cooling_rate=0.95

        for iteration in range(max_iterations):
            new_solution = self.generate_solution_neighbor(current_solution)
            new_cost = self.calculate_total_distance(new_solution)

            if self.acceptance_probability(current_cost,new_cost,temperature) > random.random():
                current_solution = new_solution
                current_cost = new_cost

            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost

            temperature *= cooling_rate

        return best_solution, best_cost

if __name__ == "__main__":
    graph = {
        'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
        'Zerind': [('Arad', 75), ('Oradea', 71)],
        'Timisoara': [('Arad', 118), ('Lugoj', 111)],
        'Sibiu': [('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Oradea', 151)],
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
        'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
        'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
        'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
        'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
        'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
        'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138), ('Dobreta', 120)],
        'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
        'Giurgiu': [('Bucharest', 90)],
        'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
        'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
        'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
        'Iasi': [('Vaslui', 92), ('Neamt', 87)],
        'Neamt': [('Iasi', 87)],
        'Eforie': [('Hirsova', 86)]
    }
    cities = list(graph.keys())

    solver = SimulatedAnnealingAlgorithm(graph, cities)
    print(solver.run())
