# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        check = set()

        def dfs(root):
            if not root:
                return False
            need = k - root.val
            if need in check:
                return True
            check.add(root.val)
            if dfs(root.left):
                return True
            if dfs(root.right):
                return True
            return False
        return dfs(root)
    