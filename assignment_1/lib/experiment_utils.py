from random import shuffle
import timeit
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
sys.path.append(parent_dir)
from assignment_1.lib.graph_utils import create_random_graph, insert_random_edges
from assignment_1.lib.load_romanian_cities import load_romania

def node_experiment(experiment_graphs, search_algorithm):
    # take the nodes from the first graph which only has 10 nodes, and pick five of them to run all experiments with
    nodes = experiment_graphs[0][1].get_nodes()
    shuffle(nodes)
    random_nodes = nodes[:10]

    # run and record the results in a dictionary
    results = {}

    for label, graph in experiment_graphs:
        results[label] = {}

        for i in range(len(random_nodes)):
            for j in range(i + 1, len(random_nodes)):
                node1 = random_nodes[i]
                node2 = random_nodes[j]
                path = search_algorithm(graph, node1, node2)
                time_taken = timeit.timeit(lambda: search_algorithm(graph, node1, node2), number=5)

                results[label][f"{node1} to {node2}"] = (time_taken * 1000, path)

    return experiment_graphs, results

def experiment(search_algorithm, num_nodes: list[int], edge_probabilities: list[float]) -> tuple[list, dict]:
    """Do experiment and return the experiment data set and the results.

    Args:
        search_algorithm (function): The function to perform the experiments with.
        num_nodes (list[int]): The number of nodes to do the different experiments with.
        edge_probabilities (list[float]): The different edge probabilities to perform the experiment with.

    Returns:
        tuple[list, dict]: The experiment data set and the results of the experiment.
    """
    # find all experiment graphs
    experiment_graphs = []

    for number in num_nodes:
        graph = create_random_graph(number)

        for edge_prob in edge_probabilities:
            edges_added_graph = insert_random_edges(graph.get_copy(), edge_prob)
            experiment_graphs.append((f"{len(graph.get_nodes())}, {edge_prob}", edges_added_graph))

    return node_experiment(experiment_graphs, search_algorithm)
    

def city_benchmark(search_algorithm):
    # load romanian cities from the book and the file and set them up to choose 10 random cities
    romania = load_romania()
    romanian_cities = romania.get_nodes()
    shuffle(romanian_cities)
    random_cities = romanian_cities[:10]

    # create variables to hold the total time and total path length for the experiemnt
    total_time = 0
    total_path_length = 0

    # find the path between the cities
    for city1 in random_cities:
        for city2 in random_cities:
            if city1 is not city2:
                # get ahold of the path and time taken for each experiment
                path = search_algorithm(romania, city1, city2)
                time_taken = timeit.timeit(lambda: search_algorithm(romania, city1, city2), number=10)

                total_time += time_taken
                total_path_length += len(path)

    # Print the average time and path length recorded
    number_of_experiments = 45 # 10 cities, we try to find path between one city with the rest 9
    average_time = total_time / number_of_experiments
    average_path_length = total_path_length / number_of_experiments

    return average_time, average_path_length