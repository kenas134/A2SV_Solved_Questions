# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre:
            return None
        
        root = TreeNode(pre[0])
        
        if len(pre) == 1:
            return root
        
        # Next element in preorder is left subtree root
        left_root = pre[1]
        
        # Find left subtree size in postorder
        idx = post.index(left_root)
        size = idx + 1
        
        # Build subtrees
        root.left = self.constructFromPrePost(pre[1:1+size], post[:size])
        root.right = self.constructFromPrePost(pre[1+size:], post[size:-1])
        
        return root