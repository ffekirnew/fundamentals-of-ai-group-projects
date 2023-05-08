from typing import List
from collections import namedtuple

Item = namedtuple('Item', ['name', 'weight', 'value', 'n_items'])
Items = List[Item]
WeightLimit = int

Gene = int
Individual = List[Gene]
Population = List[Individual]
Fitness = int
