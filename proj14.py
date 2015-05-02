def computeChain(x):
	chain = 0
	while x != 1:
		chain += 1
		if((x//2)*2 == x):
			x = x//2
		else:
			x = (3*x)+1
	return chain+1
def main():
	x = 0
	largest = 0,0
	while x < 1000000:
		x+=1
		length = computeChain(x)
		if(length>largest[0]):
			largest = (length,x)
	print("largest chain length:",largest[0],"with starting number:",largest[1])

main()