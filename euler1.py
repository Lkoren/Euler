def sieve(n):
	if (n%3 == 0) or (n%5 == 0):
		return n


def loop():
	sum = 0
	for i in range(1000):
		if sieve(i):
			sum += i
	print sum
	return sum

loop()