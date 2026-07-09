from dataclasses import dataclass


@dataclass
class PrefixNode:
    char_map: dict[str, PrefixNode]
    is_word: bool


class Solution:
    def __init__(self):
        self.result: set[str] = set()
        self.root: PrefixNode = PrefixNode(dict(), False)
        self.dirs: set[tuple[int, int]] = {(-1, 0), (1, 0), (0, -1), (0,1)}

    def add_word(self, word: str) -> None:
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

    def find_word_from_node(self, board: list[list[str]], current_string: str, visited_nodes: set[tuple[int, int]], idx_x: int, idx_y: int, node: PrefixNode):
        if (idx_x, idx_y) in visited_nodes:
            return

        if idx_x < 0 or idx_x >= len(board):
            return

        row = board[idx_x]

        if idx_y < 0 or idx_y >= len(row):
            return

        char = row[idx_y]
        new_node = node.char_map.get(char)

        if not new_node:
            return

        new_string = current_string + char

        if new_node.is_word:
            self.result.add(new_string)

        for x_offset, y_offset in self.dirs:
            self.find_word_from_node(board, new_string, visited_nodes | {(idx_x, idx_y)}, idx_x+x_offset, idx_y+y_offset, new_node)


    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        for word in words:
            self.add_word(word)

        for i, row in enumerate(board):
            for j in range(len(row)):
                self.find_word_from_node(board, "", set(), i, j, self.root)

        return list(self.result)
