def check_number(maxvalue, num):
    if num in range(1,maxvalue):
        print("Number is in range!!")
    else:
        print("Number not in range!!")


value = int(input('Enter maxvalue: '))
num = int(input('Enter number: '))
check_number(value, num)