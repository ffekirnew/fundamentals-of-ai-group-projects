class Graph:
    def __init__(self) -> None:
        self.graph: dict(dict(int)) = {} # to contain key value pairs of ( node : (neighbours : weight ) )
    
    def __repr__(self) -> str:
        return f"Graph: {list(self.graph.keys())}"
    
    def add_node(self, node: str, latitude: float, longitude: float) -> None:
        """Add a new node to the graph.

        Args:
            node (str): Representation of the new node to be added.
        """
        # check if the node already exists in the graph
        if node not in self.graph:
            self.graph[node] = [(latitude, longitude,), {}] # to contain key value pairs of ( neighbours : weight )
    
    def insert_edge(self, node1: str, node2: str, weight: int) -> None:
        """Insert an edge between two nodes into the graph.

        Args:
            node1 (str): Representation of node 1.
            node2 (str): Representation of node 2.
            weight (int): Representation of the weight of the path between the two nodes.
        """
        if node1 not in self.graph or node2 not in self.graph:
            raise Exception("One or both of the nodes don't exist on the graph.")

        # make each nodes the neighbours of eachother by adding them to the graph with the given weight
        self.graph[node1][1][node2] = weight
        self.graph[node2][1][node1] = weight
    
    def delete_node(self, node: str) -> None:
        """Delete a node in the graph.

        Args:
            node (str): Representation of the node to be deleted.
        """
        # check if the node to be deleted exists on the graph
        if node in self.graph:

            # if so, delete all references of the node from all neighbours
            for neighbour in self.graph[node][1]:
                del self.graph[neighbour][node]
            
            # finally delete the node
            del self.graph[node]
    
    def delete_edge(self, node1: str, node2: str) -> None:
        """Delete an edge between two nodes in the graph.

        Args:
            node1 (str): Representation of node 1.
            node2 (str): Representation of node 2.
        """
        # check if both nodes are on the graph
        if node1 in self.graph and node2 in self.graph:

            # check if there is an edge between the nodes.
            if node2 in self.graph[node1]:
                del self.graph[node1][1][node2]
                del self.graph[node2][1][node1]
    
    def search_node(self, node: str) -> bool:
        """Search for a node in the graph.

        Args:
            node (str): Representation of the node to be searched.

        Returns:
            bool: True if the node exists on the graph, false otherwise.
        """
        return node in self.graph
    
    def get_nodes(self) -> list[str]:
        """Return the nodes in the graph.

        Returns:
            list[str]: A list containing all string nodes.
        """
        return list(self.graph.keys())
    
    def get_neighbours(self, node: str) -> list[str]:
        """Return the neighbours of a node in the graph.

        Args:
            node (str): The node to which we want the neighbours for.

        Raises:
            ValueError: If the node doesn't exist on the graph.

        Returns:
            list(str): The list of names of the nodes neighbours.
        """
        if node not in self.graph:
            raise ValueError("The node you requested doesn't exist on the graph.")

        return list(self.graph[node][1].keys())

    def __getitem__(self, key: str) -> list[tuple[float, float], dict[str, int]]:
        """Get a specific node from the graph.

        Args:
            key (str): The node data we are looking for.

        Raises:
            ValueError: If the node doesn't exist on the graph.

        Returns:
            List[Tuple(int), Dict(int)]: Returns a list of a tuple, the location,
            and a dictionary of all neighbouring nodes.
        """
        if key not in self.graph:
            raise ValueError("The node you requested doesn't exist on the graph.")
        
        return self.graph[key]

def load_romania() -> Graph:
    """Load the Romanian map from the book.

    Returns:
        Graph: The graph representation of the Romanian cities.
    """
    # create an empty graph 
    romania = Graph()

    # open the file and read the coordinates
    with open('romanian_cities.txt') as file:
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
