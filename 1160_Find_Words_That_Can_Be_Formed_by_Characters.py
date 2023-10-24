class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = 0
        for i in range(len(words)):
            temp = [char for char in chars]
            cnt+=len(words[i]) # 先把所有字串的長度加起來
            for char in words[i]:
                try:
                    temp.remove(char)
                except ValueError:
                    cnt-=len(words[i]) # 如果該字串不能被chars內的字元構成，那就扣掉該字串的長度
                    break
        return cnt
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
        
