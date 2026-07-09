class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        stack: list[tuple[TreeNode, int]] = [(root, root.val)]
        
        while stack:
            node, rolling_max = stack.pop()
            if not node:
                continue
                
            if rolling_max <= node.val:
                good_nodes += 1
            
            stack.append((node.left, max(node.val, rolling_max)))
            stack.append((node.right, max(node.val, rolling_max)))
        
        return good_nodes
