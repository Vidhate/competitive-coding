n = int(input())

# Assume squirrel has had nut on the prev tree and is at it's top. 
# In this, compute time to jump to next tree, go to top and have nut

h_prev = int(input())
time = h_prev + 1

for i in range(n-1):
	h_cur = int(input())
	time += abs((h_prev-h_cur)) + 2
	h_prev = h_cur

print(time)