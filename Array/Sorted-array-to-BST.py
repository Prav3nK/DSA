
# Given an integer array nums where the elements are sorted in ascending order, convert it to a

# binary search tree.

 

# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            return node
        
        return build_tree(0, len(nums) - 1)

# Helper function to print tree in level order
def print_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
solution = Solution()

# Test 1
nums1 = [-10, -3, 0, 5, 9]
tree1 = solution.sortedArrayToBST(nums1)
print(print_level_order(tree1))  # [0, -3, 9, -10, None, 5]

# Test 2
nums2 = [1, 3]
tree2 = solution.sortedArrayToBST(nums2)
print(print_level_order(tree2))  # [3, 1] or [1, None, 3]