class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans = set(sentence)
        return len(ans) == 26
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
