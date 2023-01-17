# https://leetcode.com/problems/permutations/submissions/
from typing import List
class Solution:
    def allPermute(self, prev, nums):
        if len(nums)==0:
            self.solution.append(prev.copy())
            return
        
        nums2 = nums.copy()
        prev = prev.copy()
        for i, num in enumerate(nums):
            prev.append(num)
            nums2.remove(num)
            self.allPermute(prev, nums2)
            prev.pop()
            nums2.insert(i,num)
            
        return
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        self.solution = []
        self.allPermute([], nums)
        return self.solution
        

s = Solution()
print(s.permute([1,2,3]))