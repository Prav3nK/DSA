# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

 

 

# Example 1:

# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]
# Explanation: The ranges are:
# [2,2]
# [4,49]
# [51,74]
# [76,99]

# Example 2:

# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing numbers.


from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        result = []
        
        # If the list is empty, the entire range is missing
        if n == 0:
            return [[lower, upper]]
        
        # Check the gap from lower to the first element
        if lower < nums[0]:
            result.append([lower, nums[0] - 1])
        
        # Check gaps between consecutive elements
        for i in range(n - 1):
            if nums[i+1] - nums[i] > 1:
                result.append([nums[i] + 1, nums[i+1] - 1])
        
        # Check the gap from the last element to upper
        if nums[-1] < upper:
            result.append([nums[-1] + 1, upper])
        
        return result