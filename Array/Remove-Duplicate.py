def remove_duplicates(nums):
    """
    Remove duplicates in-place from sorted array
    Return new length of array without duplicates
    """
    if not nums:
        return 0
    
    # Slow pointer tracks the position of last unique element
    slow = 0
    
    # Fast pointer scans through the array
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1  # Length of array without duplicates

# Example usage
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print(f"New length: {new_length}")  # Output: 5
print(f"Modified array: {nums[:new_length]}")  # Output: [0, 1, 2, 3, 4]