import unittest
from simulated_annealing_algorithm import SimulatedAnnealingAlgorithm
from _knapsack_types import Item, WeightLimit


class TestSimulatedAnnealingAlgorithm(unittest.TestCase):

    def setUp(self) -> None:
        self.items = [
            Item(name='Phone', weight=0.19, value=1000, n_items=5),
            Item(name='Laptop', weight=1.1, value=700, n_items=2),
            Item(name='Bag', weight=2.19, value=100, n_items=5),
            Item(name='Gaming Laptop', weight=4.1, value=1700, n_items=2)
        ]

    def test_generate_initial_solution(self):
        algorithm = SimulatedAnnealingAlgorithm(self.items, WeightLimit(7.5))
        solution = algorithm.generate_initial_solution()
        self.assertEqual(len(solution), len(self.items))
        self.assertIn(1, solution)
        self.assertIn(0, solution)

    def test_evaluate_solution_value(self):
        algorithm = SimulatedAnnealingAlgorithm(self.items, WeightLimit(15))
        solution = [1] * 10 + [0] * 5
        value = algorithm.evaluate_solution_value(solution)
        self.assertEqual(value, 1500)

    def test_generate_solution_neighbours(self):
        algorithm = SimulatedAnnealingAlgorithm(self.items, WeightLimit(30))
        solution = [0] * 20
        neighbours = algorithm.generate_solution_neighbours(solution)
        self.assertEqual(len(neighbours), 20)
        self.assertIn([1] + [0]*19, neighbours)
        self.assertIn([0]*19 + [1], neighbours)

    def test_accept(self):
        current_value = 1000
        neighbour_value = 800
        temperature = 100
        accept = SimulatedAnnealingAlgorithm.accept(current_value, neighbour_value, temperature)
        self.assertTrue(accept)

    def test_run(self):
        algorithm = SimulatedAnnealingAlgorithm(self.items, WeightLimit(7.5))
        value, solution = algorithm.run()
        self.assertGreater(value, 0)


if __name__ == '__main__':
    unittest.main()
