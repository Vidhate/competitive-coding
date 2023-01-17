# https://www.interviewbit.com/problems/painters-partition-problem/
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def isPossible(self, A, time, under):
		time_taken = 0
		painters = 1
		for t in time:
			time_taken+=t
			if time_taken>under:
				painters+=1
				time_taken=t

		print("painters = ",painters)
		if painters>A:
			return False
		return True

	def paint(self, A, B, C):
		paint_time = [x*B for x in C]
		low, high = max(paint_time), sum(paint_time)
		ans = high
		while low<high:
			mid = (low+high)//2
			print("under = ",mid,end=" ")
			if self.isPossible(A, paint_time, mid):
				ans = mid if mid<ans else mid
				high = mid-1
			else:
				low = mid+1

		return ans%10000003

A, B = int(input()), int(input())
#C = [int(x) for x in input().split()]
C = [ 640, 435, 647, 352, 8, 90, 960, 329, 859 ]
s = Solution()
print(s.paint(A, B, C))