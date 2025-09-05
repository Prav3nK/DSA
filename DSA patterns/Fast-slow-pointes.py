# Understanding the Fast and Slow Pointers Pattern

# The Fast and Slow Pointers pattern involves using two pointers that iterate through a data structure at different speeds. 
# Typically, the “slow” pointer moves one step at a time, while the “fast” pointer moves two steps. 
# This approach helps in detecting cycles and finding midpoints in linked lists and arrays.

# 1. Check cycle in a link list

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    

# Example 

#2. Middle of the Linked List 
#   Initialize two pointers, slow and fast.
#   Initialize two pointers, slow and fast.
#   Move slow one step at a time and fast two steps.
#   If there is a cycle, slow and fast will eventually meet.
#   If fast reaches the end of the list (null), there is no cycle.

class Solution:
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
#   3. Palindrome Linked List (Leetcode 234):

#   Given the head of a singly linked list, return true if it is a palindrome or false otherwise

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse(slow)
        fast = head
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

    def reverse(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
    
#   Exampel 4 
#   Happy Number ( Leetcode 202 ):

#   Write an algorithm to determine if a number n is happy.

#   A happy number is a number defined by the following process:
#   Starting with any positive integer, replace the number by the sum of the squares of its digits.
#   Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#   Those numbers for which this process ends in 1 are happy.

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return fast == 1

    def get_next(self, n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit * digit
        return total_sum