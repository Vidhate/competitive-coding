class MinStack:
	def __init__(self):
		self.stack = []
		self.mini = None

	# @param x, an integer
	def push(self, x):
		
		if self.stack:
			if x<self.mini:
				self.stack.append((2*x) - self.mini)
				self.mini = x
			else:
				self.stack.append(x)
		else:
			self.mini = x
			self.stack.append(x)
		
	# @return nothing
	def pop(self):
		if len(self.stack)>1:
			if self.stack[-1]>=self.mini:
				x = self.stack[-1]
				self.stack = self.stack[:-1]
				#return x
			else:
				x = self.mini
				self.mini = (2*self.mini - self.stack[-1])
				self.stack = self.stack[:-1]
				#return x
		elif len(self.stack)==1:
			x = self.stack[-1]
			self.mini = None
			self.stack = []
			#return x

	# @return an integer
	def top(self):
		if self.stack:
			if self.stack[-1]<self.mini:
				return self.mini
			else:
				return self.stack[-1]
		else:
			return -1

	# @return an integer
	def getMin(self):
		if self.top()==-1:
			return -1
		return self.mini


	def parse(self, inp):
		inp = inp.split()
		#print(inp)
		ops, i = int(inp[0]), 1
		while i<len(inp):
			if inp[i]=='P':
				i+=1
				self.push(int(inp[i]))
				#print("\nPush: ", self.stack, "Min: ", self.mini)
				
			elif inp[i]=='p':
				#print(self.pop(), end=" ")
				#print("\nPop: ", self.stack, "Min: ", self.mini)
				self.pop()
				
			elif inp[i]=='g':
				print(self.getMin(), end=" ")
				#print("\nGetMin: ", self.stack, "Min: ", self.mini)
				
			elif inp[i]=='t':
				print(self.top(), end=" ")
				#print("\nTop: ", self.stack, "Min: ", self.mini)

			i+=1
			#print(i, inp[i:])


s = MinStack()
inp = "19 P 10 P 9 g P 8 g P 7 g P 6 g p g p g p g p g p g"
print(inp)
s.parse(inp)