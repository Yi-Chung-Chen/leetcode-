class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)): 
                if strs[j-1][i]>strs[j][i]: # 去check 第一行有沒有照順序，不要做轉置矩陣這種多此一舉的方法，直接幹他就對了，反正最後還是要check，不如省下做轉置的運算
                    cnt+=1
                    break
        return cnt
# https://leetcode.com/problemset/all/?topicSlugs=string&page=2&sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkRJRkZJQ1VMVFkifV0%3D
