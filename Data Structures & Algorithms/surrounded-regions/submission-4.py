class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.dirs = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        )

    def _check_surrounded_from_point(self, i: int, j: int, seen: set[tuple[int, int]], board: list[list[str]]) -> bool:
        if min(i, j) < 0 or i >= self.rows or j >= self.cols:
            return False
        if board[i][j] == "X" or (i, j) in seen:
            return True

        seen.add((i, j))

        surrounded = True

        for dx, dy in self.dirs:
            if not self._check_surrounded_from_point(i + dx, j + dy, seen, board):
                surrounded = False

        return surrounded

    def solve(self, board: list[list[str]]) -> None:
        seen: set[tuple[int, int]] = set()

        self.rows = len(board)
        self.cols = len(board[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in seen or board[i][j] == "X":
                    continue

                current_seen = set()

                if self._check_surrounded_from_point(i, j, current_seen, board):
                    for surrounded_x, surrounded_y in current_seen:
                        board[surrounded_x][surrounded_y] = "X"
                else:
                    seen |= current_seen
