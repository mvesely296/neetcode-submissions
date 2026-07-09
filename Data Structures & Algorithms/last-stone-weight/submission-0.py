import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            result = heapq.heappop_max(stones) - heapq.heappop_max(stones)
            if result:
                heapq.heappush_max(stones, result)
        
        return stones[0] if stones else 0