"""
Problem nine: 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

-----

Using Dickson's method we can find *all* triplets: find positive integers r, 
s, t, such that r^2 = 2*s*t. Then: x = r + s, y = r + t, z = r + s + t. 


"""
import math

def loop(): 
    t = 1
    r = 1
    s = 1
    for s in xrange(1, 998):                
        while True:
            r = math.sqrt(2*s*t)
            if is_square(2*s*t):
                r = math.sqrt(2*s*t)
                if (3*r + 2*s + 2*t == 1000):
                    print "x, y, z = (%(x)d, %(y)d, %(z)d" % \
                        {"x":r+s, "y": r+t, "z": r+s+t}
                    return            
            t += 1            
            if ((3*r + 2*s + 2*t) > 1000):    
                t = 1        
                break           
        
def is_square(x):
    sqrt = math.sqrt(x)
    if sqrt == int(sqrt):
        return True
    return False

loop()