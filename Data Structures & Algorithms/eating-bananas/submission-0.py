from math import ceil


class Solution:
    def can_eat(self, piles: list[int], speed: int, h: int):
        time_spent = 0
        for bananas in piles:
            time_spent += ceil(bananas / speed)

        return time_spent <= h


    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = int((l + r) / 2)
            if self.can_eat(piles, mid, h):
                r = mid
            else:
                l = mid + 1

        return r