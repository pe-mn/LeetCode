# Linked List 
# ------------
# https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/
# https://www.geeksforgeeks.org/linked-list-set-1-introduction/
# https://www.geeksforgeeks.org/data-structures/linked-list/

# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/451815/JavaPython-3-Simulate-binary-operations.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # ans = 0
        # while head:
        #     ans = (ans << 1) | head.val
        #     head = head.next
        # return ans
    
# Use walrus operator in Python 3.8:
        # ans = head.val
        # while head := head.next:
        #     ans = ans << 1 | head.val
        # return ans
        
# Loop through the linked list and added value to answer.
        ans = 0
        while head: 
            ans = 2*ans + head.val 
            head = head.next 
        return ans 
    
# num = 2^n*(1or0) + 2^(n-1)(1or0)...
# with every loop, all previous n increase by 1, which equals num2

# By multiplying it with 2 every time, we are effectively shifting the bits to the left by one. So at the end, every bit lands at its rightful place.



        