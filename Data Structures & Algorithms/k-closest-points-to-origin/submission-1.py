import heapq
import math
from dataclasses import dataclass, field


@dataclass(order=True)
class Point:
    x: int = field(compare=False)
    y: int = field(compare=False)
    priority: float = 0

    def __post_init__(self):
        self.priority = math.sqrt(self.x**2 + self.y**2)


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points_heap = []
        heapq.heapify_max(points_heap)

        for point in points:
            point = Point(x=point[0], y=point[1])
            if len(points_heap) >= k:
                if point < points_heap[0]:
                    heapq.heapreplace_max(points_heap, point)
            else:
                heapq.heappush_max(points_heap, point)

        return [[point.x, point.y] for point in points_heap]