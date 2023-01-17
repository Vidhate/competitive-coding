# https://www.interviewbit.com/problems/allocate-books/
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def maxStudents(self, A, max_pages):
        pages, ppl = 0, 1
        for val in A:
            pages+=val
            if pages>max_pages:
                ppl+=1
                pages=val

        return ppl

	def books(self, A, B):
        if B>len(A):
            return -1

        low, high = max(A), sum(A)
        ans = 0
        while low<=high:
            mid = (low+high)//2
            v = self.maxStudents(A, mid)
            if v>B:
                low = mid+1
            else:
                ans = mid
                high = mid-1

        return ans
		

s = Solution()
A, B = [int(x) for x in input().split()], int(input())
print(s.books(A, B))