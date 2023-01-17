# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
	def removeDuplicates(self, nums):
		cur, cnt, dups, l = nums[0], 1, 0, len(nums)
		for i in range(1,len(nums)):
			if nums[i]==cur:
				cnt+=1
			else:
				cur = nums[i]
				cnt=1

			if cnt>2:
				nums[i]='_'
				dups+=1

		print(nums, dups)

		for d in range(dups):
			nums.remove('_')

		return l-dups


s = Solution()
nums = [0,0,1,1,1,1,2,3,3]
k = s.removeDuplicates(nums)
print(nums[:k+1])