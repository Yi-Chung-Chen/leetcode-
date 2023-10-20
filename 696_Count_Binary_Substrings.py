class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 建立三個變數 當前多長、之前多長、計數器
        cur = 1
        pre = 0
        cnt = 0
        for i in range(1, len(s)):
            if s[i-1] == s[i]: # 開始去算最大長度
                cur+=1
            else: # 執行這塊，表示說出現 1與0的轉折，先更新pre的值，然後開始去算新的轉折值最大長度，當下一次遇到轉折的時候，就更新cnt、pre、cur
                cnt += min(cur, pre)
                pre = cur
                cur = 1
        return cnt + min(cur, pre)
      # 這題很玄 想法極度抽象XD
#https://leetcode.com/problems/count-binary-substrings/
