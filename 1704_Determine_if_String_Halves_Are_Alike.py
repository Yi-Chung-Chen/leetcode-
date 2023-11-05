class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        s = [s[:len(s)//2], s[len(s)//2:]]
        vowel = {'a', 'e', 'i', 'o', 'u'}
        cnt1 = 0
        cnt2 = 0
        for char in s[0]:
            if char in vowel:
                cnt1+=1
        for char in s[1]:
            if char in vowel:
                cnt2+=1
        return cnt1 == cnt2
# https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/1092186582/
