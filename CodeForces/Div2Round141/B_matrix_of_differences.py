# Maximize the beauty of a matrix
# https://codeforces.com/contest/1783/problem/B

t = int(input())

matrices = []
for _ in range(t):
	matrices.append(int(input()))

for matrix in matrices:

	a, b = 1, matrix**2
	beauty = [[0 for _ in range(matrix)] for _ in range(matrix)]

	for i in range(matrix):

		if i%2:
			for j in range(matrix-1,-1,-1):
				if j%2:
					beauty[i][j]=a
					a+=1
				else:
					beauty[i][j]=b
					b-=1

		else:
			for j in range(matrix):
				if j%2:
					beauty[i][j]=b
					b-=1
				else:
					beauty[i][j]=a
					a+=1

	for i in range(matrix):
		print(' '.join(map(str,beauty[i])))
		