# https://leetcode.com/problems/jump-game-ii/
# st-9:05; en-9:18

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [len(nums) for i in range(len(nums))]
        dp[0]=0
        for i in range(len(nums)):
            stride = nums[i]
            for j in range(i+1, min(i+stride+1, len(nums))):
                dp[j] = min(dp[j], dp[i]+1)
                
        return dp[-1]