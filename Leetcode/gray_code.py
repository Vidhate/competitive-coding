# https://leetcode.com/problems/gray-code/
# st-9:37; en-10:03; Not solved - help from GFG

class Solution:
	def grayCode(self, n: int) -> List[int]:
		res = [0,1]
        tracker = 1
        for i in range(1,n):
            tracker*=2
            zeros, ones = res, res[::-1]
            ones = [tracker+x for x in ones]
            res = zeros+ones
            
        return res
        
