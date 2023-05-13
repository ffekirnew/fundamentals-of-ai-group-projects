import unittest
from hill_climbing_algorithm import HillClimbingAlgorithm
from knapsack_types import Item, WeightLimit


class TestHillClimbingAlgorithm(unittest.TestCase):

    def setUp(self):
        self.items = [
            Item(name='Phone', weight=0.19, value=1000, n_items=5),
            Item(name='Laptop', weight=1.1, value=700, n_items=2),
            Item(name='Bag', weight=2.19, value=100, n_items=5),
            Item(name='Gaming Laptop', weight=4.1, value=1700, n_items=2)
        ]
        self.weight_limit = WeightLimit(10)
        self.algorithm = HillClimbingAlgorithm(self.items, self.weight_limit)

    def test_evaluate_solution_value(self):
        self.assertEqual(
            self.algorithm.evalueate_solution_value([1, 0, 1, 0]), 1100)
        self.assertEqual(
            self.algorithm.evalueate_solution_value([0, 0, 0, 0]), 0)
        self.assertEqual(
            self.algorithm.evalueate_solution_value([1, 1, 1, 1]), 3500)
        self.assertEqual(
            self.algorithm.evalueate_solution_value([1, 0, 0, 1]), 2700)

    def test_generate_initial_solution(self):
        solution = self.algorithm.generate_initial_solution()
        self.assertEqual(len(solution), len(self.items))
        self.assertLessEqual(sum(solution), self.weight_limit)
        self.assertGreater(
            self.algorithm.evalueate_solution_value(solution), 0)

    def test_generate_solution_neighbour(self):
        solution = [1, 1, 0, 0]
        neighbour, neighbour_value = self.algorithm.generate_solution_neighbour(
            solution)
        self.assertEqual(len(neighbour), len(solution))
        self.assertGreater(
            neighbour_value, self.algorithm.evalueate_solution_value(solution))

    def test_run(self):
        value, items = self.algorithm.run()
        self.assertIsInstance(value, int)
        self.assertIsInstance(items, list)
        self.assertGreater(value, 0)
        self.assertLessEqual(sum([self.items[i].weight for i in range(
            len(self.items)) if items[i]]), self.weight_limit)


if __name__ == '__main__':
    unittest.main()
