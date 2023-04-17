import copy

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
                del self.graph[neighbour][1][node]
            
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
            if node2 in self.graph[node1][1]:
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
    
    def get_neighbours(self, node: str) -> list[tuple[str, int]]:
        """Return the neighbours of a node in the graph.

        Args:
            node (str): The node to which we want the neighbours for.

        Raises:
            ValueError: If the node doesn't exist on the graph.

        Returns:
            list(tuple(str, int)): The list of names of the nodes neighbours and the weights.
        """
        if node not in self.graph:
            raise ValueError("The node you requested doesn't exist on the graph.")

        return list(self.graph[node][1].items())

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
    
    def __contains__(self, node: str) -> bool:
        """Returns if a node is part of self graph in pythonic manner.

        Example Usage:
            node in graph_variable

        Args:
            node (str): The node we want to look for.

        Returns:
            bool: True if the node is in the graph, false otherwise.
        """
        return node in self.graph
    
    def get_copy(self):
        """Return the shallow copy of the graph.

        Returns:
            Graph: a graph.
        """
        return copy.deepcopy(self)

