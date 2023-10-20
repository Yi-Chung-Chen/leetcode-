class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = ''
        for i in range(len(s)):
            ans+=s[i][::-1]
            if i<len(s)-1:
                ans+=' '
        return ans
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
