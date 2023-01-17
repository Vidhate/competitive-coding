# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from typing import List
class Solution:
	def reset_dictionary(self, words):
		dictionary = {word:0 for word in words}
		for word in words:
			dictionary[word]+=1

		return dictionary

	def findSubstring(self, s: str, words: List[str]) -> List[int]:
		
		dictionary = self.reset_dictionary(words)

		len_word = len(words[0])
		get_word = lambda x : s[x:x+len_word]

		answer = []
		
		i = 0
		while i < len(s)-(len_word*len(words))+1:

			w = get_word(i)
			print(w)
			if dictionary.get(w, None):
				j = i
				while j<len(s)-len_word+1 and dictionary.get(get_word(j),0)>0:
					dictionary[get_word(j)]-=1
					j+=len_word
					print(dictionary)
					
				if not any([val for key,val in dictionary.items()]):
					answer.append(i)

				dictionary = self.reset_dictionary(words)

			i+=1

		return answer

sol = Solution()
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]

# s = "barfoothefoobarman"
# words = ["foo","bar"]

# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]

s= "a"
words = ["a"]

print(sol.findSubstring(s, words))