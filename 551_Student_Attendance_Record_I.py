class Solution:
    def checkRecord(self, s: str) -> bool:
        return len(s.split('LLL')) == 1 and s.count('A')<2 # s.split('LLL')的長度如果超過1表示有LLL被分割出來那就直接掰囉
#https://leetcode.com/problems/student-attendance-record-i/
