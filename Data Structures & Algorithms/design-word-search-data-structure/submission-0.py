from dataclasses import dataclass


@dataclass
class PrefixNode:
    char_map: dict[str, PrefixNode]
    is_word: bool

class WordDictionary:

    def __init__(self):
        self.root = self.root = PrefixNode(dict(), False)

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.char_map:
                node = node.char_map[char]

            else:
                new_node = PrefixNode(dict(), False)
                node.char_map[char] = new_node
                node = new_node

        node.is_word = True

        return

    def search(self, word: str, idx: int = 0, node: PrefixNode | None = None) -> bool:
        node = node or self.root

        for i in range(idx, len(word)):
            char = word[i]
            if char == ".":
                return any(self.search(word, i+1, nd) for nd in node.char_map.values())

            node = node.char_map.get(char)
            if not node:
                return False

        return node.is_word