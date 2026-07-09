class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = ord("a")

        sList = [0] * (ord("z") - a + 1)

        for char in s:
            sList[ord(char) - a] += 1
        
        for char in t:
            key = ord(char) - a
            sList[key] -= 1
            if (sList[key]) < 0:
                return False
        
        return True