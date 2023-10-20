class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction={'R' : 0,
                    'L' : 0,
                    'U' : 0,  
                    'D' : 0,
        }
        for move in moves:
            direction[move]+=1
        return direction['R'] == direction['L'] and direction['U'] == direction['D']
#https://leetcode.com/problems/robot-return-to-origin/description/
