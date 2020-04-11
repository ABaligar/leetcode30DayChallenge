# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        slow = fast = head
        while(fast and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
