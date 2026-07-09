from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.time_map: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)  # key: (time, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get_biggest_before(self, pairs: list[tuple[int, str]], ts: int) -> str:
        if pairs[0][0] > ts:
            return ""
        if pairs[-1][0] <= ts:
            return pairs[-1][1]

        l = 0
        r = len(pairs) - 1

        while r - l > 1:
            mid = (r + l) // 2
            if pairs[mid][0] == ts:
                return pairs[mid][1]
            elif pairs[mid][0] < ts:
                l = mid
            else:
                r = mid

        return pairs[l][1]


    def get(self, key: str, timestamp: int) -> str:
        list_of_keys = self.time_map[key]

        if not list_of_keys:
            return ""

        return self.get_biggest_before(list_of_keys, timestamp)