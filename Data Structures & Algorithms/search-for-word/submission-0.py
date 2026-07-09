class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        visited: set[tuple[int, int]] = set()

        dirs = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        def find(i: int, j: int, char_idx: int) -> bool:
            if char_idx >= len(word):
                return True

            if (i, j) in visited:
                return False

            if not 0 <= i < len(board):
                return False

            row = board[i]

            if not 0 <= j < len(row):
                return False

            if row[j] != word[char_idx]:
                return False

            visited.add((i, j))

            if any(find(i+ip, j+jp, char_idx+1) for ip, jp in dirs):
                return True

            visited.remove((i, j))

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if find(i, j, 0):
                    return True

        return False
