# https://www.interviewbit.com/problems/sorted-permutation-rank-with-repeats/

class Solution:
	# @param A : string
	# @return an integer
	def __init__(self):
		pass

	def power(self, a, b):
		mod = 1000003
		if a==0:
			return 0
		if b==0:
			return 1
		if b==1:
			return a
		if b%2==0:
			res = self.power(a,b//2)
			return ((res%mod) * (res%mod)) % mod
		else:
			res = ((a%mod) * (self.power(a,(b-1))%mod)) % mod
			return res % mod

	def findRank(self, A):

		mod = 1000003
		n = len(A)
		fact = [1]
		occur = {}
		for f, char in enumerate(A):	
			fact.append(((f+1) % mod) * (fact[-1] % mod) % mod)

			if char in occur:
				occur[char]+=1
			else:
				occur[char]=1

		print(occur)

		ans = 0
		for i, char in enumerate(A):
			pos = n - i - 1
			rank = 0
			c = 0
			for char2 in A[i+1:]:
				if char2<char:
					c+=1

			den = 1
			for _,count in occur.items():
				den = ((den % mod) * (fact[count] % mod)) % mod

			ans += c * ((fact[pos] % mod) * (self.power(den, mod-2) % mod)) % mod
			ans = ans % mod

			occur[char]-=1
			if occur[char]==0:
				occur.pop(char)

		return (ans + 1) % mod

s = Solution()
s.findRank(input())