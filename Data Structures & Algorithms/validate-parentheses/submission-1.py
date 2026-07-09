class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close_map: dict[str, str] = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in open_to_close_map.keys():
                stack.append(char)
            else:
                try:
                    if open_to_close_map[stack.pop()] != char:
                        return False
                except IndexError:
                    return False

        return len(stack) == 0