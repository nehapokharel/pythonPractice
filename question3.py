word = input("Enter string: ")

for i in word:
    if i == word[0]:
        result =word.replace(i,'$')
print(word[0]+result[1:])