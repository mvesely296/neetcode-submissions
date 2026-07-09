class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result_fwd = [1]

        length = len(nums)

        for i in range(1, length):
            result_fwd.append(result_fwd[i-1] * nums[i-1])

        current_product = 1
        result = [0] * length
        result[length-1] = result_fwd[length - 1]
        for i in range(1, length):
            current_product *= nums[length - i]
            result[length - i - 1] = current_product * result_fwd[length - i - 1]

        return result
