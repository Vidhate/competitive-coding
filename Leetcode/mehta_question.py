"""
Q. In rephrase.ai, one of common infra challenges that we deal is about optimizing computation time to occur less cost. 
Let's say we have a service which takes string as an input (e.g. "Good morning, Shubham") and covert it into video with default actor. 
The time it takes to perform this operation is len(string) + 5 sec.
#
# Now let's say you have given a personalized text (e.g. "Hey $name, how are you doing"?) 
and values that the personalized variable (e.g. $name) can take (e.g. Shubham, Aman, Vishwajeet). 
You have to tell what is the minimum computation time it will take to generate all videos of the given personalized text

st = 10:05
"""
from typing import Dict, List
class Solution():
	def solve(self, template : str, personalization_list : Dict[str, List[str]]) -> int:

		if not '$$' in template:
			return len(template)+5

		# Finding fixed cost from creating video for non-personalized part of the template
		fixed_cost = 5
		last_anchor, anchor = 0, 0
		while template.find('$$', last_anchor+1)!=-1:
			anchor = template.find('$$', last_anchor+1)
			fixed_cost+=(anchor-last_anchor-2)
			#print(template[last_anchor:anchor])
			last_anchor = template.find('$$', anchor+1)

		#print(template[last_anchor+2:])
		fixed_cost+=(len(template[last_anchor+2:]))

		#print(fixed_cost)

		word_len_sum = 0
		for key,val in personalization_list.items():
			personal_string = " ".join(val)
			#print(personal_string)
			word_len_sum += len(personal_string)

		#print(word_len_sum)

		return fixed_cost+word_len_sum

s = Solution()
print(s.solve("""Some sentence with which this begins Hey $$name$$ <N>, 
	how are you doing? How is the weather in $$city$$ <N> 
	some sentence with which it ends?
	""",
	{"name" : ["Shubham", "Aman", "Vishwajeet"], "city": ["mumbai", "mumbai", "bangalore"]}))


# Time can be further reduced for cases like vi-neet, vi-sh-nu, vi-sh-wa-jeet, vi-sh-wa-ngi : prefix optimization
# Time can also be saved for cases like aman-deep, san-deep; adit-ya, lavan-ya, amavas-ya : postfix optimization