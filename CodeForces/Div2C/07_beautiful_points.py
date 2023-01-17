# https://codeforces.com/problemset/problem/268/C

"""
Idea - simple and only the following points - 
1. once a point is chosen on the integral grid, all points along x and y axis wrt that point become invalid choices. 
	--> this puts the max points possible to choose at min(m,n) + 1 (because 0 can also be a coordinate)
2. between 0 and 100 there are only 2 pythagorean triplets - (3,4,5) & (6,8,10), so no pair of chosen points can have x (or y) and y (or x) diff as 3,4 or 6,8 respectively
	--> this implies we can keep choosing points with 1,1 diff over the last point, provided the diff never becomes 3,4 or 6,8

on more thought, I don't even have to think about point 2, because I can always start on the top left diagoral and keep doing (+1,-1),
and it will never have an integral dist and will exhaust max possible points
"""

n, m = [int(x) for x in input().split()]
max_points = min(m,n)+1
print(max_points)

i=0
while n>=0 and i<=m:
	print(str(n)+" "+str(i))
	n-=1
	i+=1