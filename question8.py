word = input('Enter string: ')
number = int(input('Enter number: '))

for i in word:
    if word.index(i) == number:
        print((word[:number] + word[number+1:]))
    