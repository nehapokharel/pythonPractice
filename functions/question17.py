string=input("Enter a string: ")
char=input("Enter a character: ")
check=lambda x,y: x in y[0]
if check(char,string):
    print('given string starts with a given character')
else:
    print('given string do not starts with a given character')
