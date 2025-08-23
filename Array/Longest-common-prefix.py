# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # Shorten the prefix until it matches the beginning of current string
            while not current_string.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                
                # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""
        
        return prefix

# Simple test cases
solution = Solution()

# Test Case 1
strs1 = ["flower", "flow", "flight"]
result1 = solution.longestCommonPrefix(strs1)
print(f'Input: {strs1}')
print(f'Output: "{result1}"')
print(f'Expected: "fl"')
print(f'Test 1: {"PASS" if result1 == "fl" else "FAIL"}')
print()

# Test Case 2
strs2 = ["dog", "racecar", "car"]
result2 = solution.longestCommonPrefix(strs2)
print(f'Input: {strs2}')
print(f'Output: "{result2}"')
print(f'Expected: ""')
print(f'Test 2: {"PASS" if result2 == "" else "FAIL"}')