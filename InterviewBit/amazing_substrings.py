# https://www.interviewbit.com/problems/amazing-subarrays/

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):

		mod = 10003
		vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
		l = len(A)
		total = 0
		for i,char in enumerate(A):
			if char in vowels:
				total += (l-i)
				total = total%mod
		return total

s = Solution()
print(s.solve(input()))