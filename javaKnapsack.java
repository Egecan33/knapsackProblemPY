public class javaKnapsack {

    public static int knapsackProblem(int[] values, int[] weights, int maxWeight) {
        int numItems = values.length;
        int[][] dp = new int[numItems + 1][maxWeight + 1];

        for (int i = 1; i <= numItems; i++) {
            for (int w = 0; w <= maxWeight; w++) {
                if (weights[i - 1] <= w) {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        return dp[numItems][maxWeight];
    }

    public static void main(String[] args) {
        // Changeable parameters
        int[] values = { 60, 100, 120 };
        int[] weights = { 10, 20, 30 };
        int maxWeight = 50;

        int maxValue = knapsackProblem(values, weights, maxWeight);
        System.out.println("The maximum value that can be obtained is: " + maxValue);
    }
}
