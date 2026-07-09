class Solution:
    def get_height_and_balance(self, root: Optional[TreeNode]) -> tuple[int, bool]:
        if not root:
            return 0, True
        
        h1, b1 = self.get_height_and_balance(root.left)
        h2, b2 = self.get_height_and_balance(root.right)
        
        return max(h1, h2) + 1, b1 and b2 and (abs(h1 - h2) <= 1) 
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height_and_balance(root)[1]
