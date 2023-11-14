class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c1, n1):
            return chr(ord(c1)+int(n1))
        s = [s[i:i+2] for i in range(0, len(s), 2)]
        ans = ''
        for i in range(len(s)):
            try:
                ans+=(s[i][0]+shift(s[i][0], s[i][1]))
            except IndexError:
                ans+=s[i]
        return ans 
# https://leetcode.com/problems/replace-all-digits-with-characters/description/
