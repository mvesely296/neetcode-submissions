class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.size: int = k
        self.nums: list[int] = []

        for num in nums:
            self.add(num)

        return self.nums[0]

    def rebalance(self, idx: int):
        length = len(self.nums)
        while True:
            parent = int((idx-1)/2)
            child_a = 2*idx + 1
            child_b = 2*idx + 2

            if parent >= 0 and self.nums[parent] > self.nums[idx]:
                self.nums[parent], self.nums[idx] = self.nums[idx], self.nums[parent]
                idx = parent
                continue

            if child_b >= length or self.nums[child_a] < self.nums[child_b]:
                child = child_a
            else:
                child = child_b

            if child < length and self.nums[idx] > self.nums[child]:
                self.nums[child], self.nums[idx] = self.nums[idx], self.nums[child]
                idx = child
                continue

            break


    def add(self, val: int) -> int:
        if len(self.nums) >= self.size and self.nums[0] > val:
            pass

        elif len(self.nums) >= self.size:
            self.nums[0] = val
            self.rebalance(0)

        else:
            self.nums.append(val)
            self.rebalance(len(self.nums)-1)

        return self.nums[0]
