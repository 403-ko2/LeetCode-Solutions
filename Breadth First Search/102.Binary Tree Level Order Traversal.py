"""
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        res = []
        quene = deque([root])

        while quene:
            qSize = len(quene)
            currLev = []
            for _ in range(qSize):
                node = quene.popleft()
                currLev.append(node.val)
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            res.append(currLev)

        return res
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
