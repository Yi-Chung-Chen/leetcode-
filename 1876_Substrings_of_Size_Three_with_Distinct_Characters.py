class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        s = [s[i:i+3] for i in range(len(s))]
        cnt = 0
        print(s)
        for substr in s:
            if len(set(substr)) == 3:
                cnt+=1
        return cnt
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
