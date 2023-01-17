# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List
class Solution:
    def binarySearchInterval(self, nums, target):
        #print("finding", target, "in", nums)

        if len(nums)==0:
            return [-1,-1]
        
        left, right = 0, len(nums)-1
        mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                #print("mid", mid)
                start, _ = self.binarySearchInterval(nums[left:mid], target)
                start = mid if start==-1 else left+start
                _, end = self.binarySearchInterval(nums[mid+1:right+1], target)
                end = max(mid, mid+1+end)
                #print("start", start, "end", end)
                return [start, end]
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
                
        return [-1, -1]
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binarySearchInterval(nums, target)
        
        
s = Solution()
print(s.searchRange([5,7,7,8,8,8,10], 8))