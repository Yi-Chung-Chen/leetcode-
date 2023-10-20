class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if set(s) == set(goal) and len(s) == len(goal): # 測資過濾
            mem = goal # 用mem去存取goal最初的資料
            goal = goal[1:]+goal[0] # 按照題目的作法 left shift
            if mem == s: # 先檢查mem是否恰好就是s
                return True
            while goal!=mem: # 如果不是就用left shift的方式改變字串，停止條件為goal長得跟原本一樣
                if goal == s:
                    return True
                goal = goal[1:]+goal[0]
        return False
# https://leetcode.com/problems/rotate-string/
