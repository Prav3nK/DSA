from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# Test the solution
solution = Solution()

# Test case 1
nums1 = [1,2,3,0,0,0]
solution.merge(nums1, 3, [2,5,6], 3)
print(nums1)  # [1,2,2,3,5,6]

# Test case 2
nums1 = [1]
solution.merge(nums1, 1, [], 0)
print(nums1)  # [1]

# Test case 3
nums1 = [0]
solution.merge(nums1, 0, [1], 1)
print(nums1)  # [1]