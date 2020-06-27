def sum_of_list(numberlist):
    sum = 0
    for num in numberlist:
        sum = sum + int(num)
    return sum

samplelist = [8, 2, 3, 0, 7]

y = sum_of_list(samplelist)
print('sum of numbers in list: ' + str(y))
