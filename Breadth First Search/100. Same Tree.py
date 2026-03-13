# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False

        stack = [p, q]
        while stack:
            q_popped = stack.pop() #q node
            p_popped = stack.pop() #p node

            if p_popped.val != q_popped.val:
                return False
            
            #append the left or right node for comparasion
            if p_popped.left and not q_popped.left or q_popped.left and not p_popped.left:
                return False
            elif p_popped.left and q_popped.left:
                stack.append(p_popped.left)
                stack.append(q_popped.left)
            
            if p_popped.right and not q_popped.right or q_popped.right and not p_popped.right:
                return False
            elif p_popped.right and q_popped.right:
                stack.append(p_popped.right)
                stack.append(q_popped.right)
        
        return True
        
        #return true when stack is empty
