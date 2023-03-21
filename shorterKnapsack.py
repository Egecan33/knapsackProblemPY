def knapsack_problem(values, weights, max_weight):
    num_items = len(values)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[num_items][max_weight]


if __name__ == "__main__":
    # Changeable parameters
    values = [60, 100, 120]
    weights = [10, 20, 30]
    max_weight = 50

    max_value = knapsack_problem(values, weights, max_weight)
    print(f"The maximum value that can be obtained is: {max_value}")
