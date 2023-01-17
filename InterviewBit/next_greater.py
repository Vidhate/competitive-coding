# https://www.interviewbit.com/problems/nextgreater/
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def nextGreater(self, A):

		res, s = [], []
		res.insert(0,-1)
		s.append(A[-1])
		A = A[:-1]

		for a in A[::-1]:
			if a<s[-1]:
				res.insert(0,s[-1])
			else:
				while s and a>=s[-1]:
					s.pop()

				if s:
					res.insert(0, s[-1])
				else:
					res.insert(0, -1)
				
			s.append(a)
			print("stack", s)
			print("res", res)

		return res

s = Solution()
inp = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
print(inp)
print(s.nextGreater(inp))