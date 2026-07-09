class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        indices = {inorder[i]: i for i in range(len(inorder))}

        self.pre_idx = 0

        def dfs(l: int, r: int) -> TreeNode | None:
            if l >= r:
                return None

            curr_val = preorder[self.pre_idx]
            self.pre_idx += 1

            idx = indices[curr_val]

            node = TreeNode(
                curr_val,
                dfs(l, idx),
                dfs(idx+1, r)
            )

            return node



        return dfs(0, len(preorder))