class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        times = 1
        while times*word in sequence:
            times+=1 #注意是要找連續的，而非斷斷續續的 斷斷續續的則用 FOREACH i = 0, ... , len(seq)-len(w) seq[i:i+len(word)] == w: cnt+=1
        return times-1 
# https://leetcode.com/problems/maximum-repeating-substring/description/
