import math
def sieve(stop):
    stopsqrt = math.sqrt(stop)
    m = 2
    composite = set()
    while m <= stopsqrt:
        if m not in composite:
            yield m
            for k in xrange(m, stop, m):
                composite.add(k)
        m += 1
    for x in xrange(int(stopsqrt), stop):
        if x not in composite:
            yield x

for prime in sieve(1000000):
    if 600851475143 % prime == 0:
        print prime
