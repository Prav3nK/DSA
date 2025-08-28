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