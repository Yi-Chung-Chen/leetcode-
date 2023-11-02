class Solution:
    def dayOfYear(self, date: str) -> int:
        def special_year(year):
            if year%1000 == 0:
                return True
            elif year%400 == 0:
                return True
            elif year%4==0 and year%100!=0:
                return True
            return False
        month_day = {
            '1':31,
            '2':28,
            '3':31,
            '4':30,
            '5':31,
            '6':30,
            '7':31,
            '8':31,
            '9':30,
            '10':31,
            '11':30,
            '12':31,
        }
        date = list(date.split('-'))
        day = 0
        for i in range(1, int(date[1])+1):
            day+=month_day[str(i)]
        if special_year(int(date[0])) and int(date[1])>1 : #潤
            day+=1
            month_day['2'] = 29
    
        day-=(month_day[str(int(date[1]))]-int(date[2]))
        return day
# https://leetcode.com/problems/day-of-the-year/
