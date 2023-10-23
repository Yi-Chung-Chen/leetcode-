class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # . before @ ignore 
        # + before @ delete char from the range of + to @

        # first filter '.'
        for i in range(len(emails)):
            at = emails[i].index('@')
            emails[i] = ''.join([char for char in emails[i][:at] if char!='.'])+emails[i][at:]
        
        #second filter '+'
        for i in range(len(emails)):
            if '+' in emails[i]:
                at = emails[i].index('@')
                plus = emails[i].index('+')
                emails[i] = emails[i][:plus]+emails[i][at:]
        return len(set(emails))
# https://leetcode.com/problems/unique-email-addresses/
# 這題比較快的方法是把email分成 local 跟 domain去做 用split去做切割
