class Solution:
    def sumEvenGrandparent(self, root):
        def dfs(node, parent, grandparent):
            if not node:
                return 0

            if grandparent and grandparent.val % 2 == 0:
                return node.val + dfs(node.right,node,parent) + dfs(node.left,node,parent)
            return dfs(node.right,node,parent) + dfs(node.left,node,parent)

        return dfs(root,None,None)