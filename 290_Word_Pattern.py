class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(list(set(pattern))) != len(list(set(s))): # 先用一個filter 過濾掉不符合的測資
            return False
        def encoder(data): 
            freq = {} # 創建一個頻率表
            cnt = 0
            for i in range(len(data)):
                try:
                    freq[data[i]]+=0 # 跟往常的作法稍有不同，這次不用記次數，而是給出現的字一個編碼
                except KeyError: # 如果遇到的字元不在，頻率表內，那就新增他
                    freq[data[i]] = cnt
                    cnt+=1
            
            check = [] # 這是用來存取從字元轉換成編碼的暫存器
            for i in range(len(data)):
                check.append(freq[data[i]])
            
            return check

        return encoder(pattern) == encoder(s)
# https://leetcode.com/problems/word-pattern/
