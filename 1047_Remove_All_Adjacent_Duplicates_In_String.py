class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 用stack去做，如果下一次出現的在stack內，就把在stack內的彈出，否則新增
        temp = [s[0]] 
        for i in range(1, len(s)):
            if len(temp)>0 and temp[-1]==s[i]:
                temp.pop()
            else:
                temp.append(s[i])
        return ''.join(temp)a
