import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()

    def test_add_node(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.assertIn("A", self.graph.get_nodes())

    def test_insert_edge(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.graph.add_node("B", 2.34, 5.67)
        self.graph.insert_edge("A", "B", 5)
        self.assertIn(("B", 5), self.graph.get_neighbours("A"))
        self.assertIn(("A", 5), self.graph.get_neighbours("B"))

    def test_delete_node(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.graph.add_node("B", 2.34, 5.67)
        self.graph.insert_edge("A", "B", 5)
        self.graph.delete_node("A")
        self.assertNotIn("A", self.graph.get_nodes())
        self.assertNotIn(("A", 5), self.graph.get_neighbours("B"))

    def test_delete_edge(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.graph.add_node("B", 2.34, 5.67)
        self.graph.insert_edge("A", "B", 5)
        self.graph.delete_edge("A", "B")
        self.assertNotIn(("B", 5), self.graph.get_neighbours("A"))
        self.assertNotIn(("A", 5), self.graph.get_neighbours("B"))

    def test_search_node(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.assertTrue(self.graph.search_node("A"))
        self.assertFalse(self.graph.search_node("B"))

    def test_get_nodes(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.graph.add_node("B", 2.34, 5.67)
        self.assertListEqual(["A", "B"], self.graph.get_nodes())

    def test_get_neighbours(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.graph.add_node("B", 2.34, 5.67)
        self.graph.insert_edge("A", "B", 5)
        self.assertListEqual([("B", 5)], self.graph.get_neighbours("A"))

    def test_getitem(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.graph.add_node("B", 2.34, 5.67)
        self.graph.insert_edge("A", "B", 5)
        print(self.graph['A'])
        self.assertEqual([((1.23, 4.56)), {'B': 5}], self.graph['A'])

    def test_contains(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.assertIn("A", self.graph)
        self.assertNotIn("B", self.graph)

    def test_get_copy(self):
        self.graph.add_node("A", 1.23, 4.56)
        self.graph.add_node("B", 2.34, 5.67)
        self.graph.insert_edge("A", "B", 5)
        copy_graph = self.graph.get_copy()
        self.assertEqual(self.graph.get_nodes(), copy_graph.get_nodes())
