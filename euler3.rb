
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
	while i <= Math.sqrt(n)
		factor = n/i
		if is_whole?(factor) 
			puts "#{i}: whole: #{factor}"
			if is_prime?(factor) 
				puts "Greates prime factor: #{factor}"
				return factor
			end
		end
		i += 1
	end
end

def is_whole?(n)
	return true if n == n.floor
	false
end

puts biggest_prime_factor(13195)