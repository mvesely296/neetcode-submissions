MIN_SENTINEL = float("-inf")
MAX_SENTINEL = float("inf")

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n == 0:
            if m % 2:
                return nums2[m // 2]
            else:
                return (nums2[m // 2] + nums2[m // 2 - 1]) / 2

        if m == 0:
            if n % 2:
                return nums1[n // 2]
            else:
                return (nums1[n // 2] + nums1[n // 2 - 1]) / 2

        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        target = (n + m + 1) // 2

        # i + j = target - 1
        l = 0
        r = n

        # works only if nums1 is bigger or equal to nums2 and also odd number of elements
        while True:
            i = (l + r) // 2
            j = target - i

            left1 = nums1[i-1] if i else MIN_SENTINEL
            left2 = nums2[j - 1] if j else MIN_SENTINEL
            right1 = nums1[i] if i < n else MAX_SENTINEL
            right2 = nums2[j] if j < m else MAX_SENTINEL

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                r = i-1

            else:
                l = i+1
