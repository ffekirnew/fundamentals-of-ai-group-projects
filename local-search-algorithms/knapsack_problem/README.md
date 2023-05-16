# Knapsack (30 pts)

## Problem Statement
The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item included in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

Write three algorithms (Genetic Algorithm, Hill Climbing, and Simulated Annealing) to solve the knapsack problem. Your algorithm should take a file on the command line in the following fashion:
	
	python knapsack.py --algorithm ga --file my-file.txt

The input file should have content in the following style

    50
    Item,weight,value, n_items
    Phone,0.19,1000, 5
    Laptop,1.1,700, 2

The first line in the content is the maximum weight in kilograms that your knapsack can handle. The second line is the headers of the succeeding lines and your algorithm should ignore it. The third and onwards should have a comma-separated list of an item’s name, its weight in kilogram, and the item's value in USD. The list should contain 10, 15, and 20 items. It might be tiresome to write 20 items, hence, write some randomized program that generates such a list for you.

## Solution
Our solution contains all of the implementations of the algorithms in the `solution_algorithms` folder.
