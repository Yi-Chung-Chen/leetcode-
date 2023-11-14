class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = {'type':0,
                'color':1,
                'name':2,
        }
        cnt = 0
        for item in items:
            if item[rule[ruleKey]] == ruleValue:
                cnt+=1
        return cnt
# https://leetcode.com/problems/count-items-matching-a-rule/description/
