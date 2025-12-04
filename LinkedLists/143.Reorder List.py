"""
Link: https://leetcode.com/problems/reorder-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #first step we should take is to find the mid point of the linked list by using a slow fast approach

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # print(slow, 'and', fast)

        #second step sperate the list from the mid point and reverse the second one. I called it the
        #severed list

        severed = slow.next
        prev = slow.next = None

        while severed:
            temp = severed.next
            severed.next = prev
            prev = severed
            severed = temp

        # print(prev)
        
        #third step is to weave the two lists together. 

        first, severed = head, prev

        while severed:
            temp1, temp2 = first.next, severed.next
            first.next = severed
            severed.next = temp1
            first, severed = temp1, temp2
        
