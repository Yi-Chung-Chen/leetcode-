class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        temp = text.split()
        space = 0
        for char in text:
            if char == ' ':
                space+=1

        if len(temp)==1:
            return temp[0]+' '*space

        eqlSpace = int(space/(len(temp)-1))
        ans = ''  
        for i in range(len(temp)):
            ans+=temp[i]
            if i!=len(temp)-1:
                ans+=eqlSpace*' '

        ans+=(space-eqlSpace*(len(temp)-1))*' '

        return ans
# https://leetcode.com/problems/rearrange-spaces-between-words/
