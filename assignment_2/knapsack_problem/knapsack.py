import argparse

# import the types for the solution
from solution_algorithms.knapsack_types import Item

# import the GeneticAlgorithm class from your implementation
from solution_algorithms.genetic_algorithm import GeneticAlgorithm
from solution_algorithms.hill_climbing_algorithm import HillClimbingAlgorithm
from solution_algorithms.simulated_annealing_algorithm import SimulatedAnnealingAlgorithm


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Solve the knapsack problem using different algorithms.')
    parser.add_argument('--algorithm', type=str, default='ga',
                        help='algorithm to use (ga, hca, or sa)')
    parser.add_argument('--file', type=str, required=True,
                        help='path to input file')

    return parser.parse_args()


def main():
    args = parse_arguments()

    # parse the problem instance from the input file
    with open(args.file, 'r') as f:
        lines = f.readlines()
        capacity = int(lines[0])
        items = []
        for line in lines[2:]:
            item, weight, value, n_items = line.strip().split(',')
            items.append(Item(name=item, weight=float(weight),
                         value=float(value), n_items=int(n_items)))

    # create an instance of the selected algorithm and solve the problem
    if args.algorithm == 'ga':
        ga = GeneticAlgorithm(items, capacity)
        best_fitness, solution = ga.run()

        # print the solution
        print(f'Optimal value: {best_fitness}')
        print(
            f'Items in knapsack: {", ".join(str(i) for i in solution)}')

    elif args.algorithm == 'hca':
        hca = HillClimbingAlgorithm(items, capacity)
        best_value, solution = hca.run()

        # print the solution
        print(f'Optimal value: {best_value}')
        print(
            f'Items in knapsack: {", ".join(str(i) for i in solution)}')

    elif args.algorithm == 'sa':
        sa = SimulatedAnnealingAlgorithm(items, capacity)
        best_value, solution = sa.run()

        # print the solutions
        print(f'Optimal value: {best_value}')
        print(
            f'Items in knapsack: {", ".join(str(i) for i in solution)}')
    else:
        print('Chosen algorithm can only be one of: sa, hca, ga.')



if __name__ == '__main__':
    main()
