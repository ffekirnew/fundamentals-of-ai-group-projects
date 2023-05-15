import argparse

# import the list generator in case the user forgets to provide one
from list_generator import generate_input_files

# import the types for the solution
from solution_algorithms._knapsack_types import Item

# import the GeneticAlgorithm class from your implementation
from solution_algorithms.genetic_algorithm import GeneticAlgorithm
from solution_algorithms.hill_climbing_algorithm import HillClimbingAlgorithm
from solution_algorithms.simulated_annealing_algorithm import SimulatedAnnealingAlgorithm


def parse_arguments():
    """The parse_arguments function parses the command line arguments and returns them as an object.

    :return: An object that parses the arguments
    """
    parser = argparse.ArgumentParser(
        description='Solve the knapsack problem using different algorithms.')
    parser.add_argument('--algorithm', type=str, default='ga',
                        help='algorithm to use (ga, hca, or sa)')
    parser.add_argument('--file', type=str, default=None,
                        help='path to input file')

    return parser.parse_args()


def main():
    """The main function of the program.

    :return: The best solution found by the algorithm
    """
    args = parse_arguments()
    algorithm = args.algorithm

    if not args.file:
        files = generate_input_files()
    else:
        files = [ args.file ]

    # for every file passed, do the solution
    for file in files:
        # parse the problem instance from the input file
        with open(file, 'r') as f:
            lines = f.read().split("\n")
            capacity = float(lines[0])
            items = []
            for line in lines[2:]:
                if line == '':
                    continue
                item, weight, value, n_items = line.strip().split(',')
                items.append(Item(name=item, weight=float(weight),
                                  value=float(value), n_items=int(n_items)))

        # create an instance of the selected algorithm and solve the problem
        if algorithm == 'ga':
            selected_algorithm = GeneticAlgorithm(items, capacity)

        elif algorithm == 'hca':
            selected_algorithm = HillClimbingAlgorithm(items, capacity)

        elif algorithm == 'sa':
            selected_algorithm = SimulatedAnnealingAlgorithm(items, capacity)

        else:
            print('Chosen algorithm can only be one of: sa, hca, ga.')
            return

        best_value, solution = selected_algorithm.run()

        # print the solutions
        print(f'Using the items file at: {file}, and the algorithm: {algorithm}')
        print(f'Optimal value: {best_value}')
        print(f'Items in knapsack: {", ".join(str(i) for i in solution)}\n')


if __name__ == '__main__':
    main()
