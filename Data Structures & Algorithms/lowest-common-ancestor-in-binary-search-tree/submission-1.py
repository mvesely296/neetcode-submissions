class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if ((root.val > p.val) != (root.val > q.val)) or (root.val == p.val) or (root.val == q.val):
            return root

        if root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return self.lowestCommonAncestor(root.right, p, q)
