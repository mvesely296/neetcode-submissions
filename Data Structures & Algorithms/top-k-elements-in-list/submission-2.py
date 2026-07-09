from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_to_elem_map: defaultdict[int, list[int]] = defaultdict(list)
        elem_to_count_map: dict[int, int] = {}

        for elem in nums:
            curr_count = elem_to_count_map.get(elem, 0)
            if curr_count > 0:
                count_to_elem_map[curr_count].remove(elem)

            elem_to_count_map[elem] = curr_count + 1
            count_to_elem_map[curr_count + 1].append(elem)

        curr_count = max(count_to_elem_map.keys())

        result = []
        while len(result) < k:
            # simplification with extend() because task guarantees answer to be unique -> we don't have to worry about
            # overshooting k, otherwise we'd have to do this manually
            result.extend(count_to_elem_map[curr_count])
            curr_count -= 1

        return result
