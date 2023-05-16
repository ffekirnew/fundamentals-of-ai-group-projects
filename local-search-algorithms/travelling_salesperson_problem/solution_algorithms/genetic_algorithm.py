import math
import random
import heapq


class GeneticAlgorithm:
    def __init__(self, map, cities):
        self.map = map
        self.cities = cities
        self.distances = self.all_distances()
        self.chromosome_length = len(cities)

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

    def generate_individual(self):
        return random.sample(self.cities, len(self.cities))

    def generate_initial_population(self, population_size):
        population = []

        for _ in range(population_size):
            population.append(self.generate_individual())

        return population

    def distance(self, city1, city2):
        return self.distances[city1][city2]

    def fitness(self, individual):
        total = 0
        for i in range(len(individual) - 1):
            city1 = individual[i]
            city2 = individual[i + 1]
            total += self.distance(city1, city2)
        return total

    def calculate_population_probability(self, population):
        total_fitness = sum(self.fitness(individual) for individual in population)

        probability_of_population = []

        for individual in population:
            fitness = total_fitness - self.fitness(individual)
            probability_of_population.append(fitness / total_fitness)

        return probability_of_population

    def select_parents(self, population, number_of_selections):
        possible_probabilities = self.calculate_population_probability(population)

        slices = []
        total: int = 0

        for i in range(len(population)):
            slices.append([i, total, total + possible_probabilities[i]])
            total += possible_probabilities[i]

        selections = []
        for i in range(number_of_selections):
            spin: float = random.random()
            selections.append(
                [population[section[0]] for section in slices if section[1] < spin <= section[2]][0])

        # print(selections)
        return selections

    @staticmethod
    def single_point_crossover(parent_1, parent_2, x_point):
        children = []

        child_1 = parent_1[:x_point] + parent_2[x_point:]
        child_2 = parent_2[:x_point] + parent_1[x_point:]

        children.append(child_1)
        children.append(child_2)

        return children

    def mutate(self, individual):
        mutant = individual

        for _ in range(4):
            index1, index2 = random.randint(0, len(self.cities) - 1), random.randint(0, len(self.cities) - 1)
            mutant[index1], mutant[index2] = mutant[index2], mutant[index1]

        return mutant

    def reproduce(self, population):
        parents = self.select_parents(population, 2)
        children = self.single_point_crossover(parents[0], parents[1], random.randint(0, self.chromosome_length - 1))

        return children

    def run(self, population_size=1000, number_of_generations=1000):
        solution_chromosome = []
        min_global_fitness = math.inf
        population = self.generate_initial_population(population_size)

        for _ in range(number_of_generations):
            population_fitness = min(self.fitness(individual) for individual in population)

            if population_fitness < min_global_fitness:
                population.sort(key=lambda individual: self.fitness(individual))
                solution_chromosome = population[0]
                min_global_fitness = population_fitness

            min_global_fitness = min(min_global_fitness, population_fitness)

            parents = self.select_parents(population, 2)
            children = self.reproduce(parents)

            for child in children:
                self.mutate(child)

            population += children
            population.sort(key=lambda individual: self.fitness(individual))

            population = population[:population_size]

        answer_solution = []
        for i in range(len(solution_chromosome) - 1):
            path = self.path_between_cities(solution_chromosome[i], solution_chromosome[i + 1])
            answer_solution.extend(path)
            answer_solution.pop()

        return answer_solution, min_global_fitness


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

    solver = GeneticAlgorithm(graph, cities)
    print(solver.run())
