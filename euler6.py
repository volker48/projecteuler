def sum_of_squares(limit):
    return sum([x**2 for x in range(limit)])

def square_of_sum(limit):
    return sum(range(limit))**2

print square_of_sum(101) - sum_of_squares(101)