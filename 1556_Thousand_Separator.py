class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        cnt = 0
        ans = ''
        for digit in n:
            if cnt%3==0 and cnt: #每過千位就加dot
                ans+='.'
            ans+=digit
            cnt+=1
        return ans[::-1]


# https://leetcode.com/problems/thousand-separator/description/
