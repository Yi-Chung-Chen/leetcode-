class Solution:
    def reformatNumber(self, number: str) -> str:
        number = ''.join([digit for digit in number if digit.isdigit()])
        temp = ''.join([number[i:i+3]+'-' for i in range(0, len(number), 3)])
        temp = temp[:-1]
        if len(number)%3 == 1:
            temp = temp[:-3]+'-'+temp[-3]+temp[-1]
        return temp
# https://leetcode.com/problems/reformat-phone-number/submissions/1092181922/
