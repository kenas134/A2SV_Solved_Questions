# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        self.maxx = 0

        def dfs(root):
            if not root:
                return True,float("inf"),float("-inf"),0
            
            is_left,l_minn,l_maxx,l_summ=dfs(root.left)
            is_right,r_minn,r_maxx,r_summ=dfs(root.right)

            if is_left and is_right and l_maxx < root.val < r_minn:
                cur = r_summ+l_summ + root.val
                self.maxx = max(self.maxx,cur)
                return [True,min(root.val,l_minn),max(root.val,r_maxx),cur]
            return [False,0,0,0]
        dfs(root)
        return self.maxx