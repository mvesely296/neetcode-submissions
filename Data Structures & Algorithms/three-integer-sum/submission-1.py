class Solution:
    def two_sum(self, numbers: list[int], target: int, start: int) -> list[tuple[int, int]]:
        l = start
        r = len(numbers) - 1
        result = []

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                result.append((numbers[l], numbers[r]))
                l += 1
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        return result


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: set[tuple[int, int, int]] = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            num1 = nums[i]
            answers = self.two_sum(nums, -num1, i+1)
            if answers:
                for answer in answers:
                    triplets.add((num1, answer[0], answer[1]))

        return [list(x) for x in triplets]