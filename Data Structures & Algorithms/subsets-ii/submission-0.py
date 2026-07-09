class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        nums = sorted(nums)
        length = len(nums)

        def ss(curr_list: list[int], idx: int, num_to_ignore: int | None):
            if idx >= length:
                return

            num = nums[idx]

            if num == num_to_ignore:
                ss(curr_list, idx + 1, num)
                return

            curr_list.append(num)
            result.append(curr_list.copy())

            ss(curr_list, idx+1, None)
            curr_list.pop()
            ss(curr_list, idx + 1, num)

        ss([], 0, None)
        return result