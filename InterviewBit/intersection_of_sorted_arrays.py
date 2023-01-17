# https://www.interviewbit.com/problems/intersection-of-sorted-arrays/

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):

		i, j = 0, 0
		intersection = []
		while i<len(A) and j<len(B):
			if A[i]==B[j]:
				intersection.append(A[i])
				i+=1
				j+=1
			elif A[i]<B[j]:
				i+=1
			else:
				j+=1

		return intersection

s = Solution()

A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 5]

print(s.intersect(A,B))