class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for i in range(len(logs)):
            if logs[i][0] != '.':
                cnt+=1
            elif logs[i] == '../':
                if cnt>0:
                    cnt-=1
        return cnt
# https://leetcode.com/problems/crawler-log-folder/description/
