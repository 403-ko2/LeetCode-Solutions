#this is a  DFS solution using an iterative approach rather than recursive. BFS wouldnt work here because the leafs closer 
#to the top would get collected thus putting the array our of order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_all_leafs(root, array):
            if not root:
                return
            stack = [root]
            while stack:
                current = stack.pop()
                if not current.left and not current.right:
                    array.append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

        if not root1 or not root2:
            return False

        ones_leafs, twos_leafs = [], []

        get_all_leafs(root1, ones_leafs)
        get_all_leafs(root2, twos_leafs)

        return ones_leafs == twos_leafs
