def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(1, n +1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

weights = [2, 3, 4, 5]    # Trọng lượng từng vật
values = [3, 4, 5, 6]     # Giá trị từng vật
W = 8                     # Trọng lượng tối đa của túi

print("Trọng lượng:", weights)
print("Giá trị:", values)
print("Trọng lượng tối đa:", W)
print("Giá trị lớn nhất có thể đạt được:", knapsack(weights, values, W))
