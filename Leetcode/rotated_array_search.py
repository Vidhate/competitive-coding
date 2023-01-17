# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
	def binsrch(self, a, n):
		l, r = 0, len(a)-1
		while l<=r:
			m = (l+r)//2
			if a[m]==n:
				return m

			if a[l]<=a[m]:
				if a[l]<=n and a[m]>n:
					r = m-1
				else:
					l = m+1
			else:
				if n>a[m] and n<=a[r]:
					l = m+1
				else:
					r = m-1

		return -1

	def search(self, nums, target):
		return self.binsrch(nums, target)

s = Solution()
print(s.search([4,5,6,7,0,1,2],1))