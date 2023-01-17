# https://www.interviewbit.com/problems/implement-power-function/

class Solution:
	# @param x : integer
	# @param n : integer
	# @param d : integer
	# @return an integer
	def upow(self, x, n, d):
		if x==0:
			return 0
		if n==0:
			return 1%d
		if n==1:
			return x%d

		f = self.upow(x,n//2,d) % d
		print(f,n,d)
		f = ((f % d) * (f % d)) % d
		if n%2==1:
			f = ((x % d) * (f % d)) % d
		return f % d


	def pow(self, x, n, d):
		sign = -1 if (x<0) and n%2==1 else 1
		if x==0:
			return 0
		if abs(x)==1:
			return (sign*1)%d

		ans = 
		return self.upow(x,n,d) % d

s = Solution()
x, n, d = int(input()), int(input()), int(input())
print(s.pow(x,n,d))