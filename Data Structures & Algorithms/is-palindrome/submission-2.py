class Solution:
    a = ord('a')
    z = ord('z')
    a_upper = ord('A')
    z_upper = ord('Z')
    zero = ord('0')
    nine = ord('9')

    def is_valid_character(self, c: str) -> bool:
        char = ord(c)
        return (
                (char >= self.a and char <= self.z) or
                (char >= self.a_upper and char <= self.z_upper) or
                (char >= self.zero and char <= self.nine)
        )


    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        i = 0
        j = length - 1
        while i < j:
            while i < j and not self.is_valid_character(s[i]):
                i += 1

            while i < j and not self.is_valid_character(s[j]):
                j -= 1

            if s[i].upper() != s[j].upper():
                return False

            i += 1
            j -= 1

        return True
