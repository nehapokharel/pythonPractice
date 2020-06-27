def multiple_of_list(numberlist):
    multiple = 1
    for num in numberlist:
        multiple = multiple * int(num)
    return multiple

samplelist = [8, 2, 3, -1, 7]

y = multiple_of_list(samplelist)
print('multiple of numbers in list: ' + str(y))