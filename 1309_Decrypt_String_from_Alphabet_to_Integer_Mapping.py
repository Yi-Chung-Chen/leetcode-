class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {'0':'0'} # 避免0發生keyError
        for i in range(26):  # 建對應表
            try:
                mapping[chr(i+97)] = mapping[chr(i+97)]
            except KeyError:
                if i<9:
                    mapping[str(i+1)] = chr(i+97)
                else:
                    mapping[str(i+1)+'#'] = chr(i+97)

        ans = []
        for i in range(len(s)):
            if s[i]!='#':
                ans.append(mapping[s[i]]) # 直接幹他，不要考慮太多
            else:
                ans.pop()
                ans.pop()
                ans.append(mapping[s[i-2:i+1]]) # 如果發現到'#'就把前面兩個彈出，導入正確的對應
        return ''.join(ans)
      
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
