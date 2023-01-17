# https://www.interviewbit.com/problems/longest-common-prefix/

class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):

		longest = ""
		shortest = A[0]

		for s in A:
			if len(s)<len(shortest):
				shortest=s

		for i,char in enumerate(shortest):
			x = [s[i]==char for s in A]
			if all(x):
				longest+=char
			else:
				return longest
		return longest

s = Solution()
#A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abab", "ab", "abcd"]
print(s.longestCommonPrefix(A))