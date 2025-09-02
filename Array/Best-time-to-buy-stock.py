# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.





from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if we sell at current price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices1}")
    print(f"Output: {sol.maxProfit(prices1)}")  # Expected: 5
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: {prices2}")
    print(f"Output: {sol.maxProfit(prices2)}")  # Expected: 0
    
    # Additional test cases
    prices3 = [1, 2, 3, 4, 5]
    print(f"Input: {prices3}")
    print(f"Output: {sol.maxProfit(prices3)}")  # Expected: 4
    
    prices4 = [3, 2, 1]
    print(f"Input: {prices4}")
    print(f"Output: {sol.maxProfit(prices4)}")  # Expected: 0