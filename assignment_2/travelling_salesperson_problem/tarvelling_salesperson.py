import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Solve the travelling salesperson problem using different algorithms.')
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
