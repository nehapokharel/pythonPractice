def multiple_number(num):
    return lambda x : x * num

z = multiple_number(3)
print("multiple: " + str(z(2)))