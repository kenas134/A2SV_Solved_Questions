# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        chk = {num:i for i,num in enumerate(nums)}
        def dfs(left,right):
            if left > right:
                return None
            maxx = max(nums[left:right+1])
            root = TreeNode(maxx)
            idx = chk[maxx]
            root.left = dfs(left,idx-1)
            root.right = dfs(idx+1,right)
            return root
        return dfs(0,len(nums)-1)