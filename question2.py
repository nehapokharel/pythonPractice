word = input('enter string: ')

if len(word)>1:
    print(word[:2]+word[-2:])
else:
    print("empty string")
