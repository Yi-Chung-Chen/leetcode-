class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 先把字串的文字分割出來
        jewels = [jewel for jewel in jewels]
        stones = [stone for stone in stones]
        cnt = 0 # counter
        for stone in stones:
            if stone in jewels: # check 石頭是不是寶石
                cnt+=1
        return cnt
#https://leetcode.com/problems/jewels-and-stones/description/
