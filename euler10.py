"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

----

Easy peasy, and a chance to use a generator. Fun! This got me the decathlete achievement: solved ten problems in a row.

"""


import math

def get_prime():
    n = 1
    while True:
        if is_prime(n):
            yield n
        n += 1

def loop():
    p = get_prime()
    sum = 0
    t = 0
    while t < 2000000:
        sum += t        
        t = p.next()        
    print "ding! total is: " + str(sum)

def is_prime(n): 
    if n == 1: 
        return False
    sqrt = math.sqrt(n)        
    i = 1
    if n == 2 or n == 3:
        return True
    if n%2 == 0:
        return False
    if n%3 == 0:
        return False    
    while 6*i - 1 <= sqrt:
        if ( n%(6*i - 1) == 0 or n%(6*i + 1) == 0):
            return False
        i += 1
    return True

loop()