class Solution:
    def get_depth_and_diameter(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return 0, 0

        left = self.get_depth_and_diameter(root.left)
        right = self.get_depth_and_diameter(root.right)

        depth = max(left[0], right[0]) + 1
        diameter = max(left[1], right[1], left[0] + right[0])

        return depth, diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.get_depth_and_diameter(root)[1]
