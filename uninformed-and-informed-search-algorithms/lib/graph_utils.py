import random
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
sys.path.append(parent_dir)
from assignment_1.lib.graph import Graph

def create_random_graph(num_nodes: int) -> Graph:
    """Create a graph with randomely placed nodes of the amound num_nodes.

    Args:
        num_nodes (int): The number of nodes wanted on the graph.

    Returns:
        Graph: A Graph with the generated nodes.
    """
    new_graph = Graph()
    
    # add all nodes to the new_graph
    for i in range(num_nodes):
        # latitudes range between -90 and 90, so generate a random integer between 0 and 1, multiply it by 90, and then multiply it by 1 or -1 to make it positive or negative
        latitude = random.random() * 90 * random.choice([1, -1])
        # longitudes range between -180 and 180, so generate a random integer between 0 and 1, multiply it by 180, and then multiply it by 1 or -1 to make it positive or negative
        longitude = random.random() * 180 * random.choice([1, -1])
        
        new_graph.add_node(f"{i}", latitude, longitude)
    
    return new_graph

def insert_random_edges(graph: Graph, edge_prob: float) -> Graph:
    """Insert random nodes to a graph.

    Args:
        graph (Graph): An already existing graph.
        edge_prob (float): The probabilities with which to add the edges with.

    Returns:
        Graph: The new graph with the added nodes.
    """
    nodes = graph.get_nodes()
    num_nodes = len(nodes)
    # randomly connect nodes with probability edge_prob
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if random.random() < edge_prob:
                weight = random.randint(1, 10)
                graph.insert_edge(nodes[i], nodes[j], weight)
    
    return graph
