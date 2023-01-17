def binary(x):
	s = ""
	if x==0:
		s = "0"
	else:
		while x>0:
			s = str(x%2) + s
			x = int(x/2)

	if len(s)==32:
		return s

	while len(s)<32:
		s = "0"+s

	return s

binary(int(input()))