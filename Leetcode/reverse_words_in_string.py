# https://leetcode.com/problems/reverse-words-in-a-string/
# st : 4:15PM end : 4:17PM

class Solution:
	def reverseWords(self, s: str) -> str:
		s = s.split()
        return " ".join(s[::-1])