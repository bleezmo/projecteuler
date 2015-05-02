def main():
	num = 2520
	while True:
		isNum = True
		for i in range(1,21):
			if((num//i)*i != num):
				isNum = False
				break
		if(isNum):
			break
		num+=10
	print("Answer is:",num)
main()