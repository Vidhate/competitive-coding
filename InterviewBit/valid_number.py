# https://www.interviewbit.com/problems/valid-number/

class Solution:
	# @param A : string
	# @return an integer
	def validNumber(self, A):
		


	def isNumber(self, A):
		A = A.strip()
		i = 0
		if A[i]=='-':
			i+=1

		valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		while i<len(A):
			if not A[i] in valid:
				break

		if i==len(A):
			return 1

		dot, exp = 0, 0
		if A[i]=='e':
			exp=1
			i+=1

		if A[i]=='.':
			dot=1
			i+=1