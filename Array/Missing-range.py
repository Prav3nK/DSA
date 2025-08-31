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