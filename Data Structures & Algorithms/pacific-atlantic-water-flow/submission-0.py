from collections import deque
from typing import Deque


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0

    def _process_tiles(self, heights: list[list[int]], starting_tiles: list[tuple[int, int]]) -> set[tuple[int, int]]:
        seen = set()
        tile_queue: Deque[tuple[int, int]] = deque()

        dirs = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        )

        def add_tile(i: int, j: int, old_height: int):
            if min(i, j) < 0 or i >= self.rows or j >= self.cols or (i, j) in seen:
                return

            if old_height <= heights[i][j]:
                tile_queue.append((i, j))
                seen.add((i, j))

        for tile in starting_tiles:
            add_tile(tile[0], tile[1], heights[tile[0]][tile[1]])

        while tile_queue:
            for _ in range(len(tile_queue)):
                x, y = tile_queue.popleft()
                for dx, dy in dirs:
                    add_tile(x+dx, y+dy, heights[x][y])

        return seen

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])

        pacific_edges = [(0, x) for x in range(self.cols)] + [(x, 0) for x in range(self.rows)]
        pacific_tiles = self._process_tiles(heights, pacific_edges)

        atlantic_edges = [(self.rows-1, x) for x in range(self.cols)] + [(x, self.cols-1) for x in range(self.rows)]
        atlantic_tiles = self._process_tiles(heights, atlantic_edges)

        return [list(x) for x in atlantic_tiles & pacific_tiles]
