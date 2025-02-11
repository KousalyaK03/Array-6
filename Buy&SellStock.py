# Approach:
# 1. Use a single pass to track the minimum price encountered so far.
# 2. Calculate the potential profit at each step by selling at the current price.
# 3. Keep track of the maximum profit found.
# 4. Return the maximum profit after iterating through the list.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Initialize variables
        min_price = float('inf')  # Track the lowest price seen so far
        max_profit = 0  # Track the maximum profit achievable

        # Step 2: Iterate through the price list
        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum price if a lower one is found
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate and update max profit

        # Step 3: Return the maximum profit found
        return max_profit

# Time Complexity: O(N), where N is the length of the prices array.
# - We iterate through the array once, making it linear time complexity.

# Space Complexity: O(1), since we only use a few extra variables.