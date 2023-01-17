# https://www.interviewbit.com/problems/divisible-by-60/

class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):
        
        if len(A)==0:
            return 0

        dig_sum = sum(A)
        if dig_sum==0:
            return 1

        if not dig_sum%3==0:
            return 0

        has_zero, has_even = 0, False
        for dig in A:
            if dig==0:
                has_zero += 1
            elif dig%2==0:
                has_even = True
        
        if not has_zero>0:
            return 0

        if not has_even and has_zero<2:
            return 0

        return 1

s = Solution()
A = [int(x) for x in input().split()]
print(s.divisibleBy60(A))