import java.util.Arrays;
import java.util.Comparator;

class Item {
    int value;
    int weight;
    double ratio;

    public Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) value / weight;
    }
}

public class greedyHeuristic {

    public static int knapsackGreedy(Item[] items, int maxWeight) {
        // Sort items by value-to-weight ratio in descending order
        Arrays.sort(items, Comparator.comparingDouble((Item item) -> item.ratio).reversed());

        int totalValue = 0;
        int currentWeight = 0;

        for (Item item : items) {
            if (currentWeight + item.weight <= maxWeight) {
                currentWeight += item.weight;
                totalValue += item.value;
            } else {
                // If the remaining space is not enough for the whole item, add a fraction of
                // the item
                int remainingWeight = maxWeight - currentWeight;
                totalValue += item.value * remainingWeight / item.weight;
                break;
            }
        }

        return totalValue;
    }

    public static void main(String[] args) {
        // Changeable parameters
        int[] values = { 60, 100, 120 };
        int[] weights = { 10, 20, 30 };
        int maxWeight = 50;

        Item[] items = new Item[values.length];
        for (int i = 0; i < values.length; i++) {
            items[i] = new Item(values[i], weights[i]);
        }

        int maxValue = knapsackGreedy(items, maxWeight);
        System.out.println("The maximum value that can be obtained using the greedy heuristic is: " + maxValue);
    }
}
