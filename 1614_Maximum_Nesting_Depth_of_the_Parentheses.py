class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        cnt = 0
        # 請善用資料結構，凡正我就去看stack裡面塞了多少括號，然後慢慢紀錄，最後回傳最大的
        for char in s:
            if char == '(':
                stack.append(char)
                cnt = max(cnt, len(stack))
            elif char == ')':
                stack.pop()
        
        return cnt
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
