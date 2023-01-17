# https://leetcode.com/problems/subsets-ii/submissions/

from typing import List
class Solution:
    
    def subset(self, current_set, nums, level=0):
        
        #print(current_set, self.solution, level, nums)
        current_set = current_set.copy()
        self.solution.add(tuple(sorted(current_set)))
        #self.solution.append(current_set)

        if not nums:
            #print("Returning empty")
            return

        for i, num in enumerate(nums):
            current_set.append(num)
            self.subset(current_set, nums[i+1:], level+1)
            current_set.pop()
        return
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.solution = set()
        self.subset([], nums)
        return list(self.solution)

s = Solution()
print(s.subsetsWithDup([4,4,4,1,4]))