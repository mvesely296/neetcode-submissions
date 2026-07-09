from dataclasses import dataclass


@dataclass
class PrefixNode:
    char_map: dict[str, PrefixNode]
    is_word: bool


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode(dict(), False)

    def insert(self, word: str) -> None:
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


    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            node = node.char_map.get(char)
            if not node:
                return False

        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            node = node.char_map.get(char)
            if not node:
                return False

        return True