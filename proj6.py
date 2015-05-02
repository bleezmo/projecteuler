def main():
	sumsquares = 0
	squaresum = 0
	for i in range(1,101):
		sumsquares = sumsquares + (i**2)
		squaresum = squaresum + i
	squaresum = squaresum**2
	difference = squaresum-sumsquares
	print("Answer is:",difference)
main()