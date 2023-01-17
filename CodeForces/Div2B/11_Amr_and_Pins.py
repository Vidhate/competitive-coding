r, x, y, x2, y2 = [int(x) for x in input().split(' ')]
dist = ((x2-x)**2 + (y2-y)**2)**0.5

if dist==0:
	print(0)
elif dist<=2*r:
	print(1)
else:
	d_steps = int(dist/(2*r))
	steps = d_steps if dist%(2*r)==0 else d_steps+1
	print(steps)