import argparse
from solution_algorithms.hill_climbing_algorithm import *
from solution_algorithms.simulated_annealing import *
from solution_algorithms.genetic_algorithm import *


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Solve the travelling salesperson problem using different algorithms.')
    parser.add_argument('--algorithm', type=str, default='ga',
                        help='algorithm to use (ga, hc, or sa)')

    return parser.parse_args()


def main():
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
    cities = list(graph.keys())

    args = parse_arguments()

    # create an instance of the selected algorithm and solve the problem
    if args.algorithm == 'ga':
        selected_algorithm = GeneticAlgorithm(graph, cities)

    elif args.algorithm == 'hc':
        selected_algorithm = HillClimbingAlgorithm(graph, cities)

    elif args.algorithm == 'sa':
        selected_algorithm = SimulatedAnnealingAlgorithm(graph, cities)

    best_value, solution = selected_algorithm.run()
    print((best_value, solution))


if __name__ == '__main__':
    main()
