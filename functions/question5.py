def find_factorial(num):
    factorial = 1
    if num < 1:
        print("please enter non negative numbers")
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        return factorial

num = int(input('Enter number: '))
y = find_factorial(num)
print("the factorial of " + str(num) + " is: " + str(y))