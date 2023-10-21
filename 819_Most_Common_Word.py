class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w\s]',' ', paragraph.lower()).split() # 先把輸入轉為小寫，接著用正則化把非空格字元的內容清除掉，最後再移除空格
        paragraph = [word for word in paragraph if word not in banned] # 把被禁用的詞彙從paragraph刪除

        freq = {} # 建立字元頻率表
        for part in paragraph:
            try:
                freq[part] += 1
            except KeyError:
                freq[part] = 1

        ans = max(freq, key = lambda word:freq[word]) # 用lambda函數去返還有最大value的word
        return ans
#https://leetcode.com/problems/most-common-word/
