# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums_map = {}
        for i, num in enumerate(nums):
            if nums_map.get(num, None) is None:
                nums_map[num] = 1
            else:
                nums_map[num]+=1

        count = 0
        for num in nums:
            if num==k-num:
                if nums_map.get(num, 0)>1 and nums_map.get(k-num, 0)>1:
                    nums_map[num]-=1
                    nums_map[k-num]-=1
                    count+=1
            else:
                if nums_map.get(num, 0)>0 and nums_map.get(k-num, 0)>0:
                    nums_map[num]-=1
                    nums_map[k-num]-=1
                    count+=1

        return count

s = Solution()
print(s.maxOperations([1,2,3,4,5],5))