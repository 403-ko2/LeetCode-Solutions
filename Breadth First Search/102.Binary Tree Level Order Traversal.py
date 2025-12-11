"""
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
