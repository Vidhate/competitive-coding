# https://leetcode.com/problems/multiply-strings/

class Solution:
	def normalize(self, local):
		self.res = [self.res[i]+local[i] for i in range(len(local))]
		for i in range(len(self.res)):
			if self.res[i]>9:
				self.res[i]%=10
				self.res[i+1]+=1

	def multiply(self, num1: str, num2: str) -> str:
		
		if num1=="0" or num2=="0":
			return "0"
		if num1=="1": return num2
		if num2=="1": return num1

		self.res = [0 for i in range(len(num1)+len(num2)+2)]
		
		for i, ni in enumerate(num1[::-1]):
			local = [0 for i in range(len(num1)+len(num2)+2)]
			for j, nj in enumerate(num2[::-1]):
				self.res[i+j] += int(ni)*int(nj)
				self.res[i+j+1] += self.res[i+j]//10
				self.res[i+j] %= 10
				
			#print(self.res[::-1])

		self.res = self.res[::-1]
		e = 0
		while self.res[e]==0:
			e+=1

		#print("Result",e)
		self.res = list(map(str, self.res))
		return ''.join(self.res[e:])

s = Solution()
print(s.multiply("123456789","987654321"))

		