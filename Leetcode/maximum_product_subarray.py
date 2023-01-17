# https://leetcode.com/problems/maximum-product-subarray/
# st : 4:21PM; en : 5:10PM; O(N)

class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		
		if len(nums)==1:
            return nums[0]
        
        last_min, last_max = 1, 1
        max_product = nums[0]
        for i, num in enumerate(nums):
            maxi, mini = max([last_min*num, num, last_max*num]), min([last_min*num, num, last_max*num])
            last_max, last_min = maxi, mini
            max_product = last_max if last_max>max_product else max_product
                
        return max_product