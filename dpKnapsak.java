public class dpKnapsak {

    public static void main(String[] args) {
        int[] values = { 65, 100, 120 };
        int[] weights = { 1, 2, 3 };
        int size = 5;
        int n = values.length;
        // enter the values and weights in the array

        System.out.println("Maximum value: " + unboundedKnapsack(values, weights, size));
    }

    public static int unboundedKnapsack(int[] values, int[] weights, int capacity) {
        int n = values.length; // weights.length;
        int[] dp = new int[capacity + 1];

        for (int i = 0; i <= capacity; i++) {
            for (int j = 0; j < n; j++) {
                if (weights[j] <= i) {
                    dp[i] = Math.max(dp[i], dp[i - weights[j]] + values[j]);
                }
            }
        }
        return dp[capacity];
    }
}
