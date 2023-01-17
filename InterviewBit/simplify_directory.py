# https://www.interviewbit.com/problems/simplify-directory-path/

class Solution:
	# @param A : string
	# @return a strings
	def simplifyPath(self, A):

		directory_stack = []
		for d in A.split('/'):
			if d in ["","."]:
				continue
			elif d=='..':
				directory_stack = directory_stack[:-1]
			else:
				directory_stack.append(d)

		print(A.split('/'))
		print(directory_stack)

		return "/"+"/".join(directory_stack)

s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))