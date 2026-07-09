class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        num_of_nums = len(nums)
        nums = sorted(nums)

        def c_sum(curr_nums: list[int], idx: int, current_sum: int):

            if idx >= num_of_nums:
                return
            num = nums[idx]

            current_sum = sum(curr_nums)

            if current_sum + num > target:
                return

            curr_nums.append(num)
            if current_sum + num == target:
                result.append(curr_nums.copy())
                curr_nums.pop()
                return

            c_sum(curr_nums, idx, current_sum + num)

            curr_nums.pop()

            c_sum(curr_nums, idx + 1, current_sum)

        c_sum([], 0, 0)

        return result
