class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        dirs = (
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        )

        def traverse_island(i: int, j: int, current_area: int = 0) -> int:
            if not 0 <= i < len(grid):
                return 0
            row = grid[i]
            if not 0 <= j < len(row):
                return 0
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            current_area += 1

            for x, y in dirs:
                current_area += traverse_island(i+x, j+y)

            return current_area

        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if row[j] == 1:
                    max_area = max(traverse_island(i, j), max_area)

        return max_area
