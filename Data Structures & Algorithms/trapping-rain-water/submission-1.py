class Solution:
    def trap(self, height: list[int]) -> int:
        # self.print_heights(height)
        curr_height = 0
        trapped_total = 0
        trapped_current = 0
        counted = set()

        for i in range(len(height)):
            elem = height[i]
            if elem >= curr_height:
                curr_height = elem
                trapped_total += trapped_current
                trapped_current = 0
                if elem == curr_height:
                    counted.add(i)

            else:
                trapped_current += curr_height - elem

        trapped_current = 0
        curr_height = 0
        curr_index = len(height) - 1
        for i in range(len(height) - 1, -1, -1):
            elem = height[i]
            if elem == curr_height and i in counted:
                trapped_current = 0
            elif elem >= curr_height:
                curr_height = elem
                curr_index = i
                trapped_total += trapped_current
                trapped_current = 0
            else:
                trapped_current += curr_height - elem

        return trapped_total