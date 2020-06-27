numbers = input('Enter numbers: ')
numberlist = numbers.split()
sum = 0

for num in numberlist:
    sum = sum + int(num)
print('sum of numbers in list: ' + str(sum))
