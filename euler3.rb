
def is_prime?(n)
	return true if [1,2,3].include?(n)
	return false if (n%2 == 0) or (n%3 == 0) 
	sqrt = Math.sqrt(n)
	i = 1
	while (6*i-1) <= sqrt do		
		return false if n%(6*i - 1 ) == 0  or n%(6*i + 1) == 0 	#all primes are of form 6i +/- 1
		i += 1
	end
	true
end

def biggest_prime_factor(n)
	return n if is_prime?(n)
	i = 2.0
	prime_factor = -1
	while i <= Math.sqrt(n)
		if n%i == 0
			if is_prime?(i)
				prime_factor = i if ( i > prime_factor  )
			else
				factor = n/i				
				if is_prime?(factor)
					prime_factor = factor if ( factor > prime_factor)
				end
			end			
		end
		i += 1
	end
	(prime_factor == -1) ? result = "No prime factors" : result = "Greatest prime factor: #{prime_factor}"
	puts result
end

puts biggest_prime_factor(600851475143)
