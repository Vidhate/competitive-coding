# https://www.interviewbit.com/problems/3-sum/

class Solution:

	def search(self, A, target):

		if len(A)==1:
			return A[0]

		i, j = 0, len(A)-1
		mid = (i+j)//2
		while i<=j:

			mid = (i+j)//2

			if A[mid]==target:
				return A[mid]

			elif target>A[mid]:
				i=mid+1

			else:
				j=mid-1

		return A[mid]

	def solve(self, A, B):

		A = sorted(A)
		d = {x:i for i,x in enumerate(A)}
		mini_sum = sum(A[:3])
		mini = abs(mini_sum - B)

		for i,a in enumerate(A[:-2]):
			for j,b in enumerate(A[i+1:-1]):
				diff = B-(a+b)
				c = self.search(A[i+j+2:], diff)
				s = a+b+c
				#print(a, b, "find", A[i+j+2:], "found", c, "=", s)

				if abs(s-B)<mini:
					mini = abs(s-B)
					mini_sum = s
					#print(mini, "Minimum yet")

		return mini_sum

s = Solution()
#A = [int(x) for x in input().split()]
#B = int(input())

A = [ -1, 2, 1, -4 ]
B = 1

print(s.solve(A,B))
