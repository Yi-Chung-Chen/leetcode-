class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        freq = {}
        ans = -1
        for idx, char in enumerate(s): # O(n) 有線性解
            if char in freq: # O(1) hash是O(1)
                ans = max(ans, idx-freq[char]-1) #種樹問題 記得-1
            else:
                freq[char] = idx
        return ans
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
