# https://www.interviewbit.com/problems/maximum-absolute-difference/
def maxArr(A):

	"""
	# O(n*n) solution
    s = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            sc = abs(A[i]-A[j]) + abs(i-j)
            s = sc if sc>s else s

    return s
    """

    # O(n) solution
    max1, min1 = A[0], A[0]
    max2, min2 = A[0], A[0]
    for i,val in enumerate(A[1:]):
    	t1, t2 = val+i, val-i
    	max1 = t1 if t1>max1 else max1
    	min1 = t1 if t1<min1 else min1
    	max2 = t2 if t2>max2 else max2
    	min2 = t2 if t2<min2 else min2

    return max(max1-min1, max2-min2)