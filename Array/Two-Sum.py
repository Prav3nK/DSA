# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums [i]
            if complement in hashmap and hashmap[complement] != i :
                return [i, hashmap[complement]]
        return []

# Test cases
def test_twoSum():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test 1 - Input: {nums1}, Target: {target1}")
    print(f"Expected: [0, 1], Got: {result1}")
    print(f"Pass: {sorted(result1) == [0, 1]}")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Test 2 - Input: {nums2}, Target: {target2}")
    print(f"Expected: [1, 2], Got: {result2}")
    print(f"Pass: {sorted(result2) == [1, 2]}")
    print()
    
    # Additional test case 3 - with negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    target3 = -8
    result3 = solution.twoSum(nums3, target3)
    print(f"Test 3 - Input: {nums3}, Target: {target3}")
    print(f"Expected: [2, 4], Got: {result3}")
    print(f"Pass: {sorted(result3) == [2, 4]}")
    print()
    
    # Additional test case 4 - with duplicate numbers but different indices
    nums4 = [3, 3]
    target4 = 6
    result4 = solution.twoSum(nums4, target4)
    print(f"Test 4 - Input: {nums4}, Target: {target4}")
    print(f"Expected: [0, 1], Got: {result4}")
    print(f"Pass: {sorted(result4) == [0, 1]}")
    print()
    
    # Additional test case 5 - larger array
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target5 = 17
    result5 = solution.twoSum(nums5, target5)
    print(f"Test 5 - Input: {nums5}, Target: {target5}")
    print(f"Expected: [7, 8], Got: {result5}")
    print(f"Pass: {sorted(result5) == [6, 9]}")

# Run the tests
test_twoSum()