class Solution:
    alphabet_chars = (ord("z") - ord("a") + 1)
    alphabet_start = ord("a")

    def __get_hash_representation(self, word: str) -> tuple[int]:
        repr = [0] * self.alphabet_chars
        for char in word:
            repr[ord(char) - self.alphabet_start] += 1

        return tuple(repr)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map: dict[tuple[int], list[str]] = {}

        for word in strs:
            key = self.__get_hash_representation(word)
            words = anagram_map.get(key, list())
            words.append(word)
            anagram_map[key] = words

        return list(anagram_map.values())
