def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def main():
	num = 3
	total = 2
	while num < 2000000:
		if(is_prime(num)):
			total += num
		num+=2
	print("Answer is:",total)
main()