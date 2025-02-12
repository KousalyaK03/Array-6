# Approach:
# 1. Use dynamic programming to track three states:
#    - `hold`: Maximum profit when holding a stock (bought but not sold).
#    - `sell`: Maximum profit after selling a stock.
#    - `cooldown`: Maximum profit after a cooldown period.
# 2. At each step, update these states based on previous values:
#    - If holding a stock today, either continue holding from the previous day or buy today.
#    - If selling today, the profit is the previous hold state + today's price.
#    - If in cooldown today, the max profit is the previous sell state.
# 3. Return the maximum of `sell` and `cooldown` since we cannot end with `hold`.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0  # No prices means no profit

        n = len(prices)

        # Step 1: Initialize state variables
        hold = -prices[0]  # Holding stock means negative cost
        sell = 0  # No stock sold initially
        cooldown = 0  # No cooldown initially

        # Step 2: Iterate through the price list and update states
        for i in range(1, n):
            prev_hold = hold
            prev_sell = sell

            # Holding a stock: either continue holding or buy today
            hold = max(prev_hold, cooldown - prices[i])

            # Selling a stock today: previous hold + today's price
            sell = prev_hold + prices[i]

            # Cooldown today: take max of previous sell and previous cooldown
            cooldown = max(prev_sell, cooldown)

        # Step 3: Return the max profit (cannot be in hold state at the end)
        return max(sell, cooldown)

# Time Complexity: O(N), where N is the length of the prices array.
# - We iterate through the array once, performing constant-time operations.

# Space Complexity: O(1), since we use only a few extra variables.
