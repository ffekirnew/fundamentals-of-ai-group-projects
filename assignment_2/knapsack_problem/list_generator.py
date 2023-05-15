import random

from typing import List


def generate_items(n: int) -> List[tuple]:
    """
    The generate_items function generates a list of items with the following attributes:
        name - string, e.g. 'Item 1'
        weight - float, e.g. 0.5
        value - int, e.g., 100
        n_items - int, number of items available to pack in knapsack

    :param n: Generate n items
    :return: A list of tuples
    """
    items = []
    for i in range(n):
        name = f'Item{i + 1}'
        weight = round(random.uniform(0.1, 5.0), 2)
        value = random.randint(1, 1000)
        n_items = random.randint(1, 5)
        items.append((name, weight, value, n_items))
    return items


def save_to_file(items: List[tuple], filename: str) -> None:
    """The save_to_file function takes a list of tuples and a filename as input.
    It then writes the maximum weight to the first line of the file, followed by
    a header on the second line. The rest of each line is filled with data from
    the list of tuples in order.

    :param items: List[tuple]: Pass a list of tuples to the function
    :param filename: str: Specify the name of the file to save to
    :return: None, it just writes to a file
    """
    with open(filename, 'w') as f:
        max_weight = round(random.uniform(5.0, 20.0), 2)
        f.write(f'{max_weight}\n')
        f.write('Item,weight,value,n_items\n')
        for name, weight, value, n_items in items:
            f.write(f'{name},{weight},{value},{n_items}\n')


def generate_input_files():
    """The generate_input_files function generates three input files for testing the program.
    The first file contains 10 items, the second 15 items and the third 20 items.


    :return: The input files' names
    """
    file_names = ['input_files/input10.txt', 'input_files/input15.txt', 'input_files/input20.txt']
    save_to_file(generate_items(10), file_names[0])
    save_to_file(generate_items(15), file_names[1])
    save_to_file(generate_items(20), file_names[2])

    return file_names
