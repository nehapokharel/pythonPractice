def unique_numbers(numbers):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)        
    return new_list

numberlist = [1, 2, 3, 3, 3, 3, 4, 5]
y = unique_numbers(numberlist)
print(y)