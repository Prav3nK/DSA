# <!-- We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious

# among all its possible subsequences.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Explanation:

# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0

# Explanation:

# No harmonic subsequence exists -->
# <!-- 
# To solve this problem, we need to find the length of the longest harmonious subsequence in an array. A harmonious array is defined as an array where the difference between the maximum value and the minimum value is exactly 1. Note that the subsequence does not need to be contiguous, but the elements must be in the same relative order as in the original array. However, since we are allowed to choose any subsequence, we can consider the frequency of numbers and their adjacent values.
# Approach

#     Frequency Count: First, we count the frequency of each number in the array. This helps us to quickly access how many times each number appears.

#     Check Adjacent Pairs: For each unique number in the array, we check if there exists a number that is exactly one greater than the current number. For each such pair (x and x+1), the length of the harmonious subsequence that can be formed is the sum of the frequencies of x and x+1.

#     Maximize Length: We iterate through all such pairs and keep track of the maximum length found. If no such pair exists, we return 0. -->

from collections import defaultdict
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        max_length = 0
        for num in freq:
            if num + 1 in freq:
                current_length = freq[num] + freq[num + 1]
                if current_length > max_length:
                    max_length = current_length
        return max_length