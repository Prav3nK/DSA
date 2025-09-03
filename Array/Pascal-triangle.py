# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]



from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]  # First row
        
        for i in range(1, numRows):
            prev_row = triangle[i-1]
            new_row = [1]  # First element is always 1
            
            # Calculate middle elements
            for j in range(1, i):
                new_row.append(prev_row[j-1] + prev_row[j])
            
            new_row.append(1)  # Last element is always 1
            triangle.append(new_row)
        
        return triangle

# Test the solution
solution = Solution()

# Test case 1
print(solution.generate(5))
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Test case 2
print(solution.generate(1))
# Output: [[1]]

# Test case 3
print(solution.generate(0))
# Output: []

# Test case 4
print(solution.generate(3))
# Output: [[1],[1,1],[1,2,1]]