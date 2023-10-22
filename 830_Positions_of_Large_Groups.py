class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        record = []
        brake = 0 
        for i in range(1, len(s)):
            if s[i-1] != s[i]: # 如果發生連續中斷的情況
                if i-brake>=3: # 因題述長度大於3判定large，故新增if邏輯
                    record.append([brake, i-1]) 
                brake = i # 用一個 brake 記錄下一個新的字元出現的位置
        if len(s)-brake>=3: # 這是用來處理末段的問題，例如: 'aaabbb' 這種情況，避免bbb沒有滿足第6行的邏輯而因此消失的窘境
            record.append([brake, len(s)-1])
        return record 
# https://leetcode.com/problems/positions-of-large-groups/
