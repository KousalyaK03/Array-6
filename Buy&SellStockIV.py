# Approach:
# 1. If k is greater than half the number of days, the problem reduces to the unlimited transactions case.
# 2. Use dynamic programming to track the maximum profit at each step.
# 3. Maintain a DP table where dp[i][j] represents the max profit at day j with at most i transactions.
# 4. Use an auxiliary variable to track the max difference to optimize calculations.
# 5. Iterate through the prices and update the DP table accordingly.
# 6. Return the maximum profit possible with at most k transactions.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0  # If no prices or no transactions allowed, return 0

        # If k is very large, reduce the problem to the unlimited transactions case
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:  # Buy low, sell high greedily
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        # Step 1: Initialize DP table
        dp = [[0] * n for _ in range(k + 1)]  # dp[i][j] = max profit with i transactions on day j

        # Step 2: Fill DP table
        for i in range(1, k + 1):
            max_diff = -prices[0]  # Track the maximum profit we can get after buying
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)  # Sell at day j or not
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])  # Update max difference

        # Step 3: Return the maximum profit with at most k transactions
        return dp[k][n - 1]

# Time Complexity: O(k * N), where k is the max transactions allowed, and N is the number of days.
# - We use a nested loop where the outer loop runs k times and the inner loop runs N times.

# Space Complexity: O(k * N), for the DP table storing the maximum profit.