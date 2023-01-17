# https://leetcode.com/contest/biweekly-contest-77/problems/minimum-average-difference/

from typing import List
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0

        s = sum(nums)
        sum_left, count_left, sum_right, count_right = nums[0], 1, s-nums[0], len(nums)-1
        mini, mini_idx = s, 0
        for i in range(1,len(nums)):

            avg_left = sum_left//count_left
            avg_right = 0 if count_right==0 else sum_right//count_right
            diff = abs(avg_left-avg_right)

            if diff<mini:
                mini = diff
                mini_idx = i-1

            sum_left+=nums[i]
            count_left+=1
            sum_right-=nums[i]
            count_right-=1

        avg_left = sum_left//count_left
        avg_right = 0 if count_right==0 else sum_right//count_right
        diff = abs(avg_left-avg_right)
        if diff<mini:
            mini = diff
            mini_idx = len(nums)-1


        return mini_idx


s = Solution()
#print(s.minimumAverageDifference([2,5,3,9,5,3]))
#print(s.minimumAverageDifference([0]))
#print(s.minimumAverageDifference([5,4,3,2,1]))
print(s.minimumAverageDifference([4,2,0]))