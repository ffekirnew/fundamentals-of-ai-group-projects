import sys
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))

sys.path.append(parent_dir)

from assignment_1.lib.graph import Graph
from heapq import heapify, heappop, heappush

def ucs_search(graph: Graph, start: str, goal: str) -> list[str]:
    # sanity check to make sure both nodes exist on the graph.
    if start not in graph or goal not in graph:
        raise ValueError("The start and/or the goal nodes do not exist on the graph.")
    
    visited = set([start])

    curr_node = start
    fringe = [ (0, start, [start],) ]

    while fringe:
        curr_cost, curr_node, curr_path = heappop(fringe)

        if curr_node == goal:
            return curr_path

        visited.add(curr_node)

        for neighbour, weight in graph.get_neighbours(curr_node):
            if neighbour not in visited:
                new_path = curr_path + [neighbour]
                new_cost = weight + curr_cost

                heappush(fringe, (new_cost, neighbour, new_path,))

    return