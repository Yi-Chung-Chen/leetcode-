class Solution:
    def minOperations(self, s: str) -> int:
        #只要考慮一種結果就好，答案的len(s)-cnt就是另一種字串的結果
        case = '01'*(len(s)//2)
        cnt = 0
        if len(s)%2:
            case+='0'
        for i in range(len(s)):
            if s[i]!=case[i]:
                cnt+=1
        return min(cnt, len(s)-cnt)
