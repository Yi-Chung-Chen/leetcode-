class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        for i in range(len(command)-1):
            if command[i]+command[i+1] == '()':
                ans+='o'
            elif command[i].isalpha():
                ans+=command[i]
        if command[-1].isalpha():
            ans+=command[-1] # 要判斷最後一個是不是字母，因為你迴圈指判斷到倒數第二個
        return ans
# https://leetcode.com/problems/goal-parser-interpretation/submissions/1092170961/
