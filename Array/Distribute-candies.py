# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

 

# Example 1:

# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

# Example 2:

# Input: candyType = [1,1,2,3]
# Output: 2
# Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

# Example 3:

# Input: candyType = [6,6,6,6]
# Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.


# Approach

#     Understand the Problem: Alice has n candies (with n being even) and she can only eat n/2 candies. She wants to maximize the number of distinct types she consumes.

#     Key Insight: The maximum distinct types she can eat is limited by two factors:

#         The number of distinct candy types available (let this be distinctCount).

#         The number of candies she is allowed to eat (n/2).

#     Conclusion: She can eat at most min(distinctCount, n/2) different types. For example:

#         If there are more distinct types than allowed candies, she can only eat n/2 distinct types (each candy of a different type).

#         If there are fewer distinct types than allowed candies, she can eat all distinct types (and some duplicates, but that doesn't increase the distinct count).

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        distinct_count = len(set(candyType))
        return min(distinct_count, n // 2)