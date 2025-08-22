# Prefix sum implementation
# Create a new array with cumulative sums

# If arr = [1, 2, 3, 4, 5, 6]
# Then output = [1, 3, 6, 10, 15, 21]

def calculate_prefix_sum(arr):
    """
    Calculate the prefix sum array where each element at index i
    is the sum of all elements from index 0 to i in the original array.
    
    Args:
        arr: List of numbers
        
    Returns:
        List: Prefix sum array
    """
    prefix = []  # Initialize empty prefix array
    
    for i in range(len(arr)):
        if i == 0:
            # First element: just the first element itself
            prefix.append(arr[i])
        else:
            # Current element + previous prefix sum
            prefix.append(arr[i] + prefix[i-1])
    
    return prefix

# Test the function
def main():
    # Test case 1
    arr1 = [1, 2, 3, 4, 5, 6]
    prefix1 = calculate_prefix_sum(arr1)
    
    print("Original array:", arr1)
    print("Prefix sum array:", prefix1)
    print("Expected: [1, 3, 6, 10, 15, 21]")
    print()
    
    # Test case 2 - with negative numbers
    arr2 = [-2, 0, 3, -5, 2, -1]
    prefix2 = calculate_prefix_sum(arr2)
    
    print("Original array:", arr2)
    print("Prefix sum array:", prefix2)
    print("Expected: [-2, -2, 1, -4, -2, -3]")
    print()
    
    # Test case 3 - empty array
    arr3 = []
    prefix3 = calculate_prefix_sum(arr3)
    
    print("Original array:", arr3)
    print("Prefix sum array:", prefix3)
    print("Expected: []")
    print()
    
    # Test case 4 - single element
    arr4 = [7]
    prefix4 = calculate_prefix_sum(arr4)
    
    print("Original array:", arr4)
    print("Prefix sum array:", prefix4)
    print("Expected: [7]")
    print()
    
    # Print all prefix sum elements as in the JavaScript version
    print("Printing each element of prefix sum array for arr1:")
    for i in range(len(prefix1)):
        print(prefix1[i])

# Alternative implementation using list comprehension (more Pythonic)
def calculate_prefix_sum_pythonic(arr):
    """
    More Pythonic implementation using list comprehension and enumerate.
    """
    prefix = []
    for i, num in enumerate(arr):
        if i == 0:
            prefix.append(num)
        else:
            prefix.append(num + prefix[i-1])
    return prefix

# Even more concise version using itertools.accumulate
import itertools

def calculate_prefix_sum_itertools(arr):
    """
    Implementation using itertools.accumulate - the most Pythonic way.
    """
    return list(itertools.accumulate(arr))

if __name__ == "__main__":
    main()
    
    # Demonstrate the different implementations
    print("\n" + "="*50)
    print("COMPARING DIFFERENT IMPLEMENTATIONS")
    print("="*50)
    
    test_arr = [1, 2, 3, 4, 5]
    
    print("Original array:", test_arr)
    print("Method 1 (basic):", calculate_prefix_sum(test_arr))
    print("Method 2 (pythonic):", calculate_prefix_sum_pythonic(test_arr))
    print("Method 3 (itertools):", calculate_prefix_sum_itertools(test_arr))