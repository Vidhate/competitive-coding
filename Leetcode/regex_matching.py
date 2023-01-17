# https://leetcode.com/problems/regular-expression-matching/

"""
Examples - 
"aaaaaaaaaaaab"; "a*aa*ab"; True
"aaabababababbab"; "|a*|aba|.*||b*|ab"; True
""
"""

class Solution:

	"""
	Logic : 
	- need to handle star characters separately since they lead to matching sequences, rest all are direct matches
	- can we pre-check if * exists in a string? and remove that and check consistency with all other characters 
	"""
    def isMatch(self, s: str, p: str) -> bool:
        
    	s2 = s
    	