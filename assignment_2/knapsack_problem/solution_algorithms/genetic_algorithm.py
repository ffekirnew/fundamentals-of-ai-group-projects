from random import choice, random, randint
from typing import List, Tuple
from .knapsack_types import Items, WeightLimit, Gene, Individual, Population, Fitness


class GeneticAlgorithm:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:
        """The __init__ function initializes the KnapsackProblem class.

        :param self: Represent the instance of the class
        :param items: Items: Store the items that are available for packing
        :param weight_limit: WeightLimit: Set the weight limit of the knapsack
        :return: None
        """
        self.items: Items = items
        self.weight_limit: WeightLimit = weight_limit
        self.chromosome_length: int = len(self.items)

    def __repr__(self) -> str:
        """The __repr__ function is the string representation of an object.

        :param self: Represent the instance of the class
        :return: A string representation of the object
        """
        return f"""
                Genetic Algorithm to solve the knapsack problem for 
                Items: {self.items}
                with the capacity limit {self.weight_limit}.
                """

    def generate_random_individual(self) -> Individual:
        """
        The generate_random_individual function generates a random individual.

        :param self: Refer to the class itself
        :return: An individual with the same number of chromosomes as the number of items
        """
        individual: Individual = []

        # generate the random genes and append to the individual
        for gene in range(self.chromosome_length):
            gene: Gene = choice([0, 1])
            individual.append(gene)

        return individual

    def generate_initial_population(self, population_size: int) -> Population:
        """Generate and return a population of random individuals.

        :param self: Bind the method to the object
        :param population_size: int: Determine how many individuals will be in the population
        :return: A population object, which is a list of individual objects.
        """
        population: Population = []

        # generated random individuals with random chromosome and add them to the population
        for _ in range(population_size):
            population.append(self.generate_random_individual())

        return population

    def fitness(self, individual: Individual) -> Fitness:
        """The fitness function for the knapsack problem is a simple one.
        It takes an individual and returns its fitness value, which is the sum of all items' values in the individual's
        genes. If any item's weight exceeds the weight limit, then it disqualifies that individual by returning - 1.

        :param self: Access the class variables
        :param individual: Individual: Represent the chromosome
        :return: A value
        """
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
        """The calculate_population_probability function takes a population and returns the probability of each
        individual in that population.

        :param self: Access the attributes and methods of the class
        :param population: Population: Calculate the total fitness of the population
        :return: A list of floats
        """
        total_fitness: Fitness = sum(self.fitness(individual)
                                     for individual in population)

        probability_of_population: List[float] = []

        for individual in population:
            probability_of_population.append(
                self.fitness(individual) / total_fitness)

        return probability_of_population

    def select_parents(self, population: Population, number_of_selections: int) -> Population:
        """The select_parents function takes in a population and the number of selections to be made.
        It then calculates the probability for each individual in the population, based on their fitness score.
        The function then creates a list of slices, which are lists containing an index value (i),
        the lower bound (total) and upper bound (total + possible_probabilities[i]). The total is incremented by
        possible_probabilities[i] after each iteration. A spin variable is created with random() as its value,
        and if it falls within any section's bounds, that section's index will be appended

        :param self: Refer to the current instance of a class
        :param population: Population: Pass the population to the function
        :param number_of_selections: int: Determine the number of parents that will be selected
        :return: A list of parents, which is the population
        """
        possible_probabilities: List[float] = self.calculate_population_probability(
            population)

        slices: List[list] = []
        total: int = 0

        for i in range(len(population)):
            slices.append([i, total, total + possible_probabilities[i]])
            total += possible_probabilities[i]

        selections: Population = []
        for i in range(number_of_selections):
            spin: float = random()
            selections.append(
                [population[section[0]] for section in slices if section[1] < spin <= section[2]][0])

        return selections

    @staticmethod
    def single_point_crossover(parent_1: Individual, parent_2: Individual, x_point: int) -> Population:
        """The single_point_crossover function takes two parent individuals and a crossover point as input.
        It then returns the children of those parents, which are created by taking the first half of one parent's genes
        and combining it with the second half of another parent's genes.

        :param parent_1: Individual: Specify the type of parent_2
        :param parent_2: Individual: Pass the second parent to the function
        :param x_point: int: Determine the crossover point
        :return: A list of two children
        """
        children: Population = []

        child_1 = parent_1[:x_point] + parent_2[x_point:]
        child_2 = parent_2[:x_point] + parent_1[x_point:]

        children.append(child_1)
        children.append(child_2)

        return children

    def mutate(self, individual: Individual) -> Individual:
        """The mutate function takes an individual and returns a mutated version of that individual.

        :param self: Make the function a method of the class
        :param individual: Individual: Pass the individual to be mutated
        :return: an Individual
        """
        index: int = randint(0, self.chromosome_length - 1)

        individual[index] = 1 - individual[index]  # flip the gene

        return individual

    def reproduce(self, population: Population) -> Population:
        """The reproduce function takes a population and returns two children.
        It does this by selecting two parents from the population, then performing single point crossover on them.


        :param self: Refer to the object itself
        :param population: Population: Select the parents
        :return: A population of children
        """
        parents: Population = self.select_parents(population, 2)
        children: Population = self.single_point_crossover(parents[0], parents[1],
                                                           randint(0, self.chromosome_length - 1))

        return children

    def run(self, population_size: int = 1000, number_of_generations: int = 1000) -> tuple[int, list[str]]:
        """The run function is the main function of the Genetic Algorithm. It takes in two parameters:
        population_size and number_of_generations. The population size is how many individuals are in each generation,
        and number of generations is how many times we will run through our algorithm before stopping it.
        The function returns a tuple containing the maximum global fitness and solution chromosome.

        :param self: Represent the instance of the class
        :param population_size: int: Set the size of the population
        :param number_of_generations: int: Set the number of generations that will be run
        :return: A tuple containing the maximum fitness of the final population and a list of items that make up the solution
        """
        solution_chromosome: Individual = []
        max_global_fitness: Fitness = 0
        population: Population = self.generate_initial_population(
            population_size)

        for i in range(number_of_generations):
            population_fitness = max(self.fitness(individual)
                                     for individual in population)

            if population_fitness > max_global_fitness:
                population.sort(key=lambda individual: self.fitness(
                    individual), reverse=True)
                solution_chromosome = population[0]
                max_global_fitness = population_fitness

            max_global_fitness = max(max_global_fitness, population_fitness)

            parents = self.select_parents(population, 2)
            children = self.reproduce(parents)

            for child in children:
                self.mutate(child)

            population += children
            population.sort(key=lambda individual: self.fitness(
                individual), reverse=True)

            population = population[:population_size]

        solution: List[str] = []
        for index, gene in enumerate(solution_chromosome):
            if gene == 1:
                solution.append(self.items[index].name)

        return max_global_fitness, solution
