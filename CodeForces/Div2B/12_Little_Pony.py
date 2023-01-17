_ = input()
seq = [int(x) for x in input().split(' ')]

i=0
while i<len(seq)-1 and seq[i]<=seq[i+1]:
	i+=1

if i==len(seq)-1:
	print(0)

elif seq[-1]>seq[0]:
	print(-1)

else:
	i+=1
	steps = len(seq[i:])
	while i<len(seq)-1 and seq[i]<=seq[i+1]:
		i+=1

	if i==len(seq)-1:
		print(steps)
	else:
		print(-1)
	