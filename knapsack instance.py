import random


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


class RandomKnapsack:
    def __init__(self, num_objects, capacity):
        self.num_objects = num_objects
        self.capacity = capacity
        self.items = [
            ## Create a random item with a random weight and value
            Item(random.randint(1, 10), random.randint(1, 10))
            for i in range(num_objects)
        ]

    def print_items(self):
        for i, item in enumerate(self.items):
            print("Item", i + 1, ": Weight:", item.weight, "Value:", item.value)


# Create a RandomKnapsack instance with 10 items and a capacity of 50
rk = RandomKnapsack(10, 50)

# Print the weights and values of the generated items
rk.print_items()
