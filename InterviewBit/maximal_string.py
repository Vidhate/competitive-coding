# https://www.interviewbit.com/problems/maximal-string/

# The approach is to find all combinations of swaps and return the max possible within the given operations limit
# What this code does is swaps every i for every following j and does this recursively while storing max possible
class Solution:
	# @param A : string
	# @param B : integer
	# @return a strings
	def __init__(self):
		self.maximal = ""

	def swap(self, s, ind1, ind2):
		s = list(s)
		x = s[ind1]
		s[ind1] = s[ind2]
		s[ind2] = x
		return ''.join(s)

	def findmax(self, A, B):
		if B==0:
			if A>self.maximal:
				self.maximal = A
			return

		s = A
		for i in range(len(A)):
			for j in range(i,len(A)):
				s = self.swap(A, i, j)
				self.findmax(s,B-1)
				s = self.swap(A, i, j)
		return

	def solve(self, A, B):
		self.maximal = A

		max_possible = ''.join(sorted(A)[::-1])
		if A==max_possible or len(A)<=B:
			return max_possible

		self.findmax(A, B)
		return self.maximal

s = Solution()
print(s.solve("7599", 2))