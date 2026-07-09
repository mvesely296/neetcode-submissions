from collections import deque
from typing import Deque


def nice_print(grid: list[list[int]]):
    for row in grid:
        print(row)

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rotten_queue: Deque[tuple[int, int]] = deque()
        iters = 0

        dirs = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_queue.append((i, j))

        while rotten_queue:
            rotted_this_round = 0
            for _ in range(len(rotten_queue)):
                x, y = rotten_queue.popleft()
                for dx, dy in dirs:
                    if min(x+dx, y+dy) < 0 or x+dx == rows or y+dy == cols:
                        continue

                    if grid[x+dx][y+dy] == 1:
                        rotted_this_round = 1
                        grid[x + dx][y + dy] = 2
                        rotten_queue.append((x+dx, y+dy))
            iters += rotted_this_round

        for row in grid:
            for elem in row:
                if elem == 1:
                    return -1

        return iters
