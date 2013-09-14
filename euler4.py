import math

def is_palindrome(n):
	if (str(n) == str(n)[::-1]): 
		return True
	return False

def loop(n):
	factors = range(100, 1000)
	factors.reverse()
	for factor in factors:
		if size(n/factor) > 3:
			break
		if (test(n, factor)):	
			return {"palindrome": n, "factors": [factor, n/factor]}

def main():
	start = 997799 #largest palimdrome less than 999*999
	while True:
		if is_palindrome(start):
			p = loop(start)
			if (p):
				print "ding!"				
				print p
				return
		start -= 1


def size(n):
	return int(math.log10(n))+1

def test(n,i): #is n the product of two three digit numbers?
	return n%i == 0 and size(n/i) == 3 and size(i) == 3



main()