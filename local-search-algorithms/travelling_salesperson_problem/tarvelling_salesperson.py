import argparse

# PROBLEM STATEMENT #
# You are given the Romania map, and you are asked to come up with the shortest path to visit all the cities using a local search algorithm.

# Important:
# - It's fine for some of the constraints to be broken (revisit cities in the Tsp)
# in local search as they are not guaranteed in the first place.
# - But, especially in GA, your crossover & mutation function should avoid the
# repetition of cities & creation of new edges as much as possible.

# The plain TSP is easy and there are too many implementations on the internet
# based on local search algorithms. I specifically gave you the Romania graph
# instead of a nice randomly generated graph so that you can come up with a bit
# of creativity in the algorithms you write.

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Solve the travelling salesperson problem using different algorithms.')
    parser.add_argument('--algorithm', type=str, default='ga',
                        help='algorithm to use (ga, hc, or sa)')
    parser.add_argument('--file', type=str, required=True,
                        help='path to input file')

    return parser.parse_args()


def main():
    args = parse_arguments()

    # parse the problem instance from the input file
    with open(args.file, 'r') as f:
        # do something with the file here
        pass

    # create an instance of the selected algorithm and solve the problem
    if args.algorithm == 'ga':
        # TODO: Implement the genetic algorithm solution and use it here
        pass

    elif args.algorithm == 'hc':
        # TODO: Implement the hill climbing algorithm and use it here
        pass

    elif args.algorithm == 'sa':
        # TODO: Implement the simulated annealing algorithm and use it here
        pass


if __name__ == '__main__':
    main()
