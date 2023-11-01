class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths)==1:
            return paths[0][1]
        
        city = {}
        for path in paths:
            for cty in path:
                try:
                    city[cty]+=1
                except KeyError:
                    city[cty]=1

        Once = [] #找出只去過一次
        for cty, times in city.items():
            if times==1:
                Once.append(cty)
        
        # 不用check path[0]，因為一定會有一個終點，
        # 所以path[0]一定不在Once內，path[0]在Once的情況在最上方被過濾掉了
        for path in paths:
            for cty in Once: 
                if path[1] == cty: 
                    return cty
# https://leetcode.com/problems/destination-city/
