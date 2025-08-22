class NumArray:
    def __init__(self, nums: list):
        """
        Initialize the NumArray object with the integer array nums.
        
        We create a prefix sum array where:
        - prefix[0] = 0
        - prefix[i] = sum of nums[0] to nums[i-1]
        
        This allows us to compute any range sum in constant time.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Initialize prefix sum array with length n+1
        self.prefix = [0] * (len(nums) + 1)
        
        # Build the prefix sum array
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
    
    def sumRange(self, left: int, right: int) -> int:
        """
        Returns the sum of elements between indices left and right inclusive.
        
        Using the prefix sum array:
        sum = prefix[right + 1] - prefix[left]
        
        prefix[right + 1] = sum of elements from index 0 to right
        prefix[left] = sum of elements from index 0 to left-1
        
        Time Complexity: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]


# Test function to demonstrate the solution
def test_num_array():
    """
    Test function to verify the implementation works correctly.
    """
    # Test case 1
    nums1 = [-2, 0, 3, -5, 2, -1]
    num_array1 = NumArray(nums1)
    
    print("Input array:", nums1)
    print("Prefix array:", num_array1.prefix)
    print()
    
    # Test various ranges
    test_cases = [
        (0, 2, 1),    # -2 + 0 + 3 = 1
        (2, 5, -1),   # 3 + (-5) + 2 + (-1) = -1
        (0, 5, -3),   # Sum of all elements = -3
        (1, 4, 0),    # 0 + 3 + (-5) + 2 = 0
        (3, 3, -5),   # Single element: -5
        (0, 0, -2),   # Single element: -2
    ]
    
    print("Testing range queries:")
    print("-" * 40)
    for left, right, expected in test_cases:
        result = num_array1.sumRange(left, right)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"sumRange({left}, {right}) = {result} (Expected: {expected}) {status}")
    print()
    
    # Test case 2: Empty array (edge case)
    print("Testing edge case - empty array:")
    print("-" * 40)
    try:
        nums2 = []
        num_array2 = NumArray(nums2)
        print("Empty array handled successfully")
        print("Prefix array:", num_array2.prefix)
    except Exception as e:
        print(f"Error with empty array: {e}")
    print()
    
    # Test case 3: Single element array
    print("Testing edge case - single element array:")
    print("-" * 40)
    nums3 = [5]
    num_array3 = NumArray(nums3)
    print("Input array:", nums3)
    print("Prefix array:", num_array3.prefix)
    print("sumRange(0, 0) =", num_array3.sumRange(0, 0), "(Expected: 5)")
    print()


# Alternative function-based implementation
def create_prefix_sum(nums):
    """
    Creates a prefix sum array from the given nums array.
    
    Args:
        nums: List of integers
        
    Returns:
        List: Prefix sum array of length len(nums) + 1
    """
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix


def range_sum_query(left, right, prefix):
    """
    Returns the sum of elements between left and right indices using prefix array.
    
    Args:
        left: Starting index (inclusive)
        right: Ending index (inclusive)
        prefix: Prefix sum array
        
    Returns:
        int: Sum of elements from left to right
    """
    return prefix[right + 1] - prefix[left]


# Demonstration of the function-based approach
def demo_function_approach():
    """
    Demonstrates the function-based approach as an alternative to the class-based solution.
    """
    print("Function-based approach demonstration:")
    print("-" * 50)
    
    nums = [-2, 0, 3, -5, 2, -1]
    prefix = create_prefix_sum(nums)
    
    print("Input array:", nums)
    print("Prefix array:", prefix)
    print()
    
    # Test the same ranges as before
    test_ranges = [(0, 2), (2, 5), (0, 5), (1, 4)]
    
    for left, right in test_ranges:
        result = range_sum_query(left, right, prefix)
        print(f"Range [{left}, {right}]: sum = {result}")


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("RANGE SUM QUERY IMPLEMENTATION")
    print("=" * 60)
    print()
    
    # Test the class-based implementation
    test_num_array()
    
    # Demonstrate the function-based approach
    demo_function_approach()
    
    print()
    print("=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)