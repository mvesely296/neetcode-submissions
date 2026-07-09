class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        last_occurrence_map = {}

        max_length = 0
        current_streak_start = -1

        for i in range(len(s)):
            char = s[i]
            last_occurrence = last_occurrence_map.get(char, -1)
            if last_occurrence >= current_streak_start:
                max_length = max(max_length, i - current_streak_start)
                current_streak_start = last_occurrence + 1
                last_occurrence_map[char] = i
            else:
                last_occurrence_map[char] = i

        max_length = max(max_length, len(s) - current_streak_start)

        return max_length