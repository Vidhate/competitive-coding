# https://www.interviewbit.com/problems/valid-ip-addresses/

class Solution:
	# @param A : string
	# @return a list of strings

	def checkValidTerm(self, term):
	
		if len(term)>3 or len(term)==0:
			return False
		if len(term)>1 and int(term[0])==0:
			return False
		if int(term)>255:
			return False

		return True


	def findValid(self, A, term_num):

		#print("At term",term_num,A)
		if term_num==4:
			if self.checkValidTerm(A):
				return [A]
			else:
				return []

		if not self.checkValidTerm(A[0]):
			return []

		validTerms = []
		limit = min(4, len(A))
		for i in range(1,limit):
			term = A[:i]
			if self.checkValidTerm(term):
				validTerms.extend([term+"."+post for post in self.findValid(A[i:], term_num+1)])
				
		return validTerms


	def restoreIpAddresses(self, A):
		return self.findValid(A, 1)

s = Solution()
print(s.restoreIpAddresses(input()))