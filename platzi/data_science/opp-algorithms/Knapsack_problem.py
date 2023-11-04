import random

def knapsack(capacity, weights, values):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] #full 0 2d array
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
                # i.e capacity = 3, weights=[1,2]
                # 0  0  0
                # 0  1  1
                # 0  1  3
                # 0  1  3
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]


def main():
    capacity = random.randint(1, 20)
    weights = [random.randint(1, 10) for _ in range(random.randint(1, 20))]
    values = [random.randint(1, 10) for _ in range(len(weights))]
    print(knapsack(capacity, weights, values))

if __name__ == '__main__':
    main()
