# https://codeforces.com/contest/1775/problem/A1
# O(N) solution

t = int(input())

names = [input() for _ in range(t)]

for name in names:

	l, r = 1, len(name)-1
	while l<r:
		left, mid, right = name[:l], name[l:r], name[r:]
		if (left<=mid and right<=mid) or (left>=mid and right>=mid):
			print(f"{left} {mid} {right}")
			break

		if left<mid:
			l+=1
		elif right<mid:
			r-=1

	if l>=r:
		print(":(")