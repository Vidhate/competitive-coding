# https://www.interviewbit.com/problems/subset/

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def __init__(self):
		self.res = []

	def find_subset(self, A, subset, i):
		
		sub = subset.copy()
		self.res.append(sub)
		print(self.res, "index = ", i)
		for j in range(i,len(A)):
			sub.append(A[j])
			self.find_subset(A, sub, j+1)
			sub.pop(-1)
		return


	def subsets(self, A):
		A = sorted(A)
		self.find_subset(A, [], 0)
		return self.res

s = Solution()
print(s.subsets([1,2,3]))