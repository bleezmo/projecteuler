def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
def computeLargestDivisor(x):
	count = 2
	while count < x:
		divisor = x//count
		if(divisor*count == x):
			print("factors found:",divisor," ",count)
			return divisor
		count += 1
	raise Exception("Already is prime")
def main():
	ceil = 600851475143
	highest = computeLargestDivisor(ceil)
	while highest > 2:
		if(is_prime(highest)):
			print("Answer is:",highest)
			break
		highest = computeLargestDivisor(highest)

def main2():
	ceil = 600851475143
	lowest = 2
	highest = ceil
	while highest >= lowest:
		highest = ceil//lowest
		if(highest*lowest == ceil):
			print("factors found:",highest," ",lowest)
			if(is_prime(highest)):
				print("found prime:",highest)
		lowest += 1
main2()