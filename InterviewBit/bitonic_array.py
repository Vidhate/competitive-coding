# https://www.interviewbit.com/problems/search-in-bitonic-array/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def findInflection(self, A):
        l,r =0, len(A)-1
        while l<=r:
            mid = (l+r)//2
            if (mid<len(A)-1 and A[mid+1]<A[mid] and A[mid-1]<A[mid]):
                return mid
            elif (mid<len(A)-1 and A[mid+1]>A[mid]) or (mid>1 and A[mid-1]<A[mid]):
                l+=1
            else:
                r-=1

        return -1

    def binarySearch(self, A, B, reverse=False):

        l,r = 0, len(A)-1
        while l<=r:
            mid = (l+r)//2
            if A[mid]==B:
                return mid

            elif B>A[mid]:
                if reverse:
                    r-=1
                else:
                    l+=1
            else:
                if reverse:
                    l+=1
                else:
                    r-=1

        return -1


    def solve(self, A, B):
        
        inflect = self.findInflection(A)
        print(inflect)
        f = self.binarySearch(A[:inflect+1], B)
        print(f)
        if f>=0:
            return f
        f = self.binarySearch(A[inflect+1:], B, reverse=True)
        if f>=0:
            return inflect+1+f
        
        return -1

s = Solution()
A, B = [int(x) for x in input().split()], int(input())
print(s.solve(A,B))