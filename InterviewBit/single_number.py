# https://www.interviewbit.com/problems/single-number/

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):

		B = {}
		for v in A:
			if B.get(v,"no")=="no":
				B[v] = 1
			else:
				B.pop(v)

		return B.keys()[0]