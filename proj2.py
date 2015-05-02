def main():
	total = 2
	last = 2
	fibsum = 3
	while fibsum <= 4000000:
		temp = fibsum
		fibsum = fibsum + last
		last = temp
		half = fibsum // 2
		if(half*2 == fibsum):
			total = total + fibsum
	print(total)

main()