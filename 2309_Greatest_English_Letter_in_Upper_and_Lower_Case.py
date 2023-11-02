class Solution:
    def greatestLetter(self, s: str) -> str:
        lower = sorted([char for char in s if char.islower()])[::-1]
        upper = sorted([char for char in s if char.isupper()])[::-1]
        if len(lower)==0 or len(upper)==0:
            return ''
        for char in upper:
            if chr(ord(char)+32) in lower:
                return char
        return ''
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
