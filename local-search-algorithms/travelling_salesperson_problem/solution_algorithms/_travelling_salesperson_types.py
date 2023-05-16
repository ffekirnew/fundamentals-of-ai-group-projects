import heapq


def ucs(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, city, path = heapq.heappop(queue)

        if city == end:
            return path + [city]

        if city in visited:
            continue

        visited.add(city)

        for neighbor, edge_cost in graph[city]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [city]))

    return None


if __name__ == "__main__":
    # Romanian map represented as an adjacency list
    graph = {
        'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
        'Zerind': [('Arad', 75), ('Oradea', 71)],
        'Timisoara': [('Arad', 118), ('Lugoj', 111)],
        'Sibiu': [('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Oradea', 151)],
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
        'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
        'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
        'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
        'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
        'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
        'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138), ('Dobreta', 120)],
        'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
        'Giurgiu': [('Bucharest', 90)],
        'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
        'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
        'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
        'Iasi': [('Vaslui', 92), ('Neamt', 87)],
        'Neamt': [('Iasi', 87)],
        'Eforie': [('Hirsova', 86)]
    }

    start_city = 'Arad'
    end_city = 'Bucharest'

    # Find the shortest path between two cities using UCS
    path = ucs(graph, start_city, end_city)

    if path:
        print(f"Shortest path from {start_city} to {end_city}:")
        print(" -> ".join(path))
    else:
        print(f"No path found from {start_city} to {end_city}.")
