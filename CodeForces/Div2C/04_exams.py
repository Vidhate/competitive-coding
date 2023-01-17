n = int(input())
a = []
for i in range(n):
	a.append([int(x) for x in input().split()])

def find_min_day(n, a):
	a = sorted(a, key=lambda x:x[1])
	a = sorted(a, key=lambda x:x[0])
	day = min(a[0])
	for exam in a:
		ex = [x for x in exam if x>=day]
		day = min(ex)
	print(day)
	return

find_min_day(n,a)