n = int(input())
a = [int(x) for x in input().split()]

def find_ways(n,a):
	
	s = sum(a)
	s_by3 = int(sum(a)/3)
	s_2by3 = 2*s_by3

	if n<=2 or s%3!=0:
		print(0)
		return

	si = 0
	num_ways, permutation = 0, 0
	i=0
	while i<n-1:
		si+=a[i]

		if si==s_2by3:
			num_ways+=permutation

		if si==s_by3:
			permutation+=1

		i+=1
	print(num_ways)
	return

find_ways(n, a)