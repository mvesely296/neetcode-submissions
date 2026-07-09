class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        elem_to_count_map: dict[int, int] = {}
        n = len(nums)
        max_freq = 0

        for elem in nums:
            curr_count = elem_to_count_map.get(elem, 0) + 1
            elem_to_count_map[elem] = curr_count
            max_freq = max(max_freq, curr_count)

        buckets = [[] for _ in range(n + 1)]

        for key, v in elem_to_count_map.items():
            buckets[v].append(key)

        result = []
        curr_count = max_freq

        while len(result) < k:
            # simplification with extend() because task guarantees answer to be unique -> we don't have to worry about
            # overshooting k, otherwise we'd have to do this manually
            result.extend(buckets[curr_count])
            curr_count -= 1

        return result
