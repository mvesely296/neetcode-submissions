class Solution:
    def binary_search(self, matrix: list[int], target: int):
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = int((l + r) / 2)
            current = matrix[mid]

            if current == target:
                return True
            elif current < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        if matrix[l][0] > target:
            return False

        while r - l > 1:
            mid = int((r + l) / 2)
            first_in_row = matrix[mid][0]

            if first_in_row == target:
                return True

            if first_in_row < target:
                l = mid
            else:
                r = mid

        if matrix[r][0] <= target:
            return self.binary_search(matrix[r], target)

        else:
            return self.binary_search(matrix[l], target)
