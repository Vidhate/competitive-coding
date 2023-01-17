# https://www.interviewbit.com/problems/longest-consecutive-sequence/
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
		d = {a:1 for a in A}
		maxlen=0

		for a in A:
			c = 0
			if d.get(a-1,None) is None:
				x = a
				while not d.get(x,None) is None:
					x+=1
					c+=1
			maxlen = max(maxlen, c)
				
		return maxlen

s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))