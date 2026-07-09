from collections import defaultdict
from queue import Queue


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map: dict[str, Queue[bool]] = {}
        for char in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            char_map[char] = Queue()

        replacements_map: defaultdict[str, int] = defaultdict(lambda: 0)
        max_length = 0

        for char in s:
            for key, v in char_map.items():
                if char == key:
                    v.put(True)
                    max_length = max(max_length, v.qsize())
                else:
                    if replacements_map[key] >= k:
                        while not v.empty() and v.get():
                            pass
                        replacements_map[key] -= 1

                    if k > 0:
                        replacements_map[key] += 1
                        v.put(False)

                    max_length = max(max_length, v.qsize())

        return max_length