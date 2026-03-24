# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        prefix = {0: 1}
        
        def dfs(node, currSum):
            if not node:
                return 0
            
            currSum += node.val
            
            # check how many paths end here
            count = prefix.get(currSum - targetSum, 0)
            
            # add current sum to map
            prefix[currSum] = prefix.get(currSum, 0) + 1
            
            # explore children
            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)
            
            # backtrack
            prefix[currSum] -= 1
            
            return count
        
        return dfs(root, 0)