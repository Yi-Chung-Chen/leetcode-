class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        ptr1 = 0
        ptr2 = len(s)
        # 用 two pointer去做
        for i in range(len(s)):
            if s[i] == 'I':
                ans.append(ptr1)
                ptr1+=1
            elif s[i] == 'D':
                ans.append(ptr2)
                ptr2-=1
        # 要記得把最後一個值塞進去
        if s[-1] == 'I':
            ans.append(ptr2)
        else:
            ans.append(ptr1)

        return ans
# https://leetcode.com/problems/di-string-match/
