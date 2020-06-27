string= input('Enter input: ')
result=string.replace('.','')
if result.isdigit():
    print(str(result) + " is a number.")
else:
    print(str(result) + " is not a number.")
