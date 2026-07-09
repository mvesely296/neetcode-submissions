class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0

        dirs = (
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        )

        def traverse_island(i: int, j: int):
            if not 0 <= i < len(grid):
                return
            row = grid[i]
            if not 0 <= j < len(row):
                return
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for x, y in dirs:
                traverse_island(i+x, j+y)

        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if row[j] == "1":
                    islands += 1
                    traverse_island(i, j)

        return islands