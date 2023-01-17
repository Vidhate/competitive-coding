# https://www.interviewbit.com/problems/atoi/

class Solution:
	# @param A : string
	# @return an integer
	def atoi(self, A):

		valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		
		i = 0
		while i<len(A) and A[i]==' ':
			i+=1

		num = ""
		sign = 1
		if A[i]=='-':
			sign = -1
			i+=1
		elif A[i]=='+':
			i+=1

		while i<len(A) and A[i]!=' ':
			if A[i].isalpha():
				break

			elif not A[i] in valid:
				return 0
				
			num+=A[i]
			i+=1

		if len(num)==0:
			return 0

		j = 0
		int_num = 0
		INT_MAX, INT_MIN = (2**31) - 1, -1*(2**31)
		while j<len(num):
			int_num = int_num*10 + int(num[j])
			#print(int_num)
			if sign*int_num>=INT_MAX:
				return INT_MAX
			if sign*int_num<=INT_MIN:
				return INT_MIN
			j+=1

		return sign*int_num

s = Solution()
print(s.atoi(input()))