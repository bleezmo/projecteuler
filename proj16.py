def main():
	num = 2**1000
	total = 0
	for ch in str(num):
		total = total + int(ch)
	print(total)

main()