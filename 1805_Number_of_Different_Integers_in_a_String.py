class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen = set()
        temp = ''
        for char in word:
            if char.isdigit():
                temp+=char
            else:
                if temp!='':
                    seen.add(int(temp))
                temp=''
        if temp!='':
            seen.add(int(temp))
        return len(seen)
# https://leetcode.com/problems/number-of-different-integers-in-a-string/description/
