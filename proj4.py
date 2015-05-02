def isPalindrome(num):
	strnum = str(num)
	ptr = 0
	while ptr < (len(strnum)-ptr):
		if(strnum[ptr] != strnum[-1-ptr]):
			return False
		ptr+=1
	return True


def main():
	palindromes = []
	num1 = 100
	while num1 < 1000:
		num2 = 100
		while num2 < 1000:
			product = num1*num2
			if(isPalindrome(product)):
				palindromes = palindromes + [product]
			num2 += 1
		num1 += 1
	i = 1
	largest = palindromes[0]
	while i < len(palindromes):
		if(palindromes[i] > largest):
			largest = palindromes[i]
		i+=1
	print("Answer is:",largest)
main()