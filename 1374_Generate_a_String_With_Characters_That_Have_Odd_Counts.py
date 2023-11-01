class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ''
        if n%2:
            ans+='a'*n
        else:
            ans+='a'*(n-1)
            ans+='b'
        return ans
      # 奇偶問題
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
