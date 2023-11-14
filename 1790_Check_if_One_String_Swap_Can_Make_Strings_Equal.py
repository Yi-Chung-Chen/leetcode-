class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        for i, j in zip(s1, s2): # 善用zip
            if i!=j:
                cnt+=1
        return sorted(s1) == sorted(s2) and cnt<=2 
  # https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
