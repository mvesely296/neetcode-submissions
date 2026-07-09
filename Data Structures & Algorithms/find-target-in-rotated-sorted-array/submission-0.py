class Solution:
    def find_min_index(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            mid = int((l + r) / 2)
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1
        return l

    def search(self, nums: list[int], target: int) -> int:
        min_index = self.find_min_index(nums)
        if nums[-1] >= target:
            l = min_index
            r = len(nums) - 1
        else:
            l = 0
            r = min_index - 1

        while l <= r:
            mid = int((l+r) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
