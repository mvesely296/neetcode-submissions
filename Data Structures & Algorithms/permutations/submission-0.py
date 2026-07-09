class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def pm(curr_list: list[int], remaining_list: list[int]):

            if len(remaining_list) == 1:
                curr_list.append(remaining_list[0])
                result.append(curr_list.copy())
                curr_list.pop()
                return

            for i in range(len(remaining_list)):
                curr_list.append(remaining_list[i])
                pm(curr_list, remaining_list[:i] + remaining_list[i+1:])
                curr_list.pop()

        pm([], nums)
        return result
