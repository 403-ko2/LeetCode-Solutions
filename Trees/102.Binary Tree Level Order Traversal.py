"""
quene 
output array
while loop 
    |_ nested for loop

if there is no root node we return an empty []
create our queue with the root node
create a result arr to house our final output 

1. while queue
    1a. var for queue length
    1b. var for queue level arr
    2. for loop range of qLength:
        2a. var for node, popleft
        2b. update queue level to include node.val
    
            3. if node right != none
                3a. append node to queue
            4. if node left != none
                4a. append node to queue
        
    5. append qLevel to result arr

6. return result
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])

        while queue:
            q_size = len(queue)
            curr_lvl = []
            for _ in range(q_size):
                node = queue.popleft()
                curr_lvl.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            res.append(curr_lvl)
            
        return res
