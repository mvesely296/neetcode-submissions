class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def gp(curr_string: str, open_curr: int, open_remaining: int):
            if open_curr == 0 and open_remaining == 0:
                result.append(curr_string)
                return

            if open_curr > 0:
                gp(curr_string + ")", open_curr-1, open_remaining)

            if open_remaining > 0:
                gp(curr_string + "(", open_curr+1, open_remaining-1)

        gp("", 0, n)
        return result