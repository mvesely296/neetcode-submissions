# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_depth_and_result(self, node: TreeNode | None, k: int) -> tuple[int | None, int | None]:
        if not node:
            return 0, None

        left_depth, l2 = self.get_depth_and_result(node.left, k)

        if l2 is not None:
            return left_depth, l2

        if left_depth == k:
            return left_depth, node.val

        right_depth, r2 = self.get_depth_and_result(node.right, k - left_depth-1)

        if r2 is not None:
            return right_depth, r2

        return left_depth+right_depth+1, None

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        return self.get_depth_and_result(root, k-1)[1]
