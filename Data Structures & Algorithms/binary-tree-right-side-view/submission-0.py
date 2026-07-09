# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result: list[list[int]] = []
        current_list: list[int] = []
        current_level = 0
        queue_to_execute: Queue[tuple[TreeNode, int]] = Queue()
        queue_to_execute.put((root, current_level))

        while not queue_to_execute.empty():
            node, level = queue_to_execute.get_nowait()
            if level > current_level:
                current_level = level
                result.append(current_list)
                current_list = []

            if not node:
                continue

            current_list.append(node.val)
            queue_to_execute.put((node.left, current_level + 1))
            queue_to_execute.put((node.right, current_level + 1))
        
        result = [x[-1] for x in result]
        
        return result