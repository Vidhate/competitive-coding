# https://codeforces.com/contest/1775/problem/B

t = int(input())

for _ in range(t):
	bitsdict, bitslist = {}, []
	k = int(input())
	for _ in range(k):
		bitset = [int(x) for x in input().split(' ')][1:]
		bitslist.append(bitset)
		for bit in bitset:
			if bitsdict.get(bit, False):
				bitsdict[bit] += 1
			else:
				bitsdict[bit] = 1

	flag = False
	for bitset in bitslist:
		if any(bitsdict[bit]==1 for bit in bitset):
			continue
		else:
			flag=True
			break

	if flag:
		print("Yes")
	else:
		print("No")