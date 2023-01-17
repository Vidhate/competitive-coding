# https://www.interviewbit.com/problems/matrix-median/

class Solution:
	# @param A : list of list of integers
	# @return an integer

	def findMedian(self, A):
		B = []
		for row in A:
			B.extend(row)
		B = sorted(B)
		return B[len(B)//2]

s = Solution()
#A = [   [1, 3, 5],[2, 6, 9],[3, 6, 9]   ]
A = [[1,1,1,3,3]]
print(s.findMedian(A))