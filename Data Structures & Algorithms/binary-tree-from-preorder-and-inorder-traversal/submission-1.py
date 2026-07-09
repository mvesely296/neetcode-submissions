class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not inorder:
            return None

        current_elem = preorder[0]

        inorder_idx = inorder.index(current_elem)

        left_inorder = inorder[:inorder_idx]
        right_inorder = inorder[inorder_idx+1:]

        root = TreeNode(current_elem, self.buildTree(preorder[1:inorder_idx+1], left_inorder), self.buildTree(preorder[inorder_idx+1:], right_inorder))

        return root