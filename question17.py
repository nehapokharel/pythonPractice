numbers = input('Enter numbers: ')
numberlist = numbers.split()
multiple = 1

for num in numberlist:
    multiple = multiple * int(num)
print('multiple of numbers in list: ' + str(multiple))