f1, f2 = [int(x) for x in input().split(' ')]
n = int(input())

f3 = f2 - f1
base = 1000000007

x, y = n%3, int(n/3)

if n==3:
	res = f3

elif n==2:
	res = f2

elif n==1:
	res = f1

elif x==0:
	if y%2==1:
		res = f3
	else:
		res = (-1*f3)

elif x==1:
	if y%2==0:
		res = f1
	else:
		res = (-1*f1)

else:
	if y%2==0:
		res = f2
	else:
		res = (-1*f2)

print(res%base)