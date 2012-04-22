def products(x, y):
    for a in xrange(x, 99, -1):
        for b in xrange(a, 99, -1):
            yield a * b

def is_palindrome(toCheck):
    toCheck = str(toCheck)
    reversed = toCheck[::-1]
    return toCheck == reversed

for product in products(999,999):
    if is_palindrome(product):
        print product
