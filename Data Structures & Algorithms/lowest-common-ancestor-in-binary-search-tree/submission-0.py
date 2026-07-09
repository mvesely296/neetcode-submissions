class Solution:
    def lca_extended(self, root: TreeNode | None, p: TreeNode, q:TreeNode) -> tuple[bool, bool, TreeNode | None]:
        if not root:
            return False, False, None
        
        l1, l2, l3 = self.lca_extended(root.left, p, q)
        r1, r2, r3 = self.lca_extended(root.right, p, q)
        
        contains_p = l1 or r1 or root.val == p.val
        contains_q = l2 or r2 or root.val == q.val
        lca = l3 or r3
        if not lca and contains_q and contains_p:
            lca = root
        
        return contains_p, contains_q, lca
            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.lca_extended(root, p, q)[2]
