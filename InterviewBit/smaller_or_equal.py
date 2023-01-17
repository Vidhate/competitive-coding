# https://www.interviewbit.com/problems/smaller-or-equal-elements/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def binarySearch(self, A, B):
        l, r = 0, len(A)-1
        while l<=r:
            mid = (l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                l+=1
            else:
                r-=1
        
        return (l+r)//2

    def solve(self, A, B):
        f = self.binarySearch(A, B)
        print(f)
        while f+1<len(A) and A[f]==B:
            x = self.binarySearch(A[f+1:],B)
            f = f+1+x
            print(x,f)
            if x<0:
                break
            
        return f+1

s = Solution()
A, B = [int(x) for x in input().split()], int(input())
print(s.solve(A,B))