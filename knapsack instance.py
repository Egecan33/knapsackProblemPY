import random


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


# Set the weight capacity of the knapsack
capacity = 50

# Set the number of objects to generate
num_objects = 10

# Generate random weights and values for each object
items = [Item(random.randint(1, 10), random.randint(1, 10)) for i in range(num_objects)]

# Print the weights and values of the generated items
for i, item in enumerate(items):
    print("Item", i + 1, ": Weight:", item.weight, "Value:", item.value)
