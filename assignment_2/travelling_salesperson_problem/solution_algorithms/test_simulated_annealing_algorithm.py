import unittest
from travelling_salesperson_types import City, Graph, Tour
from simulated_annealing_algorithm import SimulatedAnnealingAlgorithm

class TestSimulatedAnnealingAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph: Graph = {
            'Bucuresti': {'Pitesti': 100, 'Giurgiu': 90, 'Braila': 200},
            'Pitesti': {'Bucuresti': 100, 'Craiova': 138},
            'Craiova': {'Pitesti': 138, 'Rimnicu Vilcea': 146},
            'Rimnicu Vilcea': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
            'Sibiu': {'Rimnicu Vilcea': 80, 'Fagaras': 99},
            'Fagaras': {'Sibiu': 99, 'Bucuresti': 211},
            'Giurgiu': {'Bucuresti': 90},
            'Braila': {'Bucuresti': 200, 'Galati': 130},
            'Galati': {'Braila': 130}
        }

    def test_is_tour_valid(self):
        algorithm = SimulatedAnnealingAlgorithm(self.graph)

        # Valid tour
        tour: Tour = ['Bucuresti', 'Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Sibiu', 'Fagaras', 'Bucuresti']
        self.assertTrue(algorithm.is_tour_valid(tour))

        # Invalid tour
        tour: Tour = ['Bucuresti', 'Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Braila', 'Fagaras', 'Bucuresti']
        self.assertFalse(algorithm.is_tour_valid(tour))

    def test_evaluate_cost(self):
        algorithm = SimulatedAnnealingAlgorithm(self.graph)

        # Tour with cost 766
        tour: Tour = ['Bucuresti', 'Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Sibiu', 'Fagaras', 'Bucuresti']
        self.assertEqual(algorithm.evaluate_cost(tour), 766)

        # Tour with cost 1134
        tour: Tour = ['Bucuresti', 'Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Sibiu', 'Fagaras', 'Bucuresti']
        self.assertEqual(algorithm.evaluate_cost(tour), 1134)

    def test_generate_initial_tour(self):
        algorithm = SimulatedAnnealingAlgorithm(self.graph)

        # Check that generated tours are valid
        for i in range(10):
            tour = algorithm.generate_initial_tour()
            self.assertTrue(algorithm.is_tour_valid(tour))

    def test_generate_neighbour(self):
        algorithm = SimulatedAnnealingAlgorithm(self.graph)

        # Neighbour of ['Bucuresti', 'Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Sibiu', 'Fagaras', 'Bucuresti']
        current_tour: Tour = ['Bucuresti', 'Pitesti', 'Craiova', 'Rimnicu Vilcea', 'Sibiu', 'Fagaras', 'Bucuresti']
        neighbour = algorithm.generate_neighbour(current_tour)
        self.assertTrue(algorithm.is_tour_valid(neighbour))
        self.assertNotEqual(current_tour, neighbour)

    def test_accept(self):
        algorithm = SimulatedAnnealingAlgorithm(self.graph)

        # Accept worse solution with high temperature
        self.assertTrue(algorithm.accept(100, 110, 1000))

        # Accept worse solution with low temperature
        self.assertTrue(algorithm.accept(100, 110, 0.00001))

        # Reject worse solution with low temperature
        self.assertFalse(algorithm.accept(100, 110, 0.1))

    def test_run(self):
        algorithm = SimulatedAnnealingAlgorithm(self.graph)

        # Check that the algorithm returns a valid tour with reasonable cost
        tour, cost = algorithm.run()
        self.assertTrue(algorithm.is_tour_valid(tour))
        self.assertLessEqual(cost, 1000)


if __name__ == '__main__':
    unittest.main()