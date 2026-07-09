class Solution:

    breaker_char = "€"

    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        return self.breaker_char.join(strs) + self.breaker_char

    def decode(self, s: str) -> list[str]:
        x = s.split(self.breaker_char)
        return x[:len(x)-1]
