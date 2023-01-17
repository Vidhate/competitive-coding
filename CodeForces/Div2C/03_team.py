n, m = [int(x) for x in input().split()]

def find_seq(n,m):

	if m>(n+1)*2 or n>m+1:
		print(-1)
		return

	seq = ""
	while m>0 and n>0:
		
		if m==n:
			if len(seq)>0:
				if seq[-1]=="1":
					seq+=("01"*m)
				else:
					seq+=("10"*m)
			else:
				seq = ("01"*m)

			print(seq)
			return

		if m>n:
			if len(seq)>1 and seq[-2:]=="11":
				seq+="0"
				n-=1
			else:
				seq+="1"
				m-=1
		
		else:
			if len(seq)>0 and seq[-1]=="0":
				seq+="1"
				m-=1
			else:
				seq+="0"
				n-=1

		#print(seq)

	while m>0:
		if seq[-2:]!="11":
			seq+="1"
			m-=1
		elif seq[:2]!="11":
			seq = "1"+seq
			m-=1

		#print(seq)

	while n>0:
		if seq[-1]!="0":
			seq+="0"
			n-=1
		elif seq[0]!="0":
			seq = "0"+seq
			n-=1

		#print(seq)

	print(seq)
	return

find_seq(n,m)