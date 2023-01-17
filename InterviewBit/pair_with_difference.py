# https://www.interviewbit.com/problems/pair-with-given-difference/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        A = sorted(A)
        B = abs(B)

        if len(A)==0:
            return 0

        i, j = 0, 1
        while i<len(A) and j<len(A):
            diff = abs(A[i]-A[j])
            print(i, A[i], j, A[j], diff)
            if diff==B:
                return 1
            elif diff>B:
                i+=1
            else:
                j+=1

        return 0

s = Solution()
#A = [int(x) for x in input().split()]
#B = int(input())

A = [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ]
B = -42

print(s.solve(A,B))