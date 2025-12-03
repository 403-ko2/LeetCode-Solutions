"""
My initial thought was to use a dictionary or set to keep track of nodes we have already visited and check to see if the "head.next" is in the set, if it is then return true
You can use a slow and fast pointer method as utilized in the very first solution. The iterates the slow pointer one at a time and the fast pointer 2 at a time. If the Linked list is cyclic
then the pointers will eventually meet on the same node and we check this. If slow pointer and fast pointer equal eachother (if they are on the same node) then we return True.

there is a way to make the slow and fast pointers even more efficient by using pythons imports like lambda but I never do that and honestly it feels like its only a leetcode competative hack lol


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

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
