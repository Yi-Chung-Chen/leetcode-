class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = [s[i:i+2*k] for i in range(0, len(s), 2*k)] # 前k個要做顛倒，每2K長度的字串循環一次，因此將s做適當切割
        ans = ''
        for part in temp:
            ans += part[:k][::-1]+part[k:] # 前k個顛倒，其餘不變
        return ans
# https://leetcode.com/problems/reverse-string-ii/description/
