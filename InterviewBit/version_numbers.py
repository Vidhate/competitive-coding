# https://www.interviewbit.com/problems/compare-version-numbers/

class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def compare(self, a, b):
		ai, bi = 0, 0
		while int(a[ai])==0:
			ai+=1
		while int(b[bi])==0:
			bi+=1

		a, b = a[ai:], b[bi:]
		if len(a)>len(b):
			return 1
		elif len(a)<len(b):
			return -1
		else:
			a = a[::-1]
			b = b[::-1]
			for i in range(len(a)):
				if a[i]>b[i]:
					return 1
				elif a[i]<b[i]:
					return -1

		return 0

	def compareVersion(self, A, B):
		
		va = A.split('.')
		vb = B.split('.')

		l = len(va) if len(va)<len(vb) else len(vb)
		i = 0
		eq_flag = 1
		while i<l:
			res = self.compare(va[i], vb[i])
			if res==-1:
				return -1
			elif res==0:
				eq_flag=1
			else:
				eq_flag=0
			i+=1

		if len(vb)>l:
			while i<len(vb) and int(vb[i])==0:
				i+=1

			if not i==len(vb):
				return -1

		elif len(va)==len(vb) and eq_flag:
			return 0

		else:
			while i<len(va) and int(va[i])==0:
				i+=1

			if i==len(va) and eq_flag:
				return 0

		return 1

s = Solution()
print(s.compareVersion(input(), input()))