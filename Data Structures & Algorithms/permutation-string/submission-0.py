from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map: defaultdict[str, int] = defaultdict(lambda: 0)
        for char in s1:
            char_map[char] += 1

        substring_length = len(s1)
        deviation = substring_length

        for i in range(len(s2)):
            char = s2[i]
            if char_map[char] > 0:
                deviation -= 1
            else:
                deviation += 1

            char_map[char] -= 1

            starting_index = i - substring_length

            if starting_index >= 0:
                old_char = s2[starting_index]
                if char_map[old_char] < 0:
                    deviation -= 1
                else:
                    deviation += 1

                char_map[old_char] += 1

            if deviation == 0:
                return True

        return False
