import sys
import os
from collections import deque

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))

sys.path.append(parent_dir)

from assignment_1.lib.graph import Graph


def bfs(graph: Graph, start: str, goal: str) -> list[str]:
        fringe = deque()
        visited = set()
        parent = {}
        
        fringe.append(start)
        parent[start] = None

        while fringe:
            currentNode = fringe.popleft()

            if currentNode in visited:
                continue

            visited.add(currentNode)

            if currentNode == goal:
                # Construct the path from the start node to the target node
                path = []
                while currentNode is not None:
                    path.append(currentNode)
                    currentNode = parent[currentNode]
                path.reverse()
                return path
            
            for child, weight in graph.get_neighbours(currentNode):
                if child not in visited:
                    parent[child] = currentNode
                    fringe.append(child)

        return []