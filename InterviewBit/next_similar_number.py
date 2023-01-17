# https://www.interviewbit.com/problems/next-similar-number
def solve(A):
		
	s = ""
	j = len(A)-1
	rightmost = -1
	replace = -1
	while j>=0 and j>rightmost:
		print(A[j])
		for i in range(int(A[j])):
			print(i)
			r = A.rfind(str(i), 0, j)
			if r>rightmost:
				rightmost = r
				replace = j
				print(A[r], r, A[j], j)
		j-=1

	if rightmost==-1:
		return -1
	
	s = "".join(A[:rightmost]) + A[replace] + "".join(sorted(A[rightmost:replace] + A[replace+1:]))
	return s

print(solve(input()))