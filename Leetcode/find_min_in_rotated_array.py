# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# st-5:22PM; en-5:45PM; O(logN)

class Solution:
	def findMin(self, nums):

		left, right = 0, len(nums)-1
		mid, last_mid = (left+right)//2, (left+right)//2
		while left<=right: 
			last_mid = mid
			mid = (left+right)//2

			print(left, mid, right, last_mid)
			print(nums[left], nums[mid], nums[right], nums[last_mid],"\n")
			
			if nums[mid]>nums[right]:
				left=mid+1
			elif nums[mid]<nums[left]:

				right=mid-1
			else:
				break
			
		a = [nums[left], nums[right], nums[last_mid]]
		print(a)
		return min(a)



s = Solution()
print(s.findMin([3,4,5,6,1,2]))