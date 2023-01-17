def hammingDistance(A):

	all_binary = []
	for a in A:
		all_binary.append(binary(a))

	print(all_binary)

	s = 0
	for i in range(32):
		one, zero = sum([1 for a in all_binary if a[i]=='1']), sum([1 for a in all_binary if a[i]=='0'])
		s += (2*one*zero)
		print(one, zero, s, i)

	return s%1000000007

hammingDistance([int(x) for x in input().split()])