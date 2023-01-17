# https://codeforces.com/contest/1775/problem/C

def msbPos(n):
 
    msb_p = -1
    while (n > 0):
     
        n = n >> 1
        msb_p += 1
     
    return msb_p

def andOperator(x, y):
 
    res = 0 # Initialize result
 
    while (x > 0 and y > 0):
     
        # Find positions of MSB in x and y
        msb_p1 = msbPos(x)
        msb_p2 = msbPos(y)
 
        # If positions are not same, return
        if (msb_p1 != msb_p2):
            break
 
        # Add 2^msb_p1 to result
        msb_val = (1 << msb_p1)
        res = res + msb_val
 
        # subtract 2^msb_p1 from x and y.
        x = x - msb_val
        y = y - msb_val
 
    return res


t = int(input())
for _ in range(t):
	inp = input()
	num1, num2 = map(int, inp.split(' '))
	# print("\n",num1, num2)
	if num2>num1:
		print(-1)
		continue

	if num2==num1:
		print(num2)
		continue

	if num2==0:
		last_dig = 0
		k = 1
		while k<=num1:
			k*=2
		print(k)
		continue

	l, r = num1, int(2*num1)
	ans = -1
	while l<=r:
		mid = (l+r)//2
		res = andOperator(mid, num1)
		if res < num2:
			r = mid-1
		elif res >num2:
			l = mid+1
		else:
			ans = mid
			r = mid-1

	print(ans)