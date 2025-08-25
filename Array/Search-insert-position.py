from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Test cases
def test_searchInsert():
    sol = Solution()
    
    # Test Case 1: Target is present in the array
    nums1 = [1, 3, 5, 6]
    target1 = 5
    result1 = sol.searchInsert(nums1, target1)
    expected1 = 2
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Test Case 1 Passed")
    
    # Test Case 2: Target is not present, should be inserted at index 1
    nums2 = [1, 3, 5, 6]
    target2 = 2
    result2 = sol.searchInsert(nums2, target2)
    expected2 = 1
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Test Case 2 Passed")
    
    # Test Case 3: Target is not present and is greater than all elements
    nums3 = [1, 3, 5, 6]
    target3 = 7
    result3 = sol.searchInsert(nums3, target3)
    expected3 = 4
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Test Case 3 Passed")
    
    print("All test cases passed!")

# Run the tests
test_searchInsert()