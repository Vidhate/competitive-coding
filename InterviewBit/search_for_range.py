# https://www.interviewbit.com/problems/search-for-a-range/
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def binarySearch(self, A, B):
		l,r = 0, len(A)-1
		if len(A)==0:
			return -1

		while l<=r:
			mid=(l+r)//2
			if A[mid]==B:
				return mid
			elif A[mid]<B:
				l = mid+1
			else:
				r = mid-1

		return -1

	def searchRange(self, A, B):

		f = self.binarySearch(A, B)
		if f==-1:
			return [-1, -1]

		low, high = f, f
		res = [f, f]
		
		while low>=0:
			res[0] = low
			low = self.binarySearch(A[:low],B)
		
		while high<len(A) and high>=0:
			res[1] = high
			f = self.binarySearch(A[high+1:], B)
			if f<0:
				break
			high = high+1+f

		return res

A, B = [int(x) for x in input().split()], int(input())
s = Solution()
print(s.searchRange(A, B))

"""
1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
10
"""