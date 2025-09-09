# 243. Shortest Word Distance
# Easy
# Topics
# conpanies iconCompanies

# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3

# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1

 

# Constraints:

#     2 <= wordsDict.length <= 3 * 104
#     1 <= wordsDict[i].length <= 10
#     wordsDict[i] consists of lowercase English letters.
#     word1 and word2 are in wordsDict.
#     word1 != word2

from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -1
        min_distance = float('inf')
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i
            if word == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
        
        return min_distance
