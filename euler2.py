def oneonetwothree():
	first = 1
	second = 2
	while True:
		temp = first + second
		first = second
		second = temp
		yield temp

def even(n):
	if (n%2 == 0):
		return n
	else:
		return 0

def loop():
	n = oneonetwothree()
	sum = 2
	while True:
		t = n.next()
		sum += even(t)
		if t > 4000000:
			print sum
			return sum

loop()


