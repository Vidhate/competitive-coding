# https://leetcode.com/problems/4sum/
from pprint import pprint
class Solution:
	def fourSum(self, nums, target):
		
		d = {}
		res = set()
		# O(N^2) to build this dict
		for a in nums:
			for b in nums:
				if a!=b:
					s = a+b
					if s in d.keys():
						pair = tuple(sorted([a,b]))
						d[s].add(pair)
					else:
						d[s] = set()
						pair = tuple(sorted([a,b]))
						d[s].add(pair)
		
		pprint(d)
		# O(N^2) to find a+b+c+d = Target
		for s in d.keys():
			if d.get(target-s,None):
				l1 = d[s]
				l2 = d[target-s]
				
				for t1 in l1:
					for t2 in l2:
						if not t1[0] in t2 and not t1[1] in t2:
							r = tuple(sorted(list(t1)+list(t2)))
							res.add(r)
		res = list(res)
		res = [list(x) for x in res]
		return res

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))