# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Map value -> index for inorder
        in_map = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_index = 0
        
        def build(left, right):
            if left > right:
                return None
            
            # Pick root from preorder
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            
            root = TreeNode(root_val)
            
            # Split using inorder index
            mid = in_map[root_val]
            
            # Build left subtree
            root.left = build(left, mid - 1)
            
            # Build right subtree
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)