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
        def dfs(root,dis):
            if root and not root.left and not root.right:
                return dis
            elif root and not root.left:
                return dfs(root.right,dis+1)
            elif root and not root.right:
                return dfs(root.left,dis+1)
            else:
                return min(dfs(root.left,dis+1),dfs(root.right,dis+1))
        return dfs(root,0)+1

