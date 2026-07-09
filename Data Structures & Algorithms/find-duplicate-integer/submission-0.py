class Solution:
    def resolve_index(self, nums: list[int], num: int, starting_num: int | None = None) -> int:
        if num == starting_num:
            return -1

        if not starting_num:
            starting_num = num

        if (new_num := nums[num - 1]) == -1:
            return num

        nums[num-1] = -1

        return self.resolve_index(nums, new_num, starting_num)

    def findDuplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            if num == -1:
                continue
            if (res := self.resolve_index(nums, num)) > -1:
                return res
