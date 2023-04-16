import unittest
from ..graph import Graph

class TestGraph(unittest.TestCase):
    def test_add_node(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        self.assertIn("A", graph.get_nodes())

    def test_insert_edge(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        graph.add_node("B", 2.0, 3.0)
        graph.insert_edge("A", "B", 3)
        self.assertEqual(graph["A"][1]["B"], 3)
        self.assertEqual(graph["B"][1]["A"], 3)

    def test_delete_node(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        graph.add_node("B", 2.0, 3.0)
        graph.insert_edge("A", "B", 3)
        graph.delete_node("A")
        self.assertNotIn("A", graph.get_nodes())
        self.assertNotIn("A", graph.get_neighbours("B"))

    def test_delete_edge(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        graph.add_node("B", 2.0, 3.0)
        graph.insert_edge("A", "B", 3)
        graph.delete_edge("A", "B")
        self.assertNotIn("B", graph["A"][1])
        self.assertNotIn("A", graph["B"][1])

    def test_search_node(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        self.assertTrue(graph.search_node("A"))
        self.assertFalse(graph.search_node("B"))

    def test_get_nodes(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        graph.add_node("B", 2.0, 3.0)
        self.assertEqual(graph.get_nodes(), ["A", "B"])

    def test_get_neighbours(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        graph.add_node("B", 2.0, 3.0)
        graph.add_node("C", 3.0, 4.0)
        graph.insert_edge("A", "B", 3)
        graph.insert_edge("B", "C", 5)
        self.assertEqual(graph.get_neighbours("B"), ["A", "C"])

    def test_getitem(self):
        graph = Graph()
        graph.add_node("A", 1.0, 2.0)
        graph.add_node("B", 2.0, 3.0)
        graph.insert_edge("A", "B", 3)
        self.assertEqual(graph["A"], [(1.0, 2.0), {"B": 3}])
