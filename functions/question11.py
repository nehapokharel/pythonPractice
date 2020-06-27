def sum_number():
    return lambda x : x + 15

y = sum_number()
print("sum: " + str(y(5)))

def multiple_number():
    return lambda x, y: x * y

z = multiple_number()
print("multiple: " + str(z(2, 5)))