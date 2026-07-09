class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not inorder:
            return None

        i = 0
        current_elem = None

        while current_elem not in inorder:
            current_elem = preorder[i]
            i += 1
        inorder_idx = inorder.index(current_elem)

        left_inorder = inorder[:inorder_idx]
        right_inorder = inorder[inorder_idx+1:]

        root = TreeNode(current_elem, self.buildTree(preorder[i:], left_inorder), self.buildTree(preorder[i:], right_inorder))

        return root