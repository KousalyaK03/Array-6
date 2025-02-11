# Approach:
# 1. We can make at most two transactions, meaning we need to track two buy and sell operations.
# 2. Maintain four variables:
#    - first_buy: Minimum cost to buy the first stock.
#    - first_profit: Maximum profit after selling the first stock.
#    - second_buy: Effective cost of buying the second stock after the first profit.
#    - second_profit: Maximum profit after selling the second stock.
# 3. Iterate through the prices array and update these four variables to maximize profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Initialize variables
        first_buy = float('inf')  # Lowest price to buy the first stock
        first_profit = 0  # Maximum profit after first sale
        second_buy = float('inf')  # Effective second buy price after first profit
        second_profit = 0  # Maximum profit after second sale

        # Step 2: Iterate through the price list
        for price in prices:
            # Buy the first stock at the minimum price
            first_buy = min(first_buy, price)

            # Sell the first stock at the maximum profit
            first_profit = max(first_profit, price - first_buy)

            # Buy the second stock considering the first profit as a discount
            second_buy = min(second_buy, price - first_profit)

            # Sell the second stock at the maximum profit
            second_profit = max(second_profit, price - second_buy)

        # Step 3: Return the maximum profit after two transactions
        return second_profit

# Time Complexity: O(N), where N is the length of the prices array.
# - We iterate through the array once, making it linear time complexity.

# Space Complexity: O(1), since we only use a few extra variables.