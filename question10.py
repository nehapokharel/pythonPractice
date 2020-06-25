word = input('Enter string: ')
newword = ""

for i in word:
    if word.index(i) % 2 == 0:
        newword += i
print(newword)