#https://www.interviewbit.com/problems/simple-queries/

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return a list of integers
	def productOfDivisors(self, num):
		product = num
		mod = 10**9 + 7
		for i in range(2,int(num**0.5)+1):
			if num%i==0:
				product = ((product%mod) * (i%mod)) % mod
				if not num//i == i:
					product = ((product%mod) * ((num//i)%mod)) % mod

		return product % mod

	def solve(self, A, B):

		new_array = []
		for i in range(len(A)):
			max_element = A[i]
			new_array.append(self.productOfDivisors(max_element))

			for j in range(i+1,len(A)):
				if A[j]>max_element:
					max_element = A[j]
				new_array.append(self.productOfDivisors(max_element))

		new_array = sorted(new_array, reverse=True)
		#print(new_array)
		ans_array = []
		for i in B:
			ans_array.append(new_array[i-1])

		return ans_array

#A, B = [1, 2, 4], [1, 2, 3, 4, 5, 6]
#A, B = [1, 3], [1]
A = [ 39, 99, 70, 24, 49, 13, 86, 43, 88, 74, 45, 92, 72, 71, 90, 32, 19, 76, 84, 46, 63, 15, 87, 1, 39, 58, 17, 65, 99, 43, 83, 29, 64, 67, 100, 14, 17, 100, 81, 26, 45, 40, 95, 94, 86, 2, 89, 57, 52, 91, 45 ]
B = [ 1221, 360, 459, 651, 958, 584, 345, 181, 536, 116, 1310, 403, 669, 1044, 1281, 711, 222, 280, 1255, 257, 811, 409, 698, 74, 838 ]

s = Solution()
print(s.solve(A, B))