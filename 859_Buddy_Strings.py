class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s): # s:'aa'  goal:'aa'
            return True
        compare = [(char1, char2) for char1, char2 in zip(s, goal) if char1!=char2] # zip的功能就是講兩個list對應到的index綁在一起
        return len(compare) == 2 and compare[0] == compare[1][::-1] #因為只能SWAP一次代表說不同處只能有一個，由於zip會把不同點match在一起，因此list的長度一定要為 2 同時第一個元素要等於第二個元素的顛倒
      
# https://leetcode.com/problems/buddy-strings/
