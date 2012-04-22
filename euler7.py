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
count = 1
for prime in sieve(10000000):
    if count == 10001:
        print prime
        break
    count += 1
