class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        digit = []
        ans = ''

        for i in range(len(s)):
            if s[i].isalpha():
                alpha.append(s[i])
            elif s[i].isdigit():
                digit.append(s[i])
 
        if len(alpha)-len(digit) == 0: # 一樣長
            for i in range(len(digit)):
                ans+=alpha[i]+digit[i]

        elif len(alpha)-len(digit) == 1: # alpha比較長
            for i in range(len(digit)):
                ans+=alpha[i]+digit[i]
            ans+=alpha[-1]

        elif len(digit)-len(alpha) == 1: # digit比較長
            for i in range(len(alpha)):
                ans+=digit[i]+alpha[i]
            ans+=digit[-1]
            
        return ans
# https://leetcode.com/problems/reformat-the-string/
