class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for elem in nums:
            if elem in elems:
                return True
            elems.add(elem)
        return False