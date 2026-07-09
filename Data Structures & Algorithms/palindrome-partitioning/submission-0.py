class Solution:
    def is_palindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


    def partition(self, s: str) -> list[list[str]]:
        result = []

        def part(curr_list: list[str], curr_word: str, idx: int):
            if idx >= len(s):
                return

            curr_word = curr_word + s[idx]
            if self.is_palindrome(curr_word):
                curr_list.append(curr_word)
                if idx + 1 >= len(s):
                    result.append(curr_list.copy())
                else:
                    part(curr_list, "", idx+1)
                curr_list.pop()

            part(curr_list, curr_word, idx+1)

            return

        part([], "", 0)

        return result