class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = [char for char in s]
        ptr1 = 0
        ptr2 = len(s)-1
        while ptr1<ptr2: # 用 two pointer的方式去做
            if s[ptr1].isalpha() and s[ptr2].isalpha():
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1+=1
                ptr2-=1
            elif s[ptr1].isalpha():
                ptr2-=1
            else:
                ptr1+=1
        return ''.join(s)
# https://leetcode.com/problems/reverse-only-letters/
