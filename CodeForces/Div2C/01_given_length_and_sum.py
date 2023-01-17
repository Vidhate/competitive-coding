m, s = [int(x) for x in input().split()]

# edge cases
def find_nums(m,s):
	if s==0 and m==1:
		print("0 0")
		return

	if s==0 or s>m*9:
		print("-1 -1")
		return

	maxi, mini = '', ''
	s_maxi, s_mini = s, s-1
	for i in range(m):
		maxi += ("9" if s_maxi>=9 else str(s_maxi))
		s_maxi -= (9 if s_maxi>=9 else s_maxi)

		mini = ("9"+mini if s_mini>=9 else str(s_mini)+mini)
		s_mini -= (9 if s_mini>=9 else s_mini)

	mini = "1" + mini[1:] if mini[0]==0 else str(int(mini[0])+1) + mini[1:]
	print(mini+" "+maxi)
	return

find_nums(m,s)