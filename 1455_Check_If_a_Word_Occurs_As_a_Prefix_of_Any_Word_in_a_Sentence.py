class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            if sentence[i][:len(searchWord)] == searchWord[:len(searchWord)]:
                return i+1
        return -1
# 沒啥好講的就是檢查，不過要從頭開始查，不可以只是因為searchWord在sentence內就return i+1
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
