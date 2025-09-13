# 448. Find All Numbers Disappeared in an Array
# Solved
# Easy
# Topics
# conpanies iconCompanies
# Hint

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:

# Input: nums = [1,1]
# Output: [2]

 

# Constraints:

#     n == nums.length
#     1 <= n <= 105
#     1 <= nums[i] <= n

# # 
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]  # mark as visited

        # Collect indices that were never marked
        return [i + 1 for i, val in enumerate(nums) if val > 0]
