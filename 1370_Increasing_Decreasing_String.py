class Solution:
    def sortString(self, s: str) -> str:
        freq = Counter(sorted(s))
        ans = ''
        cnt = 0

        while len(ans)<len(s):
            temp = ''
            print(freq)
            for key, value in freq.items():
                if value:
                    temp+=key
                    freq[key]-=1
            if cnt%2:
                temp = temp[::-1]
            ans+=temp
            cnt+=1

        return ans

      #先建頻率表，然後由小->大、大->小，這個順序去增長字串
# https://leetcode.com/problems/increasing-decreasing-string/
