n, a = int(input()), [int(x) for x in input().split()]
d = {}
maxi, mini = -1, a[0]
for x in a:
	if x in d.keys():
		d[x]+=x
	else:
		d[x]=x 
	if x<mini:
		mini=x
	if x>maxi:
		maxi=x

scores_2, scores_1 = d[mini], d.get(mini+1, 0) if mini+1 in a and d[mini+1]>d[mini] else d[mini]
#print(d, nums, scores)
for num in range(mini+2, maxi+1):
	score = max(scores_2 + d.get(num, 0), scores_1)
	scores_2 = scores_1
	scores_1 = score

#print(scores)
print(scores_1)