class Solution:
    board_size = 9

    def get_grid(self, i: int, j: int):
        return int(i / 3) * 3 + int(j / 3)

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(self.board_size)]
        cols = [set() for _ in range(self.board_size)]
        grids = [set() for _ in range(self.board_size)]

        for i in range(self.board_size):
            for j in range(self.board_size):
                num = board[i][j]
                if num == ".":
                    continue
                grid_no = self.get_grid(i, j)
                if (num in (rows[i])) or (num in (cols[j])) or ((num in (grids[grid_no]))):
                    return False
                rows[i].add(num)
                cols[j].add(num)
                grids[grid_no].add(num)

        return True
