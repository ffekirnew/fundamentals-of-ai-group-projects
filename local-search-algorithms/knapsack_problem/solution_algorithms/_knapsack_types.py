from typing import List
from collections import namedtuple

Item = namedtuple('Item', ['name', 'weight', 'value', 'n_items'])
Items = List[Item]
WeightLimit = float

# Genetic Algorithm Types
Gene = int
Individual = List[Gene]
Population = List[Individual]
Fitness = int

# Hill-climbing Types
Solution = List[int]
Solutions = List[Solution]
Bit = int
Value = int

# Simulated Annealing Types
Temperature = float
