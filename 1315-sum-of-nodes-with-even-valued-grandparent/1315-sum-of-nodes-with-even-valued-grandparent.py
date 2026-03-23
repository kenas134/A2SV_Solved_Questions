class Solution:
    def sumEvenGrandparent(self, root):
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            
            total = 0
            
            # Check if grandparent exists and is even
            if grandparent is not None and grandparent % 2 == 0:
                total += node.val
            
            # Recurse left and right
            total += dfs(node.left, node.val, parent)
            total += dfs(node.right, node.val, parent)
            
            return total
        
        return dfs(root, None, None)