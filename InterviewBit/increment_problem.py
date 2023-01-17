# https://www.interviewbit.com/problems/an-increment-problem/discussion/p/problem-explanation-for-an-increment-problem/77071/1941
from pprint import pprint
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def solve(self, A):

		d, res = {}, []
		for i,a in enumerate(A):
			if not d.get(a, None) is None:
				res[d[a]]+=1
				if d.get(a+1, None) is None:
					d[a+1] = d[a]
				elif d[a]<d[a+1]:
					d[a+1] = d[a]

			d[a] = i
			res.append(a)
		return res

s = Solution()
print(s.solve( [1,2,3,2,3,1,4,2,1,3]))