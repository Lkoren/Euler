
import math

class PrimeFinder(object):
    primes = [2,3]

    def is_prime(self, n): 
        if n == 1:
            return False
        if (n in self.primes): 
            return True
        for p in self.primes:
            if p <= math.sqrt(n):        
                if n%p == 0:   
                    return False    
        self.primes.append(n)        
        return True

    def is_prime2(self, n): #included for benchmarking. Like 100x faster!
        if n == 1: 
            return False
        sqrt = math.sqrt(n)        
        i = 1
        if n%3 == 0:
            return False
        while 6*i - 1 <= sqrt:
            if ( n%(6*i -1) == 0 or n%(6*i + 1) == 0):
                return False
            i += 1
        self.primes.append(n)
        return True

    def loop(self):
        i = 1
        while len(self.primes) < 10001: 
            self.is_prime2(i)
            i += 2
        print self.primes[len(self.primes)-1]
        #print self.primes

p = PrimeFinder().loop()