import sys
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))

sys.path.append(parent_dir)

from assignment_1.lib.graph import Graph

def dfs(graph: Graph, start: str, goal: str) -> list[str]:
    visited = set()
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            for neighbor in graph[node][1]:
                stack.append((neighbor, path + [neighbor]))