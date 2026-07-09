class Solution:

    breaker_char = "#"

    def parse_start_and_length(self, word: str, index: int) -> tuple(int, int):
        length = ""
        while word[index] != self.breaker_char:
            length += word[index]
            index += 1

        return index+1, int(length)

    def encode(self, strs: list[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + self.breaker_char + word

        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            word_start, word_length = self.parse_start_and_length(s, i)
            result.append(s[word_start:word_start + word_length])
            i = word_start + word_length
        return result