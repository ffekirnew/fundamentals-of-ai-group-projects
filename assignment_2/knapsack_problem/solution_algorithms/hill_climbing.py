from knapsack_types import Items, WeightLimit

class HillClimbing:
    def __init__(self, items: Items, weight_limit: WeightLimit) -> None:
        self.items: Items = items
        self.weight_limit: WeightLimit = weight_limit

    