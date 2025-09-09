# 252. Meeting Rooms
# Easy
# Topics
# conpanies iconCompanies

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true


from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort the intervals by the start time
        intervals.sort(key=lambda x: x[0])
        
        # Check each meeting with the next one
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True