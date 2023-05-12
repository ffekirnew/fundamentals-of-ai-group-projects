import unittest
from random import seed
from typing import List
from knapsack_types import Item, Individual
from genetic_algorithm import GeneticAlgorithm


class TestGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        # Set up some test data
        self.items = [
            Item(name='Phone', weight=0.19, value=1000, n_items=5),
            Item(name='Laptop', weight=1.1, value=700, n_items=2)
        ]
        self.weight_limit = 5
        self.ga = GeneticAlgorithm(self.items, self.weight_limit)
        seed(42)

    def test_generate_random_individual(self):
        individual = self.ga.generate_random_individual()
        self.assertEqual(len(individual), self.ga.chromosome_length)

    def test_generate_initial_population(self):
        population_size = 10
        population = self.ga.generate_initial_population(population_size)
        self.assertEqual(len(population), population_size)

    def test_fitness(self):
        individual = [1, 0]
        fitness = self.ga.fitness(individual)
        self.assertEqual(fitness, 1000)

        individual = [0, 1]
        fitness = self.ga.fitness(individual)
        self.assertEqual(fitness, 700)

        individual = [1, 1]
        fitness = self.ga.fitness(individual)
        self.assertEqual(fitness, 1700)

    def test_calculate_population_probability(self):
        population = [
            [0, 0],
            [1, 1],
            [0, 1],
            [1, 0],
        ]
        probability = self.ga.calculate_population_probability(population)
        self.assertEqual(len(probability), len(population))
        self.assertAlmostEqual(sum(probability), 1.0)

    def test_select_parents(self):
        population = [
            [0, 0],
            [1, 1],
            [0, 1],
            [1, 0],
        ]
        number_of_selections = 2
        selections = self.ga.select_parents(population, number_of_selections)
        self.assertEqual(len(selections), number_of_selections)
        for selection in selections:
            self.assertIsInstance(selection, List)

    def test_single_point_crossover(self):
        parent_1 = [1, 0, 1, 0, 1]
        parent_2 = [0, 1, 0, 1, 0]
        x_point = 3
        expected_children = [[1, 0, 1, 1, 0], [0, 1, 0, 0, 1]]
        children = self.ga.single_point_crossover(parent_1, parent_2, x_point)
        self.assertEqual(children, expected_children)

    def test_mutate(self):
        individual = [1, 0, 1, 0, 1]
        expected_individuals = [
            [0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0]
        ]
        for _ in expected_individuals:
            new_individual: Individual = self.ga.mutate(individual.copy())
            self.assertIn(new_individual, expected_individuals)

    def test_reproduce(self):
        population = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]
        expected_children = [[1, 0, 0, 1, 0], [0, 1, 1, 0, 1]]
        children = self.ga.reproduce(population)
        self.assertEqual(children, expected_children)

    def test_run(self):
        population_size = 10
        number_of_generations = 5
        max_global_fitness = self.ga.run(population_size, number_of_generations)
        self.assertEqual(type(max_global_fitness), tuple)


if __name__ == '__main__':
    unittest.main()
