class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixel = 0 # 用來算當前的pixel
        line = 0 # 用來算有多少line
        for i in range(len(s)):
            if pixel+widths[ord(s[i])-ord('a')]>100:
                pixel = widths[ord(s[i])-ord('a')]
                line+=1
            else:
                pixel+=widths[ord(s[i])-ord('a')]
        return [line+1, pixel] # 特別注意要把line做+1因為最後面那個也要算喔
# https://leetcode.com/problems/number-of-lines-to-write-string/
