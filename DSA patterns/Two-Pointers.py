# 2. Two Pointers

# The Two Pointers pattern involves using two pointers to iterate through an array or list, often used to find pairs or elements that meet specific criteria.

# Use this pattern when dealing with sorted arrays or lists where you need to find pairs that satisfy a specific condition.
# Sample Problem:

# Find two numbers in a sorted array that add up to a target value.

# Example:

#     Input: nums = [1, 2, 3, 4, 6], target = 6
#     Output: [1, 3]

# Explanation:

#     Initialize two pointers, one at the start (left) and one at the end (right) of the array.
#     Check the sum of the elements at the two pointers.
#     If the sum equals the target, return the indices.
#     If the sum is less than the target, move the left pointer to the right.
#     If the sum is greater than the target, move the right pointer to the left.



# When to Use:

#     Array is sorted (or can be sorted)

#     Looking for pairs/triplets that satisfy conditions

#     Need to traverse from both ends towards middle

#     In-place operations required



def two_sum_sorted(numbers, target):
    """
    Find two numbers in sorted array that sum to target
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0  # Pointer starting from beginning
    right = len(numbers) - 1  # Pointer starting from end
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-indexed indices
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, move left pointer right
            left += 1
        else:
            # Sum is too large, move right pointer left
            right -= 1
    
    return []  # No solution found

# Example usage
numbers = [2, 7, 11, 15]
target = 9
result = two_sum_sorted(numbers, target)
print(f"Indices: {result}")  # Output: [1, 2] (numbers[0] + numbers[1] = 2 + 7 = 9)