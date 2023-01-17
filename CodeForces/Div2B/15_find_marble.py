n,s,t = [int(x) for x in input().split()]
pos = [int(x) for x in input().split()]

def find_shuffles(n,s,t,pos):
	i = 1
	if s==t:
		print(0)
		return

	while i<n:
		s = pos[s-1]
		if s==t:
			print(i)
			return
		else:
			i+=1

	print(-1)
	return

find_shuffles(n,s,t,pos)