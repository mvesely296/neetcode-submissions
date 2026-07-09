class Solution:
    def __init__(self):
        self.result: list[list[int]] = [[]]

    def subsets(self, nums: list[int]) -> list[list[int]]:
        for num in nums:
            self.result = self.result + [x + [num] for x in self.result]

        res = self.result
        for i in range(len(self.result)-1):
            for j in range(i+1, len(self.result)-1):
                if self.result[i] == self.result[j]:
                    res.remove(self.result[i])

        return self.result
