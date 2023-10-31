class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        temp = ans[0]
        # 這題一定要線性解，不然會TLE
        for i in range(1, len(pref)):
            coef = temp
            if i<2:
                coef = ans[i-1]
            ans.append(coef^pref[i])
            temp ^= ans[i]
        return ans

# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/?envType=daily-question&envId=2023-10-31
