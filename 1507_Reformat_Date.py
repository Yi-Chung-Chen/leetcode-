class Solution:
    def reformatDate(self, date: str) -> str:
        temp = date.split()
        ans = ''
        #year
        ans+=temp[2]
        ans+='-'
        #month
        if temp[1] == 'Jan':
            ans+='01'
        elif temp[1] == 'Feb':
            ans+='02'
        elif temp[1] == 'Mar':
            ans+='03'
        elif temp[1] == 'Apr':
            ans+='04'
        elif temp[1] == 'May':
            ans+='05'
        elif temp[1] == 'Jun':
            ans+='06'
        elif temp[1] == 'Jul':
            ans+='07'
        elif temp[1] == 'Aug':
            ans+='08'
        elif temp[1] == 'Sep':
            ans+='09'
        elif temp[1] == 'Oct':
            ans+='10'
        elif temp[1] == 'Nov':
            ans+='11'
        elif temp[1] == 'Dec':
            ans+='12'
        ans+='-'
        #day
        if len(temp[0])>3:
            ans+=temp[0][:2]
        else:
            ans+=('0'+temp[0][0])
        return ans
# https://leetcode.com/problems/reformat-date/
