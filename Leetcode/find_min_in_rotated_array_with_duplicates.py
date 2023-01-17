# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# st-5:51PM en-5:55PM

class Solution:
	# O(N) solution with O(N) extra memory
	def findMin(self, nums):
		
		nums2 = []
		d = {}
		for num in nums:
			if d.get(num, None) is None:
				nums2.append(num)
				d[num]=1

		left, right = 0, len(nums2)-1
		mid = (left+right)//2
		last_mid = mid

		while left<=right:
			last_mid = mid
			mid = (left+right)//2

			if nums2[mid]>nums2[right]:
				left = mid+1
			elif nums2[mid]<nums2[left]:
				right = mid-1
			else:
				break

		return min([nums2[left], nums2[right], nums2[last_mid]])

	# O(N) solution with 0 extra memory
	def findMin2(self, nums):
		left, right = 0, len(nums)-1
		if right==0:
			return nums[0]
		while left<=right:
			mid = (left+right)//2
			prev, nxt = (mid-1+n)%n, (mid+1)%n  # like a cyclic boundary prev and nxt
			if nums[mid]<nums[nxt] and nums[mid]<nums[prev]:
				return nums[mid]
			if nums[mid]>nums[right]:
				left = mid+1
			elif nums[mid]==nums[right]:
				right-=1
			else:
				right = mid

s = Solution()
print(s.findMin([2,2,2,0,1]))