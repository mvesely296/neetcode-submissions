class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        borders: dict[int, tuple[int, int]] = {}
        current_max = 0

        for num in nums:
            left_end = borders.get(num-1, (num, num))[0]
            right_end = borders.get(num+1, (num, num))[1]

            borders[right_end] = borders[left_end] = borders[num] = (left_end, right_end)
            current_max = max(right_end - left_end + 1, current_max)

        return current_max