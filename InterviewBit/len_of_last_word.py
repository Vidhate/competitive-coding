# https://www.interviewbit.com/problems/length-of-last-word/
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
		word = ""
		last_len = 0
		last_word=""
		for i,char in enumerate(A):
			if char==' ':
				word = word if last_word=="" else last_word
				last_word=""
			else:
				last_word+=char

			print(word, last_word)

		if not len(last_word)==0:
			return len(last_word)

		return len(word)

s = Solution()
print(s.lengthOfLastWord(input()))