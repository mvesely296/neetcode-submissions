class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        length = len(nums)
        for i in range(length):
            targetIndex = found.get(target - nums[i])
            if targetIndex is not None:
                return [targetIndex, i]
            found[nums[i]] = i