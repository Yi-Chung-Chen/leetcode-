class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = ''
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sentence = sentence.split()
        idx = 1
        for word in sentence:
            if word[0] in vowel:
                word +='ma'
            else:
                word = word[1:]+word[0]+'ma'
            word+=idx*'a'
            idx+=1
            ans+=word
            if idx<=len(sentence):
                ans+=' '
        return ans
#https://leetcode.com/problems/goat-latin/
