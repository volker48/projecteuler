x = 999
y = 999
def is_palindrome(x):
    string = str(x)
    reversed = string[::-1]
    return string == reversed

while x and y > 0:
    product = x * y
    if is_palindrome(product):
        print product
        break

