a = input('enter sentence: ')
word = a.split()
count = 0
for w in word:
    if w>1 and w[:1] == w[-1:]:
        count +=1
print(count)