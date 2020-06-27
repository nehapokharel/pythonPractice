def even_numbers(numbers):
    new_list = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            new_list.append(numbers[i])
    return new_list

numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = even_numbers(numberlist)
print(y)