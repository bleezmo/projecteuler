MAX = 21
# old way to compute
# class Acc:
# 	def __init__(self):
# 		self.i = 1
# 	def incr(self):
# 		self.i+=1
# 	def paths(self):
# 		return self.i

# def left(x,y,acc):
# 	if(x < MAX):
# 		down(x+1,y,acc)
# 		left(x+1,y,acc)
# 	elif(y>=MAX):
# 		acc.incr()
# def down(x,y,acc):
# 	if(y < MAX):
# 		down(x,y+1,acc)
# 		left(x,y+1,acc)
# 	elif(x >= MAX):
# 		acc.incr()
# def oldmain():
# 	y = 0
# 	x = 0
# 	acc = Acc()
# 	down(x,y,acc)
# 	left(x,y,acc)
# 	print("Number of paths:",acc.paths())

# new way. uses node values
def computeNode(x,y,numgrid):
	topval = 0
	if(y>0 and x>0):
		numgrid[y][x] = numgrid[y-1][x]+numgrid[y][x-1]
		print("node value for ("+str(x)+","+str(y)+"):",numgrid[y][x])
	elif(y>0 or x>0):
		numgrid[y][x] = 1
def populateGrid():
	numgrid = []
	for y in range(MAX):
		numgrid = numgrid + [[]]
		for x in range(MAX):
			numgrid[y] = numgrid[y] + [0]
	return numgrid
def main():
	numgrid = populateGrid()
	for x in range(MAX):
		for y in range(MAX):
			computeNode(x,y,numgrid)
			
main()