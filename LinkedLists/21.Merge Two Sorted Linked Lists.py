"""
problem: get two singly linked lists(sorted) and combine them into
one sorted singly linked list.

Example: [1,2,4] [1,3,5] -> [1,1,2,3,4,5] 

Data structure: Linked List

Algorithm: Since were editing a linked list we want to use pointers to move the 
data around in the linked list.

- create a dummy node to prevent us from repeating logic. the dummy node will just be an empty node to give us a starting point 
- create a tail variable equal to dummy. this is what we will use to build our linked list. it will end up at the end making it our tail
- a while loop while both linked lists are non empty
- if statements inside comparing each value to determine which node should be placed next
- if one linked list runs out of nodes have if checks outside of the loop to finish placing the rest of the nodes in 
- finally we return dummy.next which is out actual head node

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
