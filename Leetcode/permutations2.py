# https://leetcode.com/problems/permutations-ii/
from typing import List
class Solution:
    def allPermute(self, prev, nums):
        if len(nums)==0:
            self.solution.append(prev.copy())
            return
        
        done = {}
        nums2 = nums.copy()
        prev = prev.copy()
        for i, num in enumerate(nums):
            if done.get(num, None) is None:
                done[num]=1
                prev.append(num)
                nums2.remove(num)
                self.allPermute(prev, nums2)
                nums2.insert(i, num)
                prev.pop()
        return
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        self.solution=[]
        self.allPermute([], nums)
        return self.solution

s = Solution()
print(s.permuteUnique([1,1,2,3]))