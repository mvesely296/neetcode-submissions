class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l = 0
        r = len(heights) - 1
        current_max = 0

        while l < r:
            current_max = max(current_max, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return current_max
