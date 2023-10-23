class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = (s1+' '+s2).split()
        cnt = Counter(s1) # 會建立頻率表
        ans = []
        for key, value in cnt.items():
            if value == 1: # 找出只出現過一次的key
                ans.append(key)
        return ans
# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
