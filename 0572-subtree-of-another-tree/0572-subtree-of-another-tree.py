# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        
        # Helper: check if two trees are identical
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            return isSame(a.left, b.left) and isSame(a.right, b.right)
        
        # Main logic
        if not root:
            return False
        
        # Check at current node
        if isSame(root, subRoot):
            return True
        
        # Otherwise check left and right
        return self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)