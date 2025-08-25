

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

def test_removeElement():
    sol = Solution()
    
    # Test Case 1: Basic case with multiple occurrences of val
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    expected_nums1 = [2, 2]
    assert k1 == len(expected_nums1)
    assert sorted(nums1[:k1]) == sorted(expected_nums1)
    print("Test Case 1 Passed")
    
    # Test Case 2: No occurrences of val
    nums2 = [1, 2, 3, 4]
    val2 = 5
    k2 = sol.removeElement(nums2, val2)
    expected_nums2 = [1, 2, 3, 4]
    assert k2 == len(expected_nums2)
    assert sorted(nums2[:k2]) == sorted(expected_nums2)
    print("Test Case 2 Passed")
    
    # Test Case 3: All elements are val
    nums3 = [2, 2, 2, 2]
    val3 = 2
    k3 = sol.removeElement(nums3, val3)
    expected_nums3 = []
    assert k3 == len(expected_nums3)
    assert nums3[:k3] == expected_nums3
    print("Test Case 3 Passed")
    
    # Test Case 4: Mixed elements with val at different positions
    nums4 = [0, 1, 2, 2, 3, 0, 4, 2]
    val4 = 2
    k4 = sol.removeElement(nums4, val4)
    expected_nums4 = [0, 1, 3, 0, 4]
    assert k4 == len(expected_nums4)
    assert sorted(nums4[:k4]) == sorted(expected_nums4)
    print("Test Case 4 Passed")
    
    print("All test cases passed!")

# Run the tests
test_removeElement()