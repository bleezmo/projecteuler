def computeA(b):
	return (500000-(1000*b))/(1000-b)
def main():
	b = 0
	a = computeA(b)
	c = 0
	while True:
		b+=1
		a = computeA(b)
		if(int(a) == a and a < b and a > 0):
			c = (1000-a)-b
			if(b < c and c > 0 and int(c) == c):
				break
	print(a,b,c)
	print("Answer is:",(a*b*c))

main()