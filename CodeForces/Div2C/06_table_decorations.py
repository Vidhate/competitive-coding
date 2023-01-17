r, g, b = [int(x) for x in input().split()]
# Explainer of the solution is here - https://codeforces.com/blog/entry/18619)

def find_tables(r,g,b):

	mn, md, mx = sorted([r,g,b])
	if (mn+md)*2<=mx:
		print(mn+md)
	else:
		print(int((mn+md+mx)/3))

find_tables(r,g,b)