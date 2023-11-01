class Solution:
    def maxPower(self, s: str) -> int:
        record = 1
        ans = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                record +=1
            else:
                ans = max(ans, record)
                record = 1
        return max(ans, record) #最後要再更新一次，避免少算到連續到字串尾的字元
# https://leetcode.com/problems/consecutive-characters/
