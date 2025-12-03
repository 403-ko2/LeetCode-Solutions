# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while head and head.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

#this is the most efficient approach as it is linear with O(n) time and O(1) space

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        myset = set()
        newhead = head

        while newhead:
            myset.add(head)
            newhead = newhead.next
            if newhead in myset:
                return True
            myset.add(newhead)
        
        return False
#this solution is slightly less efficient although more intuitive as it has O(n) time but O(n) space aswell because of the dictionary/set
