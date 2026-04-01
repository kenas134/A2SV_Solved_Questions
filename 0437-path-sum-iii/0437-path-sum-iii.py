# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        
        target = {0:1}
        def dfs(root,summ):
            if not root:
                return 0
            summ += root.val
            need = summ-targetSum

            cur =  target.get(need,0)


            target[summ] = target.get(summ,0) + 1

            right = dfs(root.right,summ)
            left = dfs(root.left,summ)    
            target[summ] -= 1        

            return cur + left + right
            
        return dfs(root,0)


            
        