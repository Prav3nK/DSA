# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:

# Input: rowIndex = 0
# Output: [1]

# Example 3:

# Input: rowIndex = 1
# Output: [1,1]



from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Start with the first element which is always 1
        
        # Build the row using the mathematical formula
        for i in range(1, rowIndex + 1):
            # Calculate next element: previous element * (n - k + 1) / k
            next_val = row[-1] * (rowIndex - i + 1) // i
            row.append(next_val)
        
        return row

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [0, 1, 2, 3, 4, 5]
    
    for rowIndex in test_cases:
        result = sol.getRow(rowIndex)
        print(f"Row {rowIndex}: {result}")