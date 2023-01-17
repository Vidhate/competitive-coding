# https://leetcode.com/problems/decode-ways/
# st = 4:07; en = 

import typing
class Solution:
    # solution with backtracking and finding all possible combinations
    def findSubsets(self, current_set, code, level=0) -> int:
        
        current_set = current_set.copy()
        #print(current_set, code, self.solution, level)
        if not code:
            self.solution+=1
            return
        
        for i in range(len(code)+1):
            left, right = code[:i], code[i:]
            if left=="" or left[0]=='0' or int(left)>26:
                continue
            current_set.append(left)
            self.findSubsets(current_set, right, level+1)
            current_set.pop()
            
        return
    """
    def numDecodings(self, s: str) -> int:
        self.solution = 0
        self.findSubsets([], s)
        return self.solution
    """
    # solution with dp
    def numDecodings(self, s: str) -> int:
        cPrev, nPrev, n = None, 1, 1
        for c in s:
            nNext = 0
            if c != '0':
                nNext += n
            if cPrev == '1' or cPrev == '2' and c < '7':
                nNext += nPrev
            cPrev, nPrev, n = c, n, nNext
        return n

s = Solution()
print(s.numDecodings("11106"))