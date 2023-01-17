# https://www.interviewbit.com/problems/colorful-number/
from pprint import pprint
class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):

		if A==0 or A==1:
			return 1

		d = {}

		while A>0:
			dig = A%10
			if dig in d.keys():
				return 0

			cur_keys = list(d.keys())
			for k in cur_keys:
				mul = int(dig*k)
				if mul<10:
					if mul in cur_keys:
						return 0
					d[mul] = 1

			d[dig] = 1

			if dig==1 or dig==0:
				return 0
			A = A//10
			#pprint(d)
		return 1

s = Solution()
print(s.colorful(236))