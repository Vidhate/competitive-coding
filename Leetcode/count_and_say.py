# https://leetcode.com/problems/count-and-say/submissions/

class Solution:
    def say(self, num):
        res = ''
        curdig, curcount = num[0], 1
        for digit in num[1:]:
            if digit==curdig:
                curcount+=1
            else:
                res+= str(curcount) + str(curdig)
                curdig = digit
                curcount = 1
                
        res+= str(curcount) + str(curdig)
        return res
                
    def countAndSay(self, n: int) -> str:
        cns = ['1','11']
        if n<=2:
            return cns[n-1]
        for i in range(2,n):
            cns.append(self.say(cns[-1]))
        return cns[-1]