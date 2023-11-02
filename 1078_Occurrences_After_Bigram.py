class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        temp = text.split()
        ans = []
        for i in range(len(temp)-2): # 判斷到倒數第三個就好，因為就算倒數兩個滿足條件，後面也沒有字串了
            if temp[i] == first:
                if temp[i+1] == second:
                    ans.append(temp[i+2]) 
        return ans
# https://leetcode.com/problems/occurrences-after-bigram/
