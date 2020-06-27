a = input('enter sentence: ')
words = a.split()

result = []

for word in words:
    if word not in result:
        result.append(word)
print(result)