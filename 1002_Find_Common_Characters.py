class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = [{} for _ in range(len(words))] # 根據words大小創建頻率表

        for i in range(len(words)): #建構頻率表
            for char in words[i]:
                try:
                    temp[i][char]+=1
                except KeyError:
                    temp[i][char]=1
        
        intersection = set(temp[0].keys()) 

        for dic in [temp[i] for i in range(1, len(temp))]:# 把每個頻率表的共同出現key抓出來
            intersection &= set(dic.keys())
        
        intersection_value = {key: [dic[key] for dic in [temp[i] for i in range(len(temp))]] for key in intersection} # 把對應到的key值重新建構一張表 key to list [value]
        
        ans = []
        for key, value in intersection_value.items(): #最後根據最低的出現次數去把key新增到ans內
            for _ in range(min(value)):
                ans.append(key)
        
        return ans
# https://leetcode.com/problems/find-common-characters/
