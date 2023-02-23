import random


class Item:
    def __init__(self, index, weight, value):
        self.index = index
        self.weight = weight
        self.value = value


class RandomKnapsack:
    def __init__(self, num_objects, capacity):
        self.num_objects = num_objects
        self.capacity = capacity
        self.items = [
            ## Create a random item with a random weight and value
            Item(index=i + 1, weight=random.randint(1, 10), value=random.randint(1, 10))
            for i in range(num_objects)
        ]

    def select_itemsR(self):
        self.selected_items = []
        total_weight = 0
        total_value = 0
        while total_weight <= self.capacity:
            # Select a random unselected item
            item = random.choice(self.items)
            # Check if the item fits in the knapsack
            if item.index not in [i.index for i in self.selected_items]:
                if total_weight + item.weight <= self.capacity:
                    self.selected_items.append(item)
                    total_weight += item.weight
                    total_value += item.value
                else:
                    print(
                        "Item "
                        + str(item.index)
                        + " with value "
                        + str(item.value)
                        + " with weight "
                        + str(item.weight)
                        + " is too heavy to be added to the knapsack.",
                    )
                    break
        print("Selected Items:")
        for item in self.selected_items:
            print("Item", item.index, ": Weight:", item.weight, "Value:", item.value)
        print("Total Value of Selected Items:", total_value)

    def print_items(self):
        for i, item in enumerate(self.items):
            print("Item", item.index, ": Weight:", item.weight, "Value:", item.value)


# Create a RandomKnapsack instance with 10 items and a capacity of 50
rk = RandomKnapsack(10, 20)

# Print the weights and values of the generated items
rk.print_items()

# Select the items to put in the knapsack
rk.select_itemsR()

print("End")
