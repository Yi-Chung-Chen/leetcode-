class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)): # 一定要做切割，所以從1開始
            ans = max(ans, s[:i].count('0')+s[i:].count('1'))
        return ans
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/
