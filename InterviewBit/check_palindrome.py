# https://www.interviewbit.com/problems/check-palindrome/

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        d = {}
        for a in A:
            if d.get(a,None):
                d[a]+=1
            else:
                d[a]=1
        
        odd = 0
        for k,v in d.items():
            if not v%2==0:
                odd+=1
        
        if odd>1:
            return 0
        return 1