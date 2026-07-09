from typing import Callable

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return False

        # node, min, max
        stack: list[tuple[TreeNode, int, int]] = [(root, 1001, -1001)]

        while stack:
            node, lower_than, higher_than = stack.pop()
            if not node:
                continue

            if node.val >= lower_than or node.val <= higher_than:
                return False

            stack.append((node.left, min(lower_than, node.val), higher_than))
            stack.append((node.right, lower_than, max(higher_than, node.val)))

        return True
