import sys
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
sys.path.append(parent_dir)
from assignment_1.lib.graph import Graph


def load_romania() -> Graph:
    """Load the Romanian map from the book.

    Returns:
        Graph: The graph representation of the Romanian cities.
    """
    # create an empty graph 
    romania = Graph()

    # get the absolute path of the directory containing the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # specify the path to the file relative to the current directory
    file_path = os.path.join(current_dir, 'romanian_cities.txt')

    # open the file and read the coordinates
    with open(file_path) as file:
        cities = file.read().split("\n")[1:]
    
    # add the cities as nodes to the graph
    for city in cities:
        name, x, y = city.split("    ")
        x = float(x)
        y = float(y)

        romania.add_node(name, x, y)
    
    # add the edges
    romania.insert_edge("Oradea", "Zerind", 71)
    romania.insert_edge("Oradea", "Sibiu", 151)
    romania.insert_edge("Zerind", "Arad", 75)
    romania.insert_edge("Arad", "Sibiu", 140)
    romania.insert_edge("Arad", "Timisoara", 118)
    romania.insert_edge("Timisoara", "Lugoj", 111)
    romania.insert_edge("Lugoj", "Mehadia", 70)
    romania.insert_edge("Mehadia", "Drobeta", 75)
    romania.insert_edge("Drobeta", "Craiova", 120)
    romania.insert_edge("Sibiu", "Rimnicu Vilcea", 80)
    romania.insert_edge("Rimnicu Vilcea", "Craiova", 146)
    romania.insert_edge("Sibiu", "Fagaras", 99)
    romania.insert_edge("Fagaras", "Bucharest", 211)
    romania.insert_edge("Rimnicu Vilcea", "Pitesti", 97)
    romania.insert_edge("Pitesti", "Bucharest", 101)
    romania.insert_edge("Bucharest", "Giurgiu", 90)
    romania.insert_edge("Iasi", "Neamt", 87)
    romania.insert_edge("Iasi", "Vaslui", 92)
    romania.insert_edge("Vaslui", "Urziceni", 142)
    romania.insert_edge("Urziceni", "Bucharest", 85)
    romania.insert_edge("Urziceni", "Hirsova", 98)
    romania.insert_edge("Hirsova", "Eforie", 86)

    # print romania
    return romania

romania = load_romania()
