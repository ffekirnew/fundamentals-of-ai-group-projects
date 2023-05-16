import unittest
from graph import Graph
from typing import List, Tuple
from load_romanian_cities import load_romania

class TestLoadRomania(unittest.TestCase):
    
    def test_load_romania(self):
        romania = load_romania()
        
        # Check if all the citis are added
        expected_cities = ["Oradea", "Zerind", "Arad", "Sibiu", "Timisoara", "Lugoj", "Mehadia", 
                          "Drobeta", "Craiova", "Rimnicu Vilcea", "Fagaras", "Bucharest", "Giurgiu", 
                          "Iasi", "Neamt", "Vaslui", "Urziceni", "Hirsova", "Eforie"]
        for city in expected_cities:
            self.assertTrue(city in romania)
        
        # Check if all the edges are added
        expected_edges = [("Oradea", "Zerind", 71), ("Oradea", "Sibiu", 151), ("Zerind", "Arad", 75), 
                          ("Arad", "Sibiu", 140), ("Arad", "Timisoara", 118), ("Timisoara", "Lugoj", 111), 
                          ("Lugoj", "Mehadia", 70), ("Mehadia", "Drobeta", 75), ("Drobeta", "Craiova", 120), 
                          ("Sibiu", "Rimnicu Vilcea", 80), ("Rimnicu Vilcea", "Craiova", 146), 
                          ("Sibiu", "Fagaras", 99), ("Fagaras", "Bucharest", 211), 
                          ("Rimnicu Vilcea", "Pitesti", 97), ("Pitesti", "Bucharest", 101), 
                          ("Bucharest", "Giurgiu", 90), ("Iasi", "Neamt", 87), ("Iasi", "Vaslui", 92), 
                          ("Vaslui", "Urziceni", 142), ("Urziceni", "Bucharest", 85), 
                          ("Urziceni", "Hirsova", 98), ("Hirsova", "Eforie", 86)]
        for city1, city2, weight in expected_edges:
            self.assertTrue((city2, weight) in romania.get_neighbours(city1))
            self.assertTrue((city1, weight) in romania.get_neighbours(city2))
            self.assertEqual(romania[city1][1][city2], weight)
