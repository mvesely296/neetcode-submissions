class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        result: list[list[int]] = []
        length = len(candidates)


        def cs(idx: int, curr_list: list[int], curr_sum: int, num_to_ignore: int | None):
            if idx >= length:
                return

            new_num = candidates[idx]

            if new_num == num_to_ignore:
                cs(idx + 1, curr_list, curr_sum, num_to_ignore)
                return

            if curr_sum + new_num > target:
                return

            curr_list.append(new_num)

            if curr_sum + new_num == target:
                result.append(curr_list.copy())
                curr_list.pop()
                return

            cs(idx+1, curr_list, curr_sum + new_num, None)

            curr_list.pop()

            cs(idx+1, curr_list, curr_sum, new_num)

        cs(0, [], 0, None)
        return result