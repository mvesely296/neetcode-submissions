class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sList = [0] * (ord("z") + 1)
        tList = [0] * (ord("z") + 1)

        for char in s:
            sList[ord(char)] += 1
        
        for char in t:
            tList[ord(char)] += 1
        
        return sList == tList