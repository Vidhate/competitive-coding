#https://www.interviewbit.com/problems/woodcutting-made-easy/

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer

	# Brute force solution O(n * b)
	def solve1(self, A, B):
		
		i = max(A) - 1
		while i>=0:
			wood = 0
			for val in A:
				wood += (val-i if val>i else 0)
			if wood>=B:
				return i
			i-=1


	def binarySearch(self, A, num):

		l,r = 0, len(A)-1
		while l<=r:
			mid=(l+r)//2
			if A[mid]==num:
				return mid
			elif A[mid]<num:
				l+=1
			else:
				r-=1

		return mid

	# O(n * logn)
	def solve(self, A, B):

		#total_wood = sum(A)
		A = sorted(A)
		i = len(A)-1
		ht = A[i]
		wood = 0
		trees = 0

		while wood<B and i>=0:
			i-=1
			trees+=1
			wood+=(trees*(ht-A[i]))
			ht = A[i]

		return ht+((wood-B)//trees)

A, B = [int(x) for x in input().split()], int(input())
s = Solution()
print(s.solve(A, B))