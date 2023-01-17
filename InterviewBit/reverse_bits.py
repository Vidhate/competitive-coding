# https://www.interviewbit.com/problems/reverse-bits/

import numpy as np
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        a = A
        num = 0
        power = 31
        while a>0:
            bit = a%2
            num+=(bit*(2**power))
            #print('{:032b}'.format(num))
            power-=1
            a = a//2

        #print('{:032b}'.format(A))
        #return '{:032b}'.format(num)
        return num

s = Solution()
print(s.reverse(int(input())))