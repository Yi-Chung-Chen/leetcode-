class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        temp = " ".join(words) #轉成字串
        return [word for word in words if temp.count(word)>1] # 算字串內重複出現次數大於1的字串

# https://leetcode.com/problems/string-matching-in-an-array/
