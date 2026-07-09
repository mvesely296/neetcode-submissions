class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        dirs = (
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        )

        def update_path(x: int, y: int):
            for dx, dy in dirs:
                if not 0 <= x+dx < len(grid):
                    continue

                if not 0 <= y+dy < len(grid[x+dx]):
                    continue

                if grid[x][y] + 1 < grid[x+dx][y+dy]:
                    grid[x + dx][y + dy] = grid[x][y] + 1
                    update_path(x+dx, y+dy)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    update_path(i, j)