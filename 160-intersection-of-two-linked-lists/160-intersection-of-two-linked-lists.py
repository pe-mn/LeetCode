# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         if headA is None or headB is None:
#             return None

#         pa = headA # 2 pointers
#         pb = headB
#         while pa is not pb:
#             # if either pointer hits the end, switch head and continue the second traversal, 
#             # if not hit the end, just move on to next
#             pa = headB if pa is None else pa.next
#             pb = headA if pb is None else pb.next
#         return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
        
# ---------------------------------------------------------------------------------------------------

        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
    
# ---------------------------------------------------------------------------------------------------

# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/1092935/Python-Short-but-difficult-solution-explained

# The idea of solution is the following:

# Calculate lengths of both lists and evaluate difference.
# Make this number of steps for the longest list, pointer p1 and pointer p2 put to start of short list.
# Move pointers p1 and p2 one by one until we have the same value: it will be either common element or it will be None element.

# First list has a elements before intersection and b elements after intersection.
# Second list has c elements before intersection and b elements after intersection, and c > a.

# On the first step we will reach end of first list and for the second list we will be c-a elements before end.
# On the second step our short list ended, so now we start to traverse long list and after c-a steps one of the pointers will be in the beginning of short list and another will be c-a steps from the long list.
# Finally, we move both pointers with speed one and either we will have common element or they both reach the end in the same time and in this case they will have common None element.
# Complexity: we traverse both lists twice, so we will make no more than 2n + 2m = O(m+n). Space complexity is O(1).