class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack: list[tuple[int, int]] = [(heights[0], 0)]  # (height, index)
        max_area = 0
        num_of_bars = len(heights)

        for i in range(1, num_of_bars):
            bar = heights[i]
            oldest_index = i
            while stack and stack[-1][0] >= bar:
                height, oldest_index = stack.pop()
                max_area = max(max_area, height * (i - oldest_index))
            stack.append((bar, oldest_index))

        while stack:
            height, oldest_index = stack.pop()
            max_area = max(max_area, height * (num_of_bars - oldest_index))

        return max_area
