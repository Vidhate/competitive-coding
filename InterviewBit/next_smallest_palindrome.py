# https://www.interviewbit.com/problems/next-smallest-palindrome/
def greater(a, b):
	if len(a)>len(b):
		return True
	if len(a)<len(b):
		return False

	for i in range(len(a)):
		if a[i]>b[i]:
			return True
		elif a[i]<b[i]:
			return False

	return True

def plusOne(num):
	dig, carry = (int(num[-1])+1)%10, int((int(num[-1])+1)/10)
	num2 = [str(dig)]
	d = len(num)-2
	while d>=0:
		dig, carry = (int(num[d])+carry)%10, int((int(num[d])+carry)/10)
		num2 = [str(dig)]+num2
		d-=1

	if carry==1:
		num2 = ["1"] + num2
	return num2


def solve(A):

	A = plusOne(A)
	i, j = 0, len(A)-1
	while i<=j and A[i]==A[j]:
		i+=1
		j-=1
	
	if i>j:
		return A
	
	pallin = ""
	if len(A)%2==1:
		half = int(len(A)/2)
		left = A[:half+1]
		right = left[:-1]
		right = right[::-1]

		if greater(right, A[half+1:]):
			pallin = "".join(left) + "".join(right)

		else:
			left = plusOne(left)
			right = left[:-1]
			pallin = "".join(left) + "".join(right[::-1])

	else:
		half = int(len(A)/2)
		left = A[:half]
		right = left[::-1]
		print(right, A[half:])

		if greater(right, A[half:]):
			pallin = "".join(left) + "".join(right)
		
		else:
			left = plusOne(left)
			pallin = "".join(left)+"".join(left[::-1])
			
	return pallin

print(solve(input()))