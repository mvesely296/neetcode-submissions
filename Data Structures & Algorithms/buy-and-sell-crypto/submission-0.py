class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_max = 0
        current_min = float("inf")

        for price in prices:
            current_max = max(current_max, price - current_min)
            current_min = min(current_min, price)

        return current_max