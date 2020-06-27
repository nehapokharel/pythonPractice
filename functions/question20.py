first_array = [1, 2, 3, 4, 5]
second_array = [1, 3, 5]

common_element = list(filter(lambda a: a in first_array, second_array))
print(common_element)