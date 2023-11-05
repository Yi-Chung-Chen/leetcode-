class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        temp = [set(word) for word in words]
        cnt = len(temp)
        for word in temp:
            for char in word:
                if char not in allowed:                  
                    cnt-=1
                    break
        return cnt
# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
