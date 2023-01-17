# https://codeforces.com/contest/1775/problem/A2
# O(logN) solution

t = int(input())

names = [input() for _ in range(t)]

for name in names:
	l, r = 1, len(name)-1
	mid = name[l:r]
	if not 'a' in mid:
		print(f"{name[:l]} {name[l:r]} {name[r:]}")
		continue

	else:
		l += mid.find('a')
		print(f"{name[:l]} {name[l:l+1]} {name[l+1:]}")
		continue

	print(":(")

# aaab
# a a ab
