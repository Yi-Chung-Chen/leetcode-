class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 這題考的就是stack而已
        def func(string):
            stack = []
            for char in string:
                if char == '#':
                    try:
                        stack.pop()
                    except IndexError:
                        pass
                else:
                    stack.append(char) 
            return stack
        return func(s) == func(t)
#https://leetcode.com/problems/backspace-string-compare/
