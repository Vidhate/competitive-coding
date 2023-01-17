# https://www.interviewbit.com/problems/minimum-parantheses/

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
		stack_count, unmatched_count = 0, 0
		valid = 0
		for p in A:
			if p=='(':
				stack_count+=1
			if p==')':
				if stack_count<=0:
					unmatched_count+=1
				else:
					stack_count-=1
		return unmatched_count+stack_count

s = Solution()
print(s.solve(input()))