# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        target = root.val
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur.val != target:
                return False
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return True


        