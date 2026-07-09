class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            mid = int((l + r) / 2)
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1
        return nums[l]