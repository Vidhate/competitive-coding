# Make an array beautiful
# https://codeforces.com/contest/1783/problem/A

from collections import Counter

t = int(input())
arrays = []
for _ in range(t):
	input()
	arrays.append([int(x) for x in input().split(' ')])

for array in arrays:
	if len(set(array))<=1:
		print("NO")
		continue

	array = sorted(array, reverse=True)
	if array[0]==array[1]:
		x = array[-1]
		array[-1] = array[0]
		array[0] = x

	print("YES")
	print(' '.join(map(str, array)))