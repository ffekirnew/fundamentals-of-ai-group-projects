import sys
import os
import math
from heapq import heapify, heappop, heappush

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))

sys.path.append(parent_dir)

from assignment_1.lib.graph import Graph

def heuristic_function(graph, node1, node2):
    return math.sqrt( (graph[node1][0][0] - graph[node2][0][0]) ** 2 + (graph[node1][0][1] - graph[node2][0][1]) ** 2 )

def a_star_search(graph: Graph, start: str, goal: str) -> bool:
    # sanity check to make sure both nodes exist on the graph.
    if start not in graph or goal not in graph:
        raise ValueError("The start and/or the goal nodes do not exist on the graph.")
    
    visited = set([start])

    curr_node = start
    fringe = [ (heuristic_function(graph, start, goal), start, [start], 0,) ]
    heapify(fringe)

    while fringe:
        _, curr_node, curr_path, curr_cost = heappop(fringe)

        if curr_node == goal:
            return curr_path

        visited.add(curr_node)

        for neighbour, weight in graph.get_neighbours(curr_node):
            if neighbour not in visited:
                new_path = curr_path + [neighbour]
                new_cost = weight + curr_cost
                heuristic = heuristic_function(graph, neighbour, goal) + new_cost

                heappush(fringe, tuple([heuristic, neighbour, new_path, new_cost]))

    return