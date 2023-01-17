def maxSubArray(A):
	"""
	# O(n*n) solution - find sum of every possible window of size 1 to N and compare/replace against global max
	s = A[0]
        if len(A)==1:
            return s

        for i in range(len(A)):
            window = i+1
            start = 0
            sc = sum(A[start:start+window])
            s = sc if sc>s else s
            while start+window<len(A):
                sc += (A[start+window]-A[start])
                s = sc if sc>s else s
                start+=1

        return s
    """

    # O(n) solution - loop once over all elements, at each position find the max sum possible until the prev element.
    # check if adding the current element to prev sum is better or restarting the sum is better
    prev = A[0]
    s = A[0]
    for a in A:
    	n = max(a, a+prev)
    	s = n if n>s else s
    	prev = n

    return s


print(maxSubArray([int(x) for x in input().split()]))