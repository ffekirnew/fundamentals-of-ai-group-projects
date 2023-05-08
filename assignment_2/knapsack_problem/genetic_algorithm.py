from random import choice, random, randint
from typing import List
from knapsack_types import Item, Items, WeightLimit, Gene, Individual, Population, Fitness


class GeneticAlgorithm:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:
        self.items: Items = items
        self.weight_limit: WeightLimit = weight_limit
        self.chromosom_length: int = len(self.items)

    def __repr__(self) -> str:
        return f"Genetic Algorithm to solve the knapsack problem for Items: {self.items} with the capacity limit {self.weight_limit}."

    def generate_random_individual(self) -> Individual:
        individual: Individual = []

        # TODO: generate the random genes and append to the individual
        for gene in range(self.chromosom_length):
            gene: Gene = choice([0, 1])
            individual.append(gene)

        return individual

    def generate_initial_population(self, population_size: int) -> Population:
        population: Population = []

        # do something
        for _ in range(population_size):
            population.append(self.generate_random_individual())

        return population

    def fitness(self, individual: Individual) -> Fitness:
        total_weight: int = 0
        total_value: Fitness = 0

        for index, gene in enumerate(individual):
            if gene == 1:
                total_weight += self.items[index].weight
                if total_weight > self.weight_limit:
                    # individual is disqualified
                    return -1

                total_value += self.items[index].value

        return total_value

    def calculate_population_probability(self, population: Population) -> List[float]:
        total_fitness: Fitness = sum(self.fitness(individual)
                                 for individual in population)

        probability_of_population: List[float] = []

        for individual in population:
            probability_of_population.append(
                self.fitness(individual) / total_fitness)

        return probability_of_population

    def select_parents(self, population: Population, number_of_selections: int) -> Population:
        possible_probabilities: List[int] = self.calculate_population_probability(
            population)

        slices: List[int] = []
        total: int = 0

        for i in range(len(population)):
            slices.append([i, total, total + possible_probabilities[i]])
            total += possible_probabilities[i]

        selections: Population = []
        for i in range(number_of_selections):
            spin: float = random()
            selections.append(
                [population[slice[0]] for slice in slices if slice[1] < spin <= slice[2]][0])

        return selections

    def single_point_crossover(self, parent_1: Individual, parent_2: Individual, x_point: int) -> Population:
        children: Population = []

        child_1 = parent_1[:x_point] + parent_2[x_point:]
        child_2 = parent_2[:x_point] + parent_1[x_point:]

        children.append(child_1)
        children.append(child_2)

        return children

    def mutate(self, individual: Individual) -> None:
        index: int = randint(0, self.chromosom_length - 1)

        individual[index] = 1 - individual[index]  # flip the gene

        return individual
    
    def reproduce(self, population: Population) -> Individual:
        parents: Population = self.select_parents(population, 2)
        children: Population = self.single_point_crossover(parents[0], parents[1], randint(0, self.chromosom_length - 1))

        return children

    def run(self, population_size: int = 1000, number_of_generations: int = 1000):
        solution_chromosom: Individual = None
        max_global_fitness: Fitness = 0
        population: Population = self.generate_initial_population(population_size)

        for i in range(number_of_generations):
            population_fitness = max(self.fitness(individual) for individual in population)

            if population_fitness > max_global_fitness:
                population.sort(key=lambda individual: self.fitness(individual), reverse=True)
                solution_chromosom = population[0]  
                max_global_fitness = population_fitness


            max_global_fitness = max( max_global_fitness, population_fitness )

            parents = self.select_parents(population, 2)
            children = self.reproduce(parents)

            for child in children:
                self.mutate(child)

            population += children
            population.sort(key=lambda individual: self.fitness(individual), reverse=True)

            population = population[:population_size]

        solution: List[str] = []
        for index, gene in enumerate(solution_chromosom):
            if gene == 1:
                solution.append(self.items[index].name)

        
        return max_global_fitness, solution
