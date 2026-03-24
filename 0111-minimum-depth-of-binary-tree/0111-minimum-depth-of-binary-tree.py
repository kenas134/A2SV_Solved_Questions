# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def rec(cur,x):
            if not cur.right and not cur.left:
                return x
            if cur.left and cur.right:
                return min(rec(cur.left,x+1),rec(cur.right,x+1))
            elif cur.left:
                return rec(cur.left,x+1)
            else:
                return rec(cur.right,x+1)
        return rec(root,1)