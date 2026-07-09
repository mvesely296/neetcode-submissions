class Solution:
    def two_sum(self, numbers: list[int], target: int, start: int) -> list[tuple[int, int]]:
        l = start
        r = len(numbers) - 1
        result = []

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                result.append((numbers[l], numbers[r]))

                left_val = numbers[l]
                right_val = numbers[r]

                while l < r and numbers[l] == left_val:
                    l += 1

                while l < r and numbers[r] == right_val:
                    r -= 1

            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        return result


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: list[list[int]] = list()
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            num1 = nums[i]
            for answer in self.two_sum(nums, -num1, i+1):
                triplets.append([num1, answer[0], answer[1]])

        return [list(x) for x in triplets]
