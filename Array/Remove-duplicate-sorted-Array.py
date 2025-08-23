# 26. Remove Duplicates from Sorted Array


# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

#     Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#     Return k.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).



from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the position of the last unique element
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

# Test the solution with the given examples
def test_solution():
    solution = Solution()
    
    # Test Case 1
    print("Test Case 1:")
    nums1 = [1, 1, 2]
    print(f"Input: nums = {nums1}")
    k1 = solution.removeDuplicates(nums1)
    print(f"Output: {k1}, nums = {nums1[:k1]}{['_'] * (len(nums1) - k1) if len(nums1) > k1 else []}")
    print(f"Expected: 2, nums = [1, 2, _]")
    print(f"Result: {'✓ PASS' if k1 == 2 and nums1[:2] == [1, 2] else '✗ FAIL'}")
    print()
    
    # Test Case 2
    print("Test Case 2:")
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Input: nums = {nums2}")
    k2 = solution.removeDuplicates(nums2)
    print(f"Output: {k2}, nums = {nums2[:k2]}{['_'] * (len(nums2) - k2) if len(nums2) > k2 else []}")
    print(f"Expected: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]")
    print(f"Result: {'✓ PASS' if k2 == 5 and nums2[:5] == [0, 1, 2, 3, 4] else '✗ FAIL'}")
    print()
    
    # Additional test cases
    print("Additional Test Cases:")
    
    # Test Case 3: Empty array
    nums3 = []
    k3 = solution.removeDuplicates(nums3)
    print(f"Empty array: k = {k3}, {'✓ PASS' if k3 == 0 else '✗ FAIL'}")
    
    # Test Case 4: Single element
    nums4 = [5]
    k4 = solution.removeDuplicates(nums4)
    print(f"Single element: k = {k4}, nums = {nums4[:k4]}, {'✓ PASS' if k4 == 1 and nums4[0] == 5 else '✗ FAIL'}")
    
    # Test Case 5: All duplicates
    nums5 = [2, 2, 2, 2, 2]
    k5 = solution.removeDuplicates(nums5)
    print(f"All duplicates: k = {k5}, nums = {nums5[:k5]}, {'✓ PASS' if k5 == 1 and nums5[0] == 2 else '✗ FAIL'}")
    
    # Test Case 6: No duplicates
    nums6 = [1, 2, 3, 4, 5]
    k6 = solution.removeDuplicates(nums6)
    print(f"No duplicates: k = {k6}, nums = {nums6[:k6]}, {'✓ PASS' if k6 == 5 and nums6 == [1, 2, 3, 4, 5] else '✗ FAIL'}")

# Run the tests
if __name__ == "__main__":
    test_solution()