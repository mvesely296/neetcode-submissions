class Solution:

    def __init__(self):
        self.digit_to_letter_map: dict[str, list[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        result = []
        length = len(digits)

        def lc(curr_str: str, idx: int):
            if idx >= length:
                result.append(curr_str)
                return

            for char in self.digit_to_letter_map[digits[idx]]:
                lc(curr_str+char, idx+1)

        lc("", 0)
        return result