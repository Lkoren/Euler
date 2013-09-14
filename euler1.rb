def sieve(n)
	return n if (n%3 == 0) || (n%5 == 0)
end

def loop()
	sum = 0
	(0..20).inject{ |n| print sieve(n) }	
end

loop()